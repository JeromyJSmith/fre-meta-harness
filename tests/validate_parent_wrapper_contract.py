from __future__ import annotations

import json
from datetime import date

from jsonschema import Draft202012Validator

import validator_core as core
from validator_slices.governance_and_runtime import build_governance_and_runtime_checks
from validator_slices.reporting_and_promotion import build_reporting_checks, build_readiness
from validator_slices.scaffold_and_examples import build_scaffold_and_example_checks
from validator_slices.subsystems_and_tooling import build_subsystems_and_tooling_checks


def main() -> int:
    front_schema = json.loads((core.ROOT / "schemas/front-matter.schema.json").read_text())
    bottom_schema = json.loads((core.ROOT / "schemas/bottom-matter.schema.json").read_text())
    front_validator = Draft202012Validator(front_schema)
    bottom_validator = Draft202012Validator(bottom_schema)

    checks = []
    checks.extend(build_scaffold_and_example_checks(core, front_validator, bottom_validator))
    checks.extend(build_governance_and_runtime_checks(core))
    checks.extend(build_subsystems_and_tooling_checks(core))

    iterations_path = core.ROOT / "runs/iterations.jsonl"
    iteration_rows, iteration_errors = core.load_jsonl(iterations_path)
    ratchet_schema = json.loads((core.ROOT / "schemas/copilot-ratchet-report.schema.json").read_text())

    reporting_checks, report_instance = build_reporting_checks(core, iteration_rows, iteration_errors, ratchet_schema)
    checks.extend(reporting_checks)

    overall = "pass" if all(item["status"] == "pass" for item in checks) else "fail"
    report = {
        "report_id": "PARENT-META-VALIDATION-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "overall_status": overall,
        "checks": checks,
    }
    (core.ROOT / "evaluation/validation-report.json").write_text(json.dumps(report, indent=2) + "\n")

    readiness = build_readiness(core, overall, iteration_errors, report_instance, ratchet_schema, iteration_rows)
    (core.ROOT / "promotion/readiness.json").write_text(json.dumps(readiness, indent=2) + "\n")

    print(json.dumps(report, indent=2))
    return 0 if overall == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
