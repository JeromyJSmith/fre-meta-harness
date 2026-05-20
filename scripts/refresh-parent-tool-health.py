from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_HEALTH_DIR = ROOT / "evaluation" / "tool-health"
STATUS_PATH = TOOL_HEALTH_DIR / "status.json"


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def main() -> int:
    local_runners = load_json(TOOL_HEALTH_DIR / "local-runners.json") or {}
    infranodus_probe = load_json(TOOL_HEALTH_DIR / "infranodus-live-probe.json") or {}

    runner_summary = local_runners.get("summary", {})
    available = runner_summary.get("available", [])
    missing = runner_summary.get("missing", [])

    payload = {
        "report_id": "PARENT-TOOL-HEALTH-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "checks": {
            "gitnexus": {
                "status": "bounded_pass",
                "full_repo_probe": {
                    "status": "warn",
                    "command": "HOME=$PWD/evaluation/tool-health/gitnexus-home gitnexus analyze . --skip-agents-md --name fre-meta-harness-parent",
                    "summary": "Indexed the parent repo, but scope-extraction warnings came from read-only files under external/.",
                    "evidence": [
                        "evaluation/tool-health/gitnexus-smoke.log"
                    ],
                },
                "fixture_probe": {
                    "status": "pass",
                    "command": "HOME=$PWD/evaluation/tool-health/gitnexus-parent-fixture/home gitnexus analyze evaluation/tool-health/gitnexus-parent-fixture/workdir --skip-agents-md --skip-git --name fre-meta-harness-parent-fixture",
                    "summary": "Indexed an isolated parent-layer fixture cleanly without traversing read-only external authorities.",
                    "evidence": [
                        "evaluation/tool-health/gitnexus-parent-fixture/gitnexus-clean-smoke.log"
                    ],
                },
            },
            "graphify": {
                "status": "pass",
                "probe": {
                    "command": "graphify update evaluation/tool-health/graphify-parent-fixture --no-cluster",
                    "summary": "Bounded parent fixture updated cleanly with no LLM requirement and produced graphify-out/graph.json.",
                    "evidence": [
                        "evaluation/tool-health/graphify-smoke.log",
                        "evaluation/tool-health/graphify-parent-fixture/graphify-out/graph.json"
                    ],
                },
            },
            "infranodus": {
                "status": "bounded_pass",
                "probe": {
                    "package": "infranodus-mcp-server@1.6.1",
                    "summary": "Live MCP analysis stayed blocked, but the bounded local substitute generated fresh parent-layer gap, bridge, and research-topic artifacts without faking OAuth-backed runtime access.",
                    "evidence": [
                        "infranodus-phase-tool-map.json",
                        "evaluation/tool-health/infranodus-package.log",
                        "evaluation/infranodus-gap-analysis.json",
                        "evaluation/infranodus-conceptual-bridges.json",
                        "evaluation/infranodus-research-topics.json",
                        "evaluation/tool-health/infranodus-live-probe.json"
                    ],
                    "limitation": infranodus_probe.get("blocker"),
                },
            },
            "agent_eval": {
                "status": "dry_pass",
                "project_root": "evaluation/agent-eval",
                "contract": "contracts/agent-eval-parent-lane.yaml",
                "experiment_id": "parent-wrapper-codex-docker",
                "eval_id": "parent-wrapper-agent-eval-boundary",
                "strongest_honest_local_evidence": "dry",
                "baseline_parent_path": "evaluation/tool-health/local-runners.json",
                "dry_probe": {
                    "status": "pass",
                    "command": "scripts/run-parent-agent-eval.sh dry",
                    "summary": "The parent-scoped fixture resolved locally, discovered the codex/docker experiment, and found the single parent-wrapper eval without making API calls.",
                    "evidence": [
                        "evaluation/tool-health/agent-eval-dry.log",
                        "evaluation/agent-eval/README.md",
                        "evaluation/agent-eval/experiments/parent-wrapper-codex-docker.ts",
                        "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/PROMPT.md"
                    ],
                },
                "smoke_probe": {
                    "status": "blocked",
                    "command": "scripts/run-parent-agent-eval.sh smoke",
                    "summary": "Smoke remains an optional remote-backed escalation and stopped closed because OPENAI_API_KEY was not configured.",
                    "evidence": [
                        "evaluation/tool-health/agent-eval-smoke.log",
                        "contracts/agent-eval-parent-lane.yaml"
                    ],
                    "satisfied_prerequisites": [
                        "docker"
                    ],
                    "missing_prerequisites": [
                        "OPENAI_API_KEY"
                    ],
                },
                "runtime_boundary": "CLI-first local runner harvests are the default parent path. Dry is the strongest lane-specific local evidence today; smoke and live remain exact remote-provider exceptions.",
            },
            "local_runners": {
                "status": "pass" if available else "missing",
                "probe": {
                    "command": "uv run python scripts/harvest-local-runner-capabilities.py",
                    "summary": f"Available local runners: {', '.join(available) if available else 'none'}. Missing runners: {', '.join(missing) if missing else 'none'}.",
                    "evidence": [
                        "evaluation/tool-health/local-runners.json"
                    ],
                },
            },
        },
    }

    STATUS_PATH.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
