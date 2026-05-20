from __future__ import annotations

import json
import shutil
import subprocess
import time
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "evaluation/tool-health/local-runners.json"

RUNNER_FAMILIES = [
    {
        "id": "claude_code",
        "label": "Claude Code",
        "probe_commands": [["claude", "--version"]],
    },
    {
        "id": "copilot",
        "label": "Copilot",
        "probe_commands": [["gh", "copilot", "--help"]],
        "version_commands": [["gh", "--version"]],
    },
    {
        "id": "codex",
        "label": "Codex",
        "probe_commands": [["codex", "--version"]],
    },
    {
        "id": "pi",
        "label": "PI",
        "probe_commands": [["pi", "--version"]],
    },
    {
        "id": "hermes_agent",
        "label": "Hermes agent",
        "probe_commands": [["hermes", "--version"]],
    },
    {
        "id": "llama",
        "label": "Llama",
        "probe_commands": [["llama", "--version"], ["ollama", "--version"], ["llama-server", "--version"]],
    },
    {
        "id": "mlx",
        "label": "MLX",
        "probe_commands": [["mlx_lm", "--help"], ["mlx", "--help"]],
    },
    {
        "id": "mlx_vlm",
        "label": "MLX VLM",
        "probe_commands": [["mlx_vlm", "--help"]],
    },
]


def run_command(command: list[str]) -> dict:
    executable = command[0]
    command_path = shutil.which(executable)
    if not command_path:
        return {
            "command": " ".join(command),
            "command_path": None,
            "status": "missing",
            "exit_code": None,
            "duration_ms": 0,
            "summary": f"{executable} is not installed",
        }

    start = time.perf_counter()
    completed = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    duration_ms = round((time.perf_counter() - start) * 1000, 2)
    output_lines = [line.strip() for line in (completed.stdout or completed.stderr).splitlines() if line.strip()]
    return {
        "command": " ".join(command),
        "command_path": command_path,
        "status": "pass" if completed.returncode == 0 else "fail",
        "exit_code": completed.returncode,
        "duration_ms": duration_ms,
        "summary": output_lines[0] if output_lines else "command produced no output",
    }


def probe_family(family: dict) -> dict:
    probe_results = [run_command(command) for command in family["probe_commands"]]
    passing_probe = next((result for result in probe_results if result["status"] == "pass"), None)

    version_summary = None
    version_commands = family.get("version_commands", family["probe_commands"])
    for command in version_commands:
        result = run_command(command)
        if result["status"] == "pass":
            version_summary = result["summary"]
            break

    if passing_probe:
        return {
            "id": family["id"],
            "label": family["label"],
            "status": "available",
            "matched_probe": passing_probe["command"],
            "command_path": passing_probe["command_path"],
            "summary": version_summary or passing_probe["summary"],
            "duration_ms": passing_probe["duration_ms"],
            "probes": probe_results,
        }

    return {
        "id": family["id"],
        "label": family["label"],
        "status": "missing",
        "matched_probe": None,
        "command_path": None,
        "summary": probe_results[0]["summary"] if probe_results else "no probe executed",
        "duration_ms": 0,
        "probes": probe_results,
    }


def main() -> int:
    results = [probe_family(family) for family in RUNNER_FAMILIES]
    available = [item["label"] for item in results if item["status"] == "available"]
    missing = [item["label"] for item in results if item["status"] != "available"]

    payload = {
        "harvest_id": "PARENT-LOCAL-RUNNERS-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "doctrine": "cli_first_local_runners",
        "metrics_contract": "contracts/parent-capability-metrics.yaml",
        "families": results,
        "summary": {
            "available_count": len(available),
            "missing_count": len(missing),
            "available": available,
            "missing": missing,
            "baseline_rule": "CLI-first local runner harvests are the default parent evaluation path. Remote-provider lanes are explicit exceptions."
        },
        "remote_exception_lanes": [
            {
                "lane": "vercel-agent-eval",
                "baseline_local_state": "dry plus local runner harvest",
                "remote_exception_requirement": "OPENAI_API_KEY for smoke/live",
            }
        ],
    }

    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
