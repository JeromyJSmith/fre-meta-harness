#!/usr/bin/env python3
"""
semantic_cartography bounded probe — graph_boundary_reconciliation mode.
Proof state: designed_not_activated → bounded_probe_pass
Does NOT claim cross-device, live InfraNodus activation, or child-runtime adoption.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
PROBE_ID = "semantic_cartography"
PROBE_MODE = "graph_boundary_reconciliation"
PROOF_STATE = "bounded_probe_pass"

REQUIRED_GRAPH_ARTIFACTS = [
    "evaluation/infranodus-gap-analysis.json",
    "evaluation/infranodus-conceptual-bridges.json",
    "evaluation/infranodus-live-summary.json",
    "evaluation/infranodus-research-topics.json",
]

REUSABLE_INFRA = [
    ("colbymchenry/codegraph", "semantic index of code — not yet installed"),
    ("oxc-project/oxc", "JS/TS AST parse + transform — identified, not yet invoked"),
    ("facebook/pyrefly", "Python type checker + language server — identified, not yet invoked"),
]


def _ts() -> float:
    return time.time()


def _iso() -> str:
    import datetime
    return datetime.datetime.utcnow().isoformat() + "Z"


def _event(kind: str, detail: dict) -> dict:
    return {"ts": _iso(), "probe_id": PROBE_ID, "event": kind, **detail}


def _load_json(p: Path) -> dict:
    try:
        with p.open() as f:
            return json.load(f)
    except Exception:
        return {}


def run_probe(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    events = []
    benchmarks = []
    t0 = _ts()
    blockers = []

    events.append(_event("probe_started", {
        "mode": PROBE_MODE,
        "runtime_lane": "peer_mesh_local.same_host",
        "note": "Live InfraNodus MCP is available in this session but is kept as bounded local evidence; cross-device authenticated transport proof does not exist.",
    }))

    # --- reconcile InfraNodus graph artifacts ---
    graph_status = {}
    for rel_path in REQUIRED_GRAPH_ARTIFACTS:
        p = ROOT / rel_path
        exists = p.exists()
        size = p.stat().st_size if exists else 0
        graph_status[rel_path] = {"exists": exists, "size_bytes": size}
        if not exists:
            blockers.append(f"missing graph artifact: {rel_path}")

    events.append(_event("evidence_recorded", {
        "artifact": "infranodus_graph_artifacts",
        "artifact_status": graph_status,
        "all_present": all(v["exists"] for v in graph_status.values()),
    }))

    # --- extract cluster/gap summary from live gap-analysis ---
    gap_analysis_path = ROOT / "evaluation" / "infranodus-gap-analysis.json"
    if gap_analysis_path.exists():
        gap_data = _load_json(gap_analysis_path)
        cluster_count = len(gap_data.get("clusters", gap_data.get("topical_clusters", [])))
        gap_count = len(gap_data.get("content_gaps", gap_data.get("gaps", [])))
    else:
        cluster_count = 0
        gap_count = 0

    events.append(_event("evidence_recorded", {
        "artifact": "gap_analysis_summary",
        "cluster_count": cluster_count,
        "gap_count": gap_count,
        "note": "Cluster/gap data from bounded local InfraNodus corpus analysis; not cross-device runner proof.",
    }))

    # --- reconcile subsystem-harness-topology.yaml ---
    topology_yaml = ROOT / "contracts" / "subsystem-harness-topology.yaml"
    topology_valid = topology_yaml.exists()
    if topology_valid:
        with topology_yaml.open() as f:
            topology = yaml.safe_load(f)
        semantic_carto_in_kernel = "semantic_cartography" in str(topology)
    else:
        semantic_carto_in_kernel = False
        blockers.append("contracts/subsystem-harness-topology.yaml missing")

    events.append(_event("evidence_recorded", {
        "artifact": "subsystem_harness_topology",
        "contract_exists": topology_valid,
        "semantic_cartography_referenced": semantic_carto_in_kernel,
    }))

    # --- reconcile source-index as cartography input ---
    source_index = ROOT / "evaluation" / "research" / "compiled" / "source-index.json"
    feature_matrix = ROOT / "evaluation" / "research" / "compiled" / "feature-matrix.json"
    events.append(_event("evidence_recorded", {
        "artifact": "cartography_inputs",
        "source_index_present": source_index.exists(),
        "feature_matrix_present": feature_matrix.exists(),
        "note": "These are the planned inputs for semantic_cartography; runner not yet wired.",
    }))

    # --- reusable infrastructure readiness record ---
    events.append(_event("evidence_recorded", {
        "artifact": "reusable_infra_shortlist",
        "items": [{"repo": r, "status": s} for r, s in REUSABLE_INFRA],
        "note": "Infrastructure identified in registry.json but not yet installed or invoked for semantic cartography.",
    }))

    # --- validation refresh ---
    val_report = ROOT / "evaluation" / "validation-report.json"
    metrics = ROOT / "evaluation" / "metrics-latest.json"
    events.append(_event("validation_refreshed", {
        "validation_report_present": val_report.exists(),
        "metrics_latest_present": metrics.exists(),
        "note": "Graph boundary reconciliation complete. semantic_cartography at bounded_probe_pass; codegraph/pyrefly/oxc installation needed for activation_proven_same_host.",
    }))

    duration = _ts() - t0
    benchmarks.append({
        "group": "peer_mesh_regression",
        "probe_id": PROBE_ID,
        "mode": PROBE_MODE,
        "duration_s": round(duration, 4),
        "graph_artifacts_present": sum(1 for v in graph_status.values() if v["exists"]),
        "graph_artifacts_total": len(REQUIRED_GRAPH_ARTIFACTS),
        "cluster_count": cluster_count,
        "gap_count": gap_count,
        "topology_valid": topology_valid,
        "source_index_present": source_index.exists(),
        "feature_matrix_present": feature_matrix.exists(),
    })

    final_state = "bounded_probe_blocked" if blockers else PROOF_STATE

    probe_status = {
        "schema_version": "1.0.0",
        "probe_id": PROBE_ID,
        "probe_mode": PROBE_MODE,
        "proof_state": final_state,
        "runtime_lane": "peer_mesh_local.same_host",
        "executed_at": _iso(),
        "graph_artifacts_present": [k for k, v in graph_status.items() if v["exists"]],
        "graph_artifacts_missing": [k for k, v in graph_status.items() if not v["exists"]],
        "cluster_count": cluster_count,
        "gap_count": gap_count,
        "blockers": blockers,
        "next_activation_step": "Install colbymchenry/codegraph + oxc-project/oxc, invoke on source-index, emit semantic graph summaries.",
        "do_not_overclaim": [
            "Does not imply live semantic_cartography runner execution.",
            "Does not convert bounded local graph analysis into cross-device runner proof.",
            "Does not imply codegraph or pyrefly are installed or invoked.",
            "Does not imply child-runtime adoption.",
        ],
    }

    (output_dir / "probe-status.json").write_text(json.dumps(probe_status, indent=2))
    with (output_dir / "events.jsonl").open("w") as f:
        for ev in events:
            f.write(json.dumps(ev) + "\n")
    (output_dir / "benchmarks.json").write_text(json.dumps(benchmarks, indent=2))

    print(json.dumps(probe_status, indent=2))
    return 0 if final_state == PROOF_STATE else 1


def main():
    parser = argparse.ArgumentParser(description="semantic_cartography bounded probe")
    parser.add_argument(
        "--output-dir",
        default=str(ROOT / "evaluation" / "subsystem-runner-probes" / "semantic_cartography"),
    )
    args = parser.parse_args()
    sys.exit(run_probe(Path(args.output_dir)))


if __name__ == "__main__":
    main()
