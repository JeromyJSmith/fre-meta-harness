from __future__ import annotations

import json
from datetime import date

from jsonschema import Draft202012Validator


def build_reporting_checks(core, iteration_rows: list[dict], iteration_errors: list[str], ratchet_schema: dict) -> tuple[list[dict], dict | None]:
    checks: list[dict] = []
    iterations_path = core.ROOT / "runs/iterations.jsonl"
    iteration_validator = Draft202012Validator(json.loads((core.ROOT / "schemas/iteration-record.schema.json").read_text()))
    invalid_rows = []
    for index, row in enumerate(iteration_rows, start=1):
        row_errors = sorted(iteration_validator.iter_errors(row), key=lambda error: list(error.path))
        if row_errors:
            invalid_rows.append({"row": index, "errors": [error.message for error in row_errors]})
    checks.append(
        {
            "name": "iteration_ledger_contract",
            "status": "pass" if not iteration_errors and not invalid_rows else "fail",
            "details": {
                "path": str(iterations_path.relative_to(core.ROOT)),
                "row_count": len(iteration_rows),
                "parse_errors": iteration_errors,
                "invalid_rows": invalid_rows,
            },
        }
    )

    ratchet_report_path = core.ROOT / "evaluation/copilot-ratchet-report.json"
    ratchet_check = {
        "name": "copilot_ratchet_report_contract",
        "status": "pass",
        "details": {"status": "missing"},
    }
    report_instance = None
    if ratchet_report_path.exists():
        report_instance = json.loads(ratchet_report_path.read_text())
        errors = sorted(Draft202012Validator(ratchet_schema).iter_errors(report_instance), key=lambda error: error.path)
        ratchet_check = {
            "name": "copilot_ratchet_report_contract",
            "status": "pass" if not errors else "fail",
            "details": {
                "path": str(ratchet_report_path.relative_to(core.ROOT)),
                "errors": [error.message for error in errors],
            },
        }
    checks.append(ratchet_check)

    runtime_truth_check = {
        "name": "runtime_truth_reporting_contract",
        "status": "fail",
        "details": {"errors": ["evaluation/copilot-ratchet-report.json is missing."]},
    }
    if report_instance is not None:
        details = core.validate_report_runtime_truth(report_instance, iteration_rows)
        runtime_truth_check = {
            "name": "runtime_truth_reporting_contract",
            "status": "pass" if not details["errors"] else "fail",
            "details": details,
        }
    checks.append(runtime_truth_check)

    return checks, report_instance


def build_readiness(core, overall: str, iteration_errors: list[str], report_instance: dict | None, ratchet_schema: dict, iteration_rows: list[dict]) -> dict:
    ratchet_blockers = []
    report_path = core.ROOT / "evaluation/copilot-ratchet-report.json"
    if iteration_errors:
        ratchet_blockers.append("Iteration ledger does not satisfy the iteration record contract.")
    if report_instance is None:
        ratchet_blockers.append("Real copilot-ratchet-report.json is missing.")
    else:
        schema_errors = list(Draft202012Validator(ratchet_schema).iter_errors(report_instance))
        if schema_errors:
            ratchet_blockers.append("Real copilot-ratchet-report.json does not satisfy the report schema.")
        runtime_truth_details = core.validate_report_runtime_truth(report_instance, iteration_rows)
        if runtime_truth_details["errors"]:
            ratchet_blockers.append("Real copilot-ratchet-report.json does not satisfy the runtime-truth reporting contract.")
        if int(report_instance.get("real_non_dry_cycles_executed", 0)) < 2:
            ratchet_blockers.append("Real copilot ratchet executed fewer than 2 non-dry cycles.")

    status_report = json.loads((core.ROOT / "evaluation/tool-health/status.json").read_text())
    tool_checks = status_report.get("checks", {})
    active_parent_runtime_lanes = ["peer_mesh_local.same_host", "inbox_protocol.same_host"]
    blocked_parent_runtime_lanes = [
        {"lane_id": "peer_mesh_local.cross_device", "status": "blocked"},
        {"lane_id": "inbox_protocol.cross_device", "status": "blocked"},
    ]

    return {
        "readiness_id": "PARENT-META-PROMOTION-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "status": "pass" if overall == "pass" and not ratchet_blockers else "blocked",
        "blockers": ([] if overall == "pass" else ["Parent wrapper contract validation failed."]) + ratchet_blockers,
        "runtime_truth_level": "bounded_runtime",
        "active_parent_runtime_lanes": active_parent_runtime_lanes,
        "blocked_parent_runtime_lanes": blocked_parent_runtime_lanes,
        "optional_tool_lanes": {
            "gitnexus": tool_checks.get("gitnexus", {}).get("status"),
            "graphify": tool_checks.get("graphify", {}).get("status"),
            "infranodus_live": tool_checks.get("infranodus", {}).get("truth_boundary", {}).get("live_status"),
            "agent_eval_smoke": tool_checks.get("agent_eval", {}).get("smoke_probe", {}).get("status"),
        },
        "do_not_overclaim_notes": [
            "same_host peer_mesh_local and inbox_protocol remain the only active parent runtime lanes.",
            "cross_device remains blocked until authenticated transport is proven.",
            "optional tool and provider-backed lanes do not upgrade promotion status by file presence alone.",
        ],
        "evidence": [
            "evaluation/validation-report.json",
            "evaluation/copilot-ratchet-report.json",
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/peer-mesh-local.json",
            "evaluation/tool-health/inbox-protocol/latest-scan.json",
            "program.md",
            "library.yaml",
            "source/parent-operational-doctrine.md",
            "runs/iterations.jsonl",
        ]
        + sorted(core.INBOX_PROTOCOL_CONTRACTS.keys())
        + [schema for schema in core.INBOX_PROTOCOL_CONTRACTS.values()]
        + [item[0] for item in core.INBOX_PROTOCOL_VALID_EXAMPLES]
        + sorted(core.FRONT_DOOR_LIFECYCLE_CONTRACTS.keys())
        + [schema for schema in core.FRONT_DOOR_LIFECYCLE_CONTRACTS.values()]
        + [item[0] for item in core.FRONT_DOOR_LIFECYCLE_VALID_EXAMPLES],
    }
