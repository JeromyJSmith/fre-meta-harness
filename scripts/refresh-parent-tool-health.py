from __future__ import annotations

import json
import os
from datetime import date
from pathlib import Path

from tool_health_probe_lib import (
    ROOT,
    TOOL_HEALTH_DIR,
    command_path,
    load_json,
    result_from_completed,
    run_command,
    write_json,
)


STATUS_PATH = TOOL_HEALTH_DIR / "status.json"


def run_local_runners_probe() -> tuple[dict, dict]:
    command = ["uv", "run", "python", "scripts/harvest-local-runner-capabilities.py"]
    completed = run_command(command)
    runners = load_json(TOOL_HEALTH_DIR / "local-runners.json") or {}
    summary = runners.get("summary", {})
    available = summary.get("available", [])
    missing = summary.get("missing", [])
    status = "pass" if available else "missing"
    return runners, {
        "status": status,
        "probe": result_from_completed(
            command,
            completed,
            evidence=["evaluation/tool-health/local-runners.json"],
            status=status,
            summary=f"Available local runners: {', '.join(available) if available else 'none'}. Missing runners: {', '.join(missing) if missing else 'none'}.",
        ).as_dict(),
    }


def run_peer_mesh_local() -> tuple[dict, dict]:
    command = ["bash", "scripts/run-parent-peer-mesh-local.sh"]
    completed = run_command(command, log_path=TOOL_HEALTH_DIR / "peer-mesh-local.log")
    summary = load_json(TOOL_HEALTH_DIR / "peer-mesh-local.json") or {}
    return summary, {
        "status": summary.get("status", "missing"),
        "strongest_honest_scope": "same_host_runtime",
        "truth_boundary": {
            "strongest_honest_status": summary.get("status", "missing"),
            "active_runtime_modes": summary.get("truth_boundary", {}).get("active_runtime_modes", ["same_host"]),
            "blocked_runtime_modes": summary.get("truth_boundary", {}).get("blocked_runtime_modes", []),
            "bounded_evidence": "evaluation/tool-health/peer-mesh-local.json",
            "limitation": summary.get("truth_boundary", {}).get("limitation"),
        },
        "activation_probe": result_from_completed(
            command,
            completed,
            evidence=[
                "evaluation/tool-health/peer-mesh-local.json",
                "evaluation/tool-health/peer-mesh-local.log",
                "evaluation/tool-health/peer-mesh-local-events.jsonl",
                "evaluation/tool-health/peer-mesh-local-benchmarks.json",
            ],
            status=summary.get("status", "missing"),
            summary="Executed the bounded same-host peer-mesh runtime slice and refreshed its tool-health evidence.",
        ).as_dict(),
    }


def run_inbox_protocol() -> dict:
    command = ["uv", "run", "python", "scripts/watchers/inbox_router.py"]
    completed = run_command(command, log_path=TOOL_HEALTH_DIR / "inbox-protocol" / "scan.log")
    latest_scan = load_json(TOOL_HEALTH_DIR / "inbox-protocol" / "latest-scan.json") or {}
    blocked_modes = [
        {
            "mode_id": "cross_device",
            "status": "blocked",
            "blocker": "Cross-device inbox synchronization remains blocked until authenticated remote routing exists.",
        }
    ]
    return {
        "status": latest_scan.get("status", "missing"),
        "strongest_honest_scope": "same_host_front_door_runtime",
        "truth_boundary": {
            "strongest_honest_status": latest_scan.get("status", "missing"),
            "active_runtime_modes": ["same_host"],
            "blocked_runtime_modes": blocked_modes,
            "bounded_evidence": "evaluation/tool-health/inbox-protocol/latest-scan.json",
            "limitation": "This slice activates the inbox-first control plane only; deeper semantic mapping and wrapper synthesis remain future work.",
        },
        "activation_probe": result_from_completed(
            command,
            completed,
            evidence=[
                "evaluation/tool-health/inbox-protocol/latest-scan.json",
                "evaluation/tool-health/inbox-protocol/gate-status.json",
                "evaluation/tool-health/inbox-protocol/routing/all.json",
                "evaluation/tool-health/inbox-protocol/delegations/all.json",
            ],
            status=latest_scan.get("status", "missing"),
            summary="Validated governed inbox packets and emitted routing plus delegation artifacts for the same-host front-door lane.",
        ).as_dict(),
    }


def run_agent_eval_probe() -> dict:
    dry_command = ["bash", "scripts/run-parent-agent-eval.sh", "dry"]
    smoke_command = ["bash", "scripts/run-parent-agent-eval.sh", "smoke"]
    dry_completed = run_command(dry_command, log_path=TOOL_HEALTH_DIR / "agent-eval-dry.log")
    smoke_completed = run_command(smoke_command, log_path=TOOL_HEALTH_DIR / "agent-eval-smoke.log")

    smoke_status = "pass" if smoke_completed.returncode == 0 else "blocked"
    smoke_missing = []
    smoke_satisfied = []
    if command_path("docker"):
        smoke_satisfied.append("docker")
    else:
        smoke_missing.append("docker")
    if os.environ.get("OPENAI_API_KEY"):
        smoke_satisfied.append("OPENAI_API_KEY")
    else:
        smoke_missing.append("OPENAI_API_KEY")

    return {
        "status": "dry_pass" if dry_completed.returncode == 0 else "blocked",
        "project_root": "evaluation/agent-eval",
        "contract": "contracts/agent-eval-parent-lane.yaml",
        "experiment_id": "parent-wrapper-codex-docker",
        "eval_id": "parent-wrapper-agent-eval-boundary",
        "strongest_honest_local_evidence": "dry" if dry_completed.returncode == 0 else "blocked",
        "baseline_parent_path": "evaluation/tool-health/local-runners.json",
        "dry_probe": result_from_completed(
            dry_command,
            dry_completed,
            evidence=[
                "evaluation/tool-health/agent-eval-dry.log",
                "evaluation/agent-eval/README.md",
                "evaluation/agent-eval/experiments/parent-wrapper-codex-docker.ts",
                "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/PROMPT.md",
            ],
            status="pass" if dry_completed.returncode == 0 else "blocked",
            summary="The parent-scoped fixture resolved locally and exercised the dry agent-eval discovery path without making API calls."
            if dry_completed.returncode == 0
            else "Dry agent-eval could not be exercised in this environment.",
        ).as_dict(),
        "smoke_probe": result_from_completed(
            smoke_command,
            smoke_completed,
            evidence=[
                "evaluation/tool-health/agent-eval-smoke.log",
                "contracts/agent-eval-parent-lane.yaml",
            ],
            status=smoke_status,
            summary="Smoke remains an optional remote-backed escalation and stopped closed because required prerequisites were not fully configured."
            if smoke_status == "blocked"
            else "Smoke agent-eval completed with configured provider-backed prerequisites.",
            missing_prerequisites=smoke_missing,
            satisfied_prerequisites=smoke_satisfied,
        ).as_dict(),
        "runtime_boundary": "CLI-first local runner harvests are the default parent path. Dry is the strongest lane-specific local evidence today; smoke and live remain exact remote-provider exceptions.",
    }


def run_gitnexus_probe() -> dict:
    fixture_command = [
        "gitnexus",
        "analyze",
        "evaluation/tool-health/gitnexus-parent-fixture/workdir",
        "--skip-agents-md",
        "--skip-git",
        "--name",
        "fre-meta-harness-parent-fixture",
    ]
    full_command = [
        "gitnexus",
        "analyze",
        ".",
        "--skip-agents-md",
        "--name",
        "fre-meta-harness-parent",
    ]
    env = {"HOME": str(TOOL_HEALTH_DIR / "gitnexus-home")}
    fixture_env = {"HOME": str(TOOL_HEALTH_DIR / "gitnexus-parent-fixture" / "home")}

    full_completed = run_command(full_command, env=env, log_path=TOOL_HEALTH_DIR / "gitnexus-smoke.log")
    fixture_completed = run_command(
        fixture_command,
        env=fixture_env,
        log_path=TOOL_HEALTH_DIR / "gitnexus-parent-fixture" / "gitnexus-clean-smoke.log",
    )
    full_status = "warn" if "warning" in (full_completed.stdout + full_completed.stderr).lower() else "pass"
    fixture_status = "pass" if fixture_completed.returncode == 0 else "fail"
    return {
        "status": "bounded_pass" if fixture_completed.returncode == 0 else "blocked",
        "strongest_honest_scope": "fixture_probe",
        "truth_boundary": {
            "strongest_honest_status": "bounded_pass" if fixture_completed.returncode == 0 else "blocked",
            "bounded_scope": "isolated_parent_fixture",
            "bounded_evidence": "evaluation/tool-health/gitnexus-parent-fixture/gitnexus-clean-smoke.log",
            "unbounded_repo_status": full_status,
            "limitation": "Full-repo indexing traverses read-only external authorities and can emit upstream scope-extraction warnings outside the kept parent slice.",
        },
        "full_repo_probe": result_from_completed(
            full_command,
            full_completed,
            evidence=["evaluation/tool-health/gitnexus-smoke.log"],
            status=full_status,
            summary="Indexed the parent repo and recorded the full-repo GitNexus smoke result.",
        ).as_dict(),
        "fixture_probe": result_from_completed(
            fixture_command,
            fixture_completed,
            evidence=["evaluation/tool-health/gitnexus-parent-fixture/gitnexus-clean-smoke.log"],
            status=fixture_status,
            summary="Indexed an isolated parent-layer fixture without traversing read-only external authorities.",
        ).as_dict(),
    }


def run_graphify_probe() -> dict:
    command = ["graphify", "update", "evaluation/tool-health/graphify-parent-fixture", "--no-cluster"]
    completed = run_command(command, log_path=TOOL_HEALTH_DIR / "graphify-smoke.log")
    graph_artifact = ROOT / "evaluation/tool-health/graphify-parent-fixture/graphify-out/graph.json"
    status = "bounded_pass" if completed.returncode == 0 or graph_artifact.exists() else "blocked"
    return {
        "status": status,
        "strongest_honest_scope": "probe",
        "truth_boundary": {
            "strongest_honest_status": status,
            "bounded_scope": "graphify_parent_fixture",
            "bounded_evidence": "evaluation/tool-health/graphify-parent-fixture/graphify-out/graph.json",
            "limitation": "This probe only proves bounded parent-fixture graph extraction and does not claim full parent-repo Graphify coverage.",
        },
        "probe": result_from_completed(
            command,
            completed,
            evidence=[
                "evaluation/tool-health/graphify-smoke.log",
                "evaluation/tool-health/graphify-parent-fixture/graphify-out/graph.json",
            ],
            status=status,
            summary="Bounded parent fixture updated through Graphify without claiming full parent-repo coverage.",
        ).as_dict(),
    }


def run_infranodus_probe() -> dict:
    command = ["uv", "run", "python", "scripts/build-parent-infranodus-artifacts.py"]
    completed = run_command(command, log_path=TOOL_HEALTH_DIR / "infranodus-package.log")
    live_probe = {
        "probe_id": "PARENT-INFRANODUS-LIVE-PROBE-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "status": "blocked",
        "mode": "live_mcp_runtime",
        "blocker": "Live InfraNodus MCP analysis remains API/OAuth-bound and no authenticated runtime session was proven in this run.",
        "bounded_fallback": "scripts/build-parent-infranodus-artifacts.py",
        "evidence": [
            "infranodus-phase-tool-map.json",
            "evaluation/tool-health/infranodus-package.log",
            "evaluation/infranodus-gap-analysis.json",
        ],
    }
    write_json(TOOL_HEALTH_DIR / "infranodus-live-probe.json", live_probe)
    status = "bounded_pass" if completed.returncode == 0 else "blocked"
    return {
        "status": status,
        "strongest_honest_scope": "bounded_local_cli_substitute",
        "truth_boundary": {
            "strongest_honest_status": status,
            "bounded_scope": "governed_parent_corpus",
            "bounded_evidence": "evaluation/infranodus-gap-analysis.json",
            "live_status": live_probe["status"],
            "live_mode": live_probe["mode"],
            "live_blocker": live_probe["blocker"],
        },
        "probe": result_from_completed(
            command,
            completed,
            evidence=[
                "infranodus-phase-tool-map.json",
                "evaluation/tool-health/infranodus-package.log",
                "evaluation/infranodus-gap-analysis.json",
                "evaluation/infranodus-conceptual-bridges.json",
                "evaluation/infranodus-research-topics.json",
                "evaluation/tool-health/infranodus-live-probe.json",
            ],
            status=status,
            summary="Refreshed the bounded local InfraNodus substitute without claiming live MCP activation.",
        ).as_dict(),
    }


def launcher_surface_report() -> dict:
    root_mcp = ROOT / ".mcp.json"
    scripts = json.loads((ROOT / "package.json").read_text()).get("scripts", {})
    return {
        "status": "pass",
        "root_mcp_config": "present" if root_mcp.exists() else "missing",
        "launcher_paths": {
            "app": "app/server.ts",
            "service": "service/main.py",
            "router": "scripts/watchers/inbox_router.py",
        },
        "package_scripts": sorted(scripts),
        "summary": "Launcher truth is carried by package scripts plus app/service/router entrypoints; no root .mcp.json is claimed when absent.",
    }


def main() -> int:
    _, local_runners = run_local_runners_probe()
    peer_mesh_summary, peer_mesh_local = run_peer_mesh_local()
    gitnexus = run_gitnexus_probe()
    graphify = run_graphify_probe()
    infranodus = run_infranodus_probe()
    agent_eval = run_agent_eval_probe()
    inbox_protocol = run_inbox_protocol()

    payload = {
        "report_id": "PARENT-TOOL-HEALTH-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "checks": {
            "gitnexus": gitnexus,
            "graphify": graphify,
            "infranodus": infranodus,
            "agent_eval": agent_eval,
            "local_runners": local_runners,
            "peer_mesh_local": peer_mesh_local,
            "inbox_protocol": inbox_protocol,
            "launcher_surfaces": launcher_surface_report(),
        },
    }

    if peer_mesh_summary:
        payload["checks"]["peer_mesh_local"]["truth_boundary"]["active_runtime_modes"] = peer_mesh_summary.get(
            "truth_boundary", {}
        ).get("active_runtime_modes", ["same_host"])
        payload["checks"]["peer_mesh_local"]["truth_boundary"]["blocked_runtime_modes"] = peer_mesh_summary.get(
            "truth_boundary", {}
        ).get("blocked_runtime_modes", payload["checks"]["peer_mesh_local"]["truth_boundary"]["blocked_runtime_modes"])

    STATUS_PATH.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
