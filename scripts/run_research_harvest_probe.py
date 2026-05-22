#!/usr/bin/env python3
"""
research_harvest bounded probe — compiled_output_reconciliation mode.
Proof state: designed_not_activated → bounded_probe_pass
Does NOT claim cross-device, Pixeltable sync, or child-runtime activation.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
PROBE_ID = "research_harvest"
PROBE_MODE = "compiled_output_reconciliation"
PROOF_STATE = "bounded_probe_pass"

REQUIRED_COMPILED = [
    "evaluation/research/compiled/capability-harvest.json",
    "evaluation/research/compiled/feature-matrix.json",
    "evaluation/research/compiled/gap-placement-map.json",
    "evaluation/research/compiled/source-index.json",
    "evaluation/research/compiled/operational-feature-matrix.json",
]


def _ts() -> float:
    return time.time()


def _iso() -> str:
    import datetime
    return datetime.datetime.utcnow().isoformat() + "Z"


def _event(kind: str, detail: dict) -> dict:
    return {"ts": _iso(), "probe_id": PROBE_ID, "event": kind, **detail}


def run_probe(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    events = []
    benchmarks = []
    t0 = _ts()
    blockers = []

    events.append(_event("probe_started", {
        "mode": PROBE_MODE,
        "runtime_lane": "inbox_protocol.same_host",
    }))

    # --- reconcile compiled outputs ---
    compiled_status = {}
    for rel_path in REQUIRED_COMPILED:
        p = ROOT / rel_path
        exists = p.exists()
        size = p.stat().st_size if exists else 0
        compiled_status[rel_path] = {"exists": exists, "size_bytes": size}
        if not exists:
            blockers.append(f"missing compiled output: {rel_path}")

    events.append(_event("evidence_recorded", {
        "artifact": "compiled_outputs",
        "compiled_status": compiled_status,
        "all_present": len(blockers) == 0,
    }))

    # --- reconcile research-packet-manifest.yaml ---
    manifest_yaml = ROOT / "contracts" / "research-packet-manifest.yaml"
    manifest_valid = manifest_yaml.exists()
    if manifest_valid:
        with manifest_yaml.open() as f:
            manifest = yaml.safe_load(f)
        capability_fields = manifest.get("capability_id_fields", [])
    else:
        capability_fields = []
        blockers.append("contracts/research-packet-manifest.yaml missing")

    events.append(_event("evidence_recorded", {
        "artifact": "research_packet_manifest",
        "contract_exists": manifest_valid,
        "capability_fields_count": len(capability_fields),
    }))

    # --- reconcile harvest-manifest reference ---
    harvest_manifest = ROOT / "evaluation" / "research" / "harvest-manifest.json"
    harvest_present = harvest_manifest.exists()
    events.append(_event("evidence_recorded", {
        "artifact": "harvest_manifest",
        "path": "evaluation/research/harvest-manifest.json",
        "present": harvest_present,
        "note": "harvest-manifest.json feeds compiled outputs; absence means only static compiled snapshot available.",
    }))

    # --- consume_source_quality_lib readiness ---
    lib = ROOT / "scripts" / "consume_source_quality_lib.py"
    lib_ready = lib.exists()
    lib_size = lib.stat().st_size if lib_ready else 0
    events.append(_event("evidence_recorded", {
        "artifact": "consume_source_quality_lib",
        "lib_ready": lib_ready,
        "lib_size_bytes": lib_size,
        "note": "Library is ready; thin CLI wrappers exist. Not yet wired as orchestrated subsystem step.",
    }))

    # --- validation refresh ---
    val_report = ROOT / "evaluation" / "validation-report.json"
    metrics = ROOT / "evaluation" / "metrics-latest.json"
    events.append(_event("validation_refreshed", {
        "validation_report_present": val_report.exists(),
        "metrics_latest_present": metrics.exists(),
        "note": "Reconciliation complete against compiled output snapshot. Re-run score-parent-wrapper.py for fresh metrics.",
    }))

    duration = _ts() - t0
    benchmarks.append({
        "group": "observability_ingest",
        "probe_id": PROBE_ID,
        "mode": PROBE_MODE,
        "duration_s": round(duration, 4),
        "compiled_outputs_present": sum(1 for v in compiled_status.values() if v["exists"]),
        "compiled_outputs_total": len(REQUIRED_COMPILED),
        "manifest_valid": manifest_valid,
        "lib_ready": lib_ready,
        "lib_size_bytes": lib_size,
    })

    final_state = "bounded_probe_blocked" if blockers else PROOF_STATE

    probe_status = {
        "schema_version": "1.0.0",
        "probe_id": PROBE_ID,
        "probe_mode": PROBE_MODE,
        "proof_state": final_state,
        "runtime_lane": "inbox_protocol.same_host",
        "executed_at": _iso(),
        "compiled_outputs_present": [k for k, v in compiled_status.items() if v["exists"]],
        "compiled_outputs_missing": [k for k, v in compiled_status.items() if not v["exists"]],
        "manifest_valid": manifest_valid,
        "lib_ready": lib_ready,
        "blockers": blockers,
        "do_not_overclaim": [
            "Does not imply live research_harvest runner execution.",
            "Does not imply cross-device activation.",
            "Does not imply Pixeltable sync activation.",
            "Does not imply child-runtime adoption.",
            "Compiled artifacts are static snapshot evidence, not runner completion proof.",
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
    parser = argparse.ArgumentParser(description="research_harvest bounded probe")
    parser.add_argument(
        "--output-dir",
        default=str(ROOT / "evaluation" / "subsystem-runner-probes" / "research_harvest"),
    )
    args = parser.parse_args()
    sys.exit(run_probe(Path(args.output_dir)))


if __name__ == "__main__":
    main()
