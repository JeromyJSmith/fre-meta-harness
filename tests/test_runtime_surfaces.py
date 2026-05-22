from __future__ import annotations

import http.server
import json
import os
import shutil
import socketserver
import subprocess
import threading
import time
import unittest
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

from service.inbox_runtime import build_routing_artifacts, inbox_snapshot, scan_inbox_packets
from service.main import delegations, health, inbox_queue, inbox_scan, inbox_packets, routing_results


ROOT = Path(__file__).resolve().parents[1]


def wait_for_json(url: str, timeout: float = 15.0) -> dict:
    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            with urlopen(url) as response:  # noqa: S310
                return json.loads(response.read().decode("utf-8"))
        except (URLError, ConnectionError, json.JSONDecodeError) as exc:
            last_error = exc
            time.sleep(0.2)
    raise AssertionError(f"Timed out waiting for {url}: {last_error}")


class ServiceRouteTests(unittest.TestCase):
    def test_health_endpoint(self) -> None:
        self.assertEqual(health(), {"status": "ok"})

    def test_queue_endpoint_shape(self) -> None:
        payload = inbox_queue()
        self.assertIn("packets", payload)
        self.assertIn("routing_decisions", payload)
        self.assertIn("delegation_bundles", payload)
        self.assertEqual(inbox_packets(), payload["packets"])
        self.assertEqual(routing_results(), payload["routing_decisions"])
        self.assertEqual(delegations(), payload["delegation_bundles"])

    def test_scan_endpoint_writes_known_artifacts(self) -> None:
        payload = inbox_scan()
        self.assertEqual(payload["status"], "ok")
        self.assertTrue((ROOT / payload["routing_decision_path"]).exists())
        self.assertTrue((ROOT / payload["delegation_bundle_path"]).exists())


class InboxRuntimeTests(unittest.TestCase):
    def test_scan_and_routing_stay_consistent(self) -> None:
        results = scan_inbox_packets()
        artifacts = build_routing_artifacts(results)
        snapshot = inbox_snapshot()

        self.assertEqual(len(snapshot["packets"]), len(results))
        self.assertEqual(len(snapshot["routing_decisions"]), len(artifacts["decisions"]))
        self.assertEqual(len(snapshot["delegation_bundles"]), len(artifacts["bundles"]))
        self.assertGreaterEqual(len(results), 1)


class RouterScriptSmokeTests(unittest.TestCase):
    def test_router_script_emits_counts_json(self) -> None:
        completed = subprocess.run(
            ["uv", "run", "python", "scripts/watchers/inbox_router.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, msg=completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertIn("packet_count", payload)
        self.assertIn("routed_count", payload)
        self.assertTrue((ROOT / "evaluation/tool-health/inbox-protocol/latest-scan.json").exists())


class ToolHealthRefreshTests(unittest.TestCase):
    def test_refresh_produces_status_with_runtime_and_launcher_lanes(self) -> None:
        completed = subprocess.run(
            ["uv", "run", "--isolated", "--with", "jsonschema", "--with", "pyyaml", "python", "scripts/refresh-parent-tool-health.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, msg=completed.stderr)
        status_payload = json.loads((ROOT / "evaluation/tool-health/status.json").read_text())
        checks = status_payload["checks"]
        self.assertIn("peer_mesh_local", checks)
        self.assertIn("inbox_protocol", checks)
        self.assertIn("local_runners", checks)
        self.assertIn("agent_eval", checks)
        self.assertIn("launcher_surfaces", checks)
        self.assertEqual(checks["launcher_surfaces"]["root_mcp_config"], "missing")


class _ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        payload = {"method": "GET", "path": self.path}
        body = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


class AppServerSmokeTests(unittest.TestCase):
    def setUp(self) -> None:
        if shutil.which("bun") is None:
            raise unittest.SkipTest("bun is required for app/server.ts smoke coverage")

        class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
            allow_reuse_address = True

        self.backend = ThreadingTCPServer(("127.0.0.1", 0), _ProxyHandler)
        self.backend_thread = threading.Thread(target=self.backend.serve_forever, daemon=True)
        self.backend_thread.start()
        self.backend_url = f"http://127.0.0.1:{self.backend.server_address[1]}"

        self.app_port = "32113"
        env = os.environ.copy()
        env["PORT"] = self.app_port
        env["INBOX_SERVICE_URL"] = self.backend_url
        self.app_proc = subprocess.Popen(
            ["bun", "app/server.ts"],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        wait_for_json(f"http://127.0.0.1:{self.app_port}/health")

    def tearDown(self) -> None:
        if hasattr(self, "app_proc"):
            self.app_proc.terminate()
            try:
                self.app_proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.app_proc.kill()
                self.app_proc.wait(timeout=10)
        if hasattr(self, "backend"):
            self.backend.shutdown()
            self.backend.server_close()
        if hasattr(self, "backend_thread"):
            self.backend_thread.join(timeout=5)

    def test_health_and_config_routes(self) -> None:
        health = wait_for_json(f"http://127.0.0.1:{self.app_port}/health")
        config = wait_for_json(f"http://127.0.0.1:{self.app_port}/config.json")
        self.assertEqual(health, {"status": "ok"})
        self.assertEqual(config["serviceOrigin"], self.backend_url)

    def test_proxy_route_forwards_to_service_origin(self) -> None:
        proxied = wait_for_json(f"http://127.0.0.1:{self.app_port}/api/runtime-check?hello=1")
        self.assertEqual(proxied["method"], "GET")
        self.assertEqual(proxied["path"], "/api/runtime-check?hello=1")

    def test_html_shell_renders(self) -> None:
        with urlopen(f"http://127.0.0.1:{self.app_port}/") as response:  # noqa: S310
            html = response.read().decode("utf-8")
        self.assertIn("Inbox Protocol Dashboard", html)
        self.assertIn("Scan inbox", html)
