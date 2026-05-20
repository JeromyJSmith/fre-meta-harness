from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SCAFFOLD = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GOAL.md",
    "GOLDENPATH.md",
    "MEMORY.md",
]
REQUIRED_PROMPT_CONTRACT = [
    "agent-heavy-run-prompt-index.md",
    "agent-heavy-run-prompt-schema.md",
    "agent-heavy-run-prompt.schema.json",
    "agent-heavy-run-prompt.template.yaml",
    "copilot-prompting-playbook.md",
]
REQUIRED_PROGRAM_FILES = [
    "program.md",
]
REQUIRED_DIRECTORIES = [
    "source",
    "schemas",
    "examples",
    "expected-failures",
    "tests",
    "evaluation",
    "promotion",
]
REQUIRED_EXTERNAL_REPOS = {
    "goal-md": [
        "README.md",
        "template/GOAL.md",
    ],
    "meta-harness": [
        "README.md",
        "ONBOARDING.md",
    ],
    "autoresearch-mlx": [
        "README.md",
        "program.md",
    ],
}


def parse_markdown_contract(path: Path) -> tuple[dict, dict]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path.name}: missing front matter start")
    _, rest = text.split("---\n", 1)
    front_raw, body = rest.split("\n---\n", 1)
    if "\n---bottom-matter---\n" not in body:
        raise ValueError(f"{path.name}: missing bottom matter marker")
    _, bottom_raw = body.split("\n---bottom-matter---\n", 1)
    front = yaml.safe_load(front_raw) or {}
    bottom = yaml.safe_load(bottom_raw) or {}
    return front, bottom


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    rows = []
    errors = []
    if not path.exists():
        return rows, errors
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: {exc.msg}")
    return rows, errors


def validate_examples() -> list[dict]:
    results = []
    front_schema = json.loads((ROOT / "schemas/front-matter.schema.json").read_text())
    bottom_schema = json.loads((ROOT / "schemas/bottom-matter.schema.json").read_text())
    ratchet_schema = json.loads((ROOT / "schemas/copilot-ratchet-report.schema.json").read_text())
    iteration_schema = json.loads((ROOT / "schemas/iteration-record.schema.json").read_text())
    Draft202012Validator.check_schema(front_schema)
    Draft202012Validator.check_schema(bottom_schema)
    Draft202012Validator.check_schema(ratchet_schema)
    Draft202012Validator.check_schema(iteration_schema)

    valid_examples = [
        ("examples/front-matter.valid.json", front_schema),
        ("examples/bottom-matter.valid.json", bottom_schema),
        ("examples/copilot-ratchet-report.valid.json", ratchet_schema),
        ("examples/iteration-record.valid.json", iteration_schema),
    ]
    for rel, schema in valid_examples:
        instance = json.loads((ROOT / rel).read_text())
        Draft202012Validator(schema).validate(instance)
        results.append({"file": rel, "status": "pass"})

    registry = yaml.safe_load((ROOT / "expected-failures/registry.yaml").read_text())
    for item in registry["invalid_examples"]:
        schema = json.loads((ROOT / item["schema"]).read_text())
        instance = json.loads((ROOT / item["file"]).read_text())
        validator = Draft202012Validator(schema)
        errors = list(validator.iter_errors(instance))
        if not errors:
            raise AssertionError(f"{item['file']} unexpectedly passed")
        message_blob = " | ".join(error.message for error in errors)
        if item["expected_reason_contains"] not in message_blob:
            raise AssertionError(
                f"{item['file']} failed for unexpected reason: {message_blob}"
            )
        results.append({"file": item["file"], "status": "pass", "reason": message_blob})
    return results


def main() -> int:
    checks = []

    scaffold_missing = [name for name in REQUIRED_SCAFFOLD if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_scaffold_files",
            "status": "pass" if not scaffold_missing else "fail",
            "details": {"missing": scaffold_missing},
        }
    )

    prompt_missing = [name for name in REQUIRED_PROMPT_CONTRACT if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_prompt_contract_files",
            "status": "pass" if not prompt_missing else "fail",
            "details": {"missing": prompt_missing},
        }
    )

    dir_missing = [name for name in REQUIRED_DIRECTORIES if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_proof_package_dirs",
            "status": "pass" if not dir_missing else "fail",
            "details": {"missing": dir_missing},
        }
    )

    program_missing = [name for name in REQUIRED_PROGRAM_FILES if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_program_files",
            "status": "pass" if not program_missing else "fail",
            "details": {"missing": program_missing},
        }
    )

    root_missing = [
        name
        for name in ["library.yaml", "infranodus-phase-tool-map.json", "pixeltable-operational-substrate.md"]
        if not (ROOT / name).exists()
    ]
    checks.append(
        {
            "name": "required_root_authorities",
            "status": "pass" if not root_missing else "fail",
            "details": {"missing": root_missing},
        }
    )

    external_missing = []
    for repo, files in REQUIRED_EXTERNAL_REPOS.items():
        for rel in files:
            path = ROOT / "external" / repo / rel
            if not path.exists():
                external_missing.append(str(path.relative_to(ROOT)))
    checks.append(
        {
            "name": "required_local_upstream_clones",
            "status": "pass" if not external_missing else "fail",
            "details": {"missing": external_missing},
        }
    )

    scaffold_results = []
    front_schema = json.loads((ROOT / "schemas/front-matter.schema.json").read_text())
    bottom_schema = json.loads((ROOT / "schemas/bottom-matter.schema.json").read_text())
    front_validator = Draft202012Validator(front_schema)
    bottom_validator = Draft202012Validator(bottom_schema)
    scaffold_ok = True
    for name in REQUIRED_SCAFFOLD:
        front, bottom = parse_markdown_contract(ROOT / name)
        front_validator.validate(front)
        bottom_validator.validate(bottom)
        scaffold_results.append({"file": name, "status": "pass"})
    checks.append(
        {
            "name": "scaffold_markdown_contracts",
            "status": "pass" if scaffold_ok else "fail",
            "details": scaffold_results,
        }
    )

    example_results = validate_examples()
    checks.append(
        {
            "name": "schema_and_example_validation",
            "status": "pass",
            "details": example_results,
        }
    )

    program_results = []
    program_front, program_bottom = parse_markdown_contract(ROOT / "program.md")
    front_validator.validate(program_front)
    bottom_validator.validate(program_bottom)
    program_results.append({"file": "program.md", "status": "pass"})
    checks.append(
        {
            "name": "program_markdown_contract",
            "status": "pass",
            "details": program_results,
        }
    )

    iterations_path = ROOT / "runs/iterations.jsonl"
    iteration_rows, iteration_errors = load_jsonl(iterations_path)
    iteration_schema = json.loads((ROOT / "schemas/iteration-record.schema.json").read_text())
    iteration_validator = Draft202012Validator(iteration_schema)
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
                "path": str(iterations_path.relative_to(ROOT)),
                "row_count": len(iteration_rows),
                "parse_errors": iteration_errors,
                "invalid_rows": invalid_rows,
            },
        }
    )

    ratchet_report_path = ROOT / "evaluation/copilot-ratchet-report.json"
    ratchet_schema = json.loads((ROOT / "schemas/copilot-ratchet-report.schema.json").read_text())
    ratchet_check = {
        "name": "copilot_ratchet_report_contract",
        "status": "pass",
        "details": {"status": "missing"},
    }
    if ratchet_report_path.exists():
        report_instance = json.loads(ratchet_report_path.read_text())
        errors = sorted(Draft202012Validator(ratchet_schema).iter_errors(report_instance), key=lambda error: error.path)
        ratchet_check = {
            "name": "copilot_ratchet_report_contract",
            "status": "pass" if not errors else "fail",
            "details": {
                "path": str(ratchet_report_path.relative_to(ROOT)),
                "errors": [error.message for error in errors],
            },
        }
    checks.append(ratchet_check)

    overall = "pass" if all(item["status"] == "pass" for item in checks) else "fail"
    report = {
        "report_id": "PARENT-META-VALIDATION-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "overall_status": overall,
        "checks": checks,
    }
    (ROOT / "evaluation/validation-report.json").write_text(json.dumps(report, indent=2) + "\n")

    ratchet_blockers = []
    report_path = ROOT / "evaluation/copilot-ratchet-report.json"
    if iteration_errors or invalid_rows:
        ratchet_blockers.append("Iteration ledger does not satisfy the iteration record contract.")
    if not report_path.exists():
        ratchet_blockers.append("Real copilot-ratchet-report.json is missing.")
    else:
        report_instance = json.loads(report_path.read_text())
        schema_errors = list(Draft202012Validator(ratchet_schema).iter_errors(report_instance))
        if schema_errors:
            ratchet_blockers.append("Real copilot-ratchet-report.json does not satisfy the report schema.")
        if int(report_instance.get("real_non_dry_cycles_executed", 0)) < 2:
            ratchet_blockers.append("Real copilot ratchet executed fewer than 2 non-dry cycles.")

    readiness = {
        "readiness_id": "PARENT-META-PROMOTION-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "status": "pass" if overall == "pass" and not ratchet_blockers else "blocked",
        "blockers": ([] if overall == "pass" else ["Parent wrapper contract validation failed."]) + ratchet_blockers,
        "evidence": [
            "evaluation/validation-report.json",
            "evaluation/copilot-ratchet-report.json",
            "infranodus-phase-tool-map.json",
            "library.yaml",
            "agent-heavy-run-prompt.schema.json",
            "program.md",
            "runs/iterations.jsonl",
        ],
    }
    (ROOT / "promotion/readiness.json").write_text(json.dumps(readiness, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if overall == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
