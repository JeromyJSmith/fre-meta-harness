from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
EDITABLE_FILES = {
    "GOAL.md",
    "domain_spec.md",
    "program.md",
    "library.yaml",
    "agentics-library.md",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "MEMORY.md",
    "GOLDENPATH.md",
}
EDITABLE_PREFIXES = (
    "source/",
    "schemas/",
    "examples/",
    "expected-failures/",
    "tests/",
    "evaluation/",
    "promotion/",
    "prompts/",
    "runs/",
    "scripts/",
)
REQUIRED_ARTIFACTS = [
    "evaluation/validation-report.json",
    "evaluation/metrics-latest.json",
    "promotion/readiness.json",
    "runs/iterations.jsonl",
]


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def load_iterations() -> tuple[list[dict], list[str]]:
    path = ROOT / "runs/iterations.jsonl"
    if not path.exists():
        return [], []
    rows = []
    errors = []
    validator = Draft202012Validator(load_iteration_schema())
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: {exc.msg}")
            continue
        row_errors = [error.message for error in validator.iter_errors(row)]
        if row_errors:
            errors.append(f"line {line_number}: {' | '.join(row_errors)}")
            continue
        rows.append(row)
    return rows, errors


def load_report_schema() -> dict:
    return json.loads((ROOT / "schemas/copilot-ratchet-report.schema.json").read_text())


def load_iteration_schema() -> dict:
    return json.loads((ROOT / "schemas/iteration-record.schema.json").read_text())


def validate_report() -> tuple[dict | None, list[str]]:
    report = load_json(ROOT / "evaluation/copilot-ratchet-report.json")
    if not report:
        return None, ["missing"]
    schema = load_report_schema()
    errors = [error.message for error in Draft202012Validator(schema).iter_errors(report)]
    return report, errors


def is_mutable_path(path: str) -> bool:
    normalized = path.lstrip("./")
    return normalized in EDITABLE_FILES or any(normalized.startswith(prefix) for prefix in EDITABLE_PREFIXES)


def real_iterations(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda row: int(row["iteration"]))


def consecutive_non_improving_cycles(score_history: list[dict]) -> int:
    count = 0
    for item in reversed(score_history):
        result = item.get("result")
        kept = item.get("kept")
        if result in {"reverted", "rejected"} or kept is False:
            count += 1
        else:
            break
    return count


def artifact_span_seconds(paths: list[str]) -> float | None:
    timestamps = []
    for rel in paths:
        path = ROOT / rel
        if not path.exists():
            return None
        timestamps.append(path.stat().st_mtime)
    if not timestamps:
        return None
    return max(timestamps) - min(timestamps)


def validator_health() -> tuple[float, dict]:
    report = load_json(ROOT / "evaluation/validation-report.json")
    if not report:
        return 0.0, {"status": "missing"}
    status = report.get("overall_status")
    return (40.0 if status == "pass" else 0.0), {"status": status}


def report_completeness() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    if not report:
        return 0.0, {"status": "missing"}
    score = 0.0
    if not schema_errors:
        score += 15.0
    required_top_level = [
        "status",
        "metric_decision",
        "metric_reason",
        "metric_review",
        "real_non_dry_cycles_executed",
        "stop_reason",
        "stop_evidence",
        "score_history",
        "files_changed",
        "artifacts",
        "iteration_ledger_entries_appended",
    ]
    present = sum(1 for key in required_top_level if key in report)
    score += round(9.0 * present / len(required_top_level), 2)
    history = report.get("score_history", [])
    detailed_rows = sum(
        1
        for item in history
        if {
            "cycle",
            "before_total_score",
            "after_total_score",
            "before_outcome_score",
            "after_outcome_score",
            "before_instrument_score",
            "after_instrument_score",
            "changed_files",
            "kept",
            "summary",
        }.issubset(item.keys())
    )
    score += round(6.0 * (detailed_rows / len(history)), 2) if history else 0.0
    ledger_aligned = len(rows) == int(report.get("real_non_dry_cycles_executed", 0)) == len(history)
    return round(score, 2), {
        "schema_errors": schema_errors,
        "history_rows": len(history),
        "detailed_rows": detailed_rows,
        "ledger_rows": len(rows),
        "ledger_aligned": ledger_aligned,
        "parse_errors": parse_errors,
    }


def metric_decision_truth() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    if not report:
        return 0.0, {"status": "missing"}
    decision = report.get("metric_decision")
    reason = report.get("metric_reason", "")
    review = report.get("metric_review", {})
    score = 0.0
    if decision in {"accepted", "repaired"} and bool(reason):
        score += 5.0
    if review.get("trustworthy") is True:
        score += 10.0
    if review.get("trust_signals"):
        score += 5.0
    if decision == "repaired" and review.get("problems_found") and review.get("repair_actions"):
        score += 10.0
    if decision == "accepted" and not review.get("problems_found") and review.get("repair_actions") == []:
        score += 10.0
    return round(score, 2), {
        "decision": decision,
        "has_reason": bool(reason),
        "schema_errors": schema_errors,
        "trustworthy": review.get("trustworthy"),
    }


def ratchet_execution() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    real_rows = real_iterations(rows)
    if not real_rows:
        return 0.0, {"status": "missing", "parse_errors": parse_errors}
    score = 0.0
    if real_rows:
        score += 10.0
    if all(row.get("validator_status") == "pass" for row in real_rows):
        score += 5.0
    mutable_files = [
        path
        for row in real_rows
        for path in row.get("changed_files", [])
        if is_mutable_path(path)
    ]
    total_changed = sum(len(row.get("changed_files", [])) for row in real_rows)
    if total_changed and len(mutable_files) == total_changed:
        score += 5.0
    if report and not schema_errors and len(report.get("score_history", [])) == len(real_rows):
        score += 8.0
    elif report and report.get("score_history"):
        score += 3.0
    return round(min(score, 25.0), 2), {
        "status": None if not report else report.get("status"),
        "schema_errors": schema_errors,
        "real_rows": len(real_rows),
        "parse_errors": parse_errors,
        "mutable_files": len(mutable_files),
        "files_changed": total_changed,
    }


def non_dry_cycle_depth() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    real_rows = real_iterations(rows)
    count = len(real_rows)
    if count == 0:
        return 0.0, {"status": "missing", "parse_errors": parse_errors}
    history = [] if not report else report.get("score_history", [])
    score = 10.0 if count == 1 else (20.0 if count == 2 else 25.0)
    if report and len(history) == count:
        score += 5.0
    return round(min(score, 25.0), 2), {
        "count": count,
        "history_rows": len(history),
        "real_rows": len(real_rows),
        "parse_errors": parse_errors,
        "schema_errors": schema_errors,
    }


def plateau_or_blocker_truth() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    history = real_iterations(rows)
    if not history or not report:
        return 0.0, {"status": "missing", "parse_errors": parse_errors}
    stop_reason = report.get("stop_reason", "")
    cycles = len(history)
    actual_consecutive = consecutive_non_improving_cycles(history)
    stop_evidence = report.get("stop_evidence", {})
    kind = stop_evidence.get("kind")
    score = 0.0
    if kind == "continuing":
        valid = report.get("status") == "running" and actual_consecutive < 2
        score = 25.0 if valid else 0.0
    elif kind == "plateau":
        valid = (
            report.get("status") == "pass"
            and cycles >= 2
            and int(report.get("real_non_dry_cycles_executed", 0)) == cycles
            and int(stop_evidence.get("consecutive_non_improving_cycles", 0)) >= 2
            and actual_consecutive >= 2
        )
        score = 25.0 if valid else 0.0
    elif kind == "blocker":
        valid = report.get("status") == "blocked" and bool(stop_evidence.get("blocker_details"))
        score = 25.0 if valid else 0.0
    return round(min(score, 25.0), 2), {
        "kind": kind,
        "stop_reason": stop_reason,
        "cycles": cycles,
        "actual_consecutive_non_improving": actual_consecutive,
        "schema_errors": schema_errors,
    }


def artifact_refresh() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    if not report and not rows:
        return 0.0, {"status": "missing"}
    artifacts = [] if not report else report.get("artifacts", [])
    listed = [artifact for artifact in REQUIRED_ARTIFACTS if artifact in artifacts]
    existing = [artifact for artifact in REQUIRED_ARTIFACTS if (ROOT / artifact).exists()]
    ledger_artifacts = sorted({artifact for row in rows for artifact in row.get("artifacts", [])})
    ledger_listed = [artifact for artifact in REQUIRED_ARTIFACTS if artifact in ledger_artifacts]
    score = round(7.5 * len(listed) / len(REQUIRED_ARTIFACTS), 2)
    score += round(7.5 * len(ledger_listed) / len(REQUIRED_ARTIFACTS), 2)
    score += round(10.0 * len(existing) / len(REQUIRED_ARTIFACTS), 2)
    span_seconds = artifact_span_seconds(
        [
            "evaluation/copilot-ratchet-report.json",
            "evaluation/validation-report.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
        ]
    )
    if span_seconds is not None and span_seconds <= 600:
        score += 5.0
    return round(min(score, 25.0), 2), {
        "listed": len(listed),
        "ledger_listed": len(ledger_listed),
        "existing": len(existing),
        "required": len(REQUIRED_ARTIFACTS),
        "freshness_span_seconds": span_seconds,
        "schema_errors": schema_errors,
        "parse_errors": parse_errors,
    }


def build_score() -> dict:
    iterations, iteration_parse_errors = load_iterations()
    outcome_components = {}
    for name, fn in [
        ("ratchet_execution", ratchet_execution),
        ("non_dry_cycle_depth", non_dry_cycle_depth),
        ("plateau_or_blocker_truth", plateau_or_blocker_truth),
        ("artifact_refresh", artifact_refresh),
    ]:
        score, details = fn()
        outcome_components[name] = {"score": score, "details": details}

    instrument_components = {}
    for name, fn in [
        ("validator_health", validator_health),
        ("report_completeness", report_completeness),
        ("metric_decision_truth", metric_decision_truth),
    ]:
        score, details = fn()
        instrument_components[name] = {"score": score, "details": details}

    outcome_score = round(sum(item["score"] for item in outcome_components.values()), 2)
    instrument_score = round(sum(item["score"] for item in instrument_components.values()), 2)
    total_score = round(0.75 * outcome_score + 0.25 * instrument_score, 2)

    weakest_component = min(
        {**outcome_components, **instrument_components}.items(),
        key=lambda item: item[1]["score"],
    )[0]

    payload = {
        "score_id": "PARENT-META-SCORE-0002",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "metric_mode": "split-ledger-validated",
        "total_score": total_score,
        "outcome_score": outcome_score,
        "instrument_score": instrument_score,
        "weakest_component": weakest_component,
        "outcome_components": outcome_components,
        "instrument_components": instrument_components,
        "iteration_count": len(real_iterations(iterations)),
        "iteration_parse_errors": iteration_parse_errors,
    }
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    payload = build_score()
    (ROOT / "evaluation/metrics-latest.json").write_text(json.dumps(payload, indent=2) + "\n")
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"total_score={payload['total_score']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
