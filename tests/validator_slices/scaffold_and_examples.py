from __future__ import annotations

import json


def build_scaffold_and_example_checks(core, front_validator, bottom_validator) -> list[dict]:
    checks: list[dict] = []

    scaffold_missing = [name for name in core.REQUIRED_SCAFFOLD if not (core.ROOT / name).exists()]
    checks.append(
        {
            "name": "required_scaffold_files",
            "status": "pass" if not scaffold_missing else "fail",
            "details": {"missing": scaffold_missing},
        }
    )

    prompt_missing = [name for name in core.REQUIRED_PROMPT_CONTRACT if not (core.ROOT / name).exists()]
    checks.append(
        {
            "name": "required_prompt_contract_files",
            "status": "pass" if not prompt_missing else "fail",
            "details": {"missing": prompt_missing},
        }
    )

    dir_missing = [name for name in core.REQUIRED_DIRECTORIES if not (core.ROOT / name).exists()]
    checks.append(
        {
            "name": "required_proof_package_dirs",
            "status": "pass" if not dir_missing else "fail",
            "details": {"missing": dir_missing},
        }
    )

    program_missing = [name for name in core.REQUIRED_PROGRAM_FILES if not (core.ROOT / name).exists()]
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
        if not (core.ROOT / name).exists()
    ]
    checks.append(
        {
            "name": "required_root_authorities",
            "status": "pass" if not root_missing else "fail",
            "details": {"missing": root_missing},
        }
    )

    external_missing = []
    for repo, files in core.REQUIRED_EXTERNAL_REPOS.items():
        for rel in files:
            path = core.ROOT / "external" / repo / rel
            if not path.exists():
                external_missing.append(str(path.relative_to(core.ROOT)))
    checks.append(
        {
            "name": "required_local_upstream_clones",
            "status": "pass" if not external_missing else "fail",
            "details": {"missing": external_missing},
        }
    )

    scaffold_results = []
    for name in core.REQUIRED_SCAFFOLD:
        front, bottom = core.parse_markdown_contract(core.ROOT / name)
        front_validator.validate(front)
        bottom_validator.validate(bottom)
        scaffold_results.append({"file": name, "status": "pass"})
    checks.append(
        {
            "name": "scaffold_markdown_contracts",
            "status": "pass",
            "details": scaffold_results,
        }
    )

    checks.append(
        {
            "name": "schema_and_example_validation",
            "status": "pass",
            "details": core.validate_examples(),
        }
    )

    program_front, program_bottom = core.parse_markdown_contract(core.ROOT / "program.md")
    front_validator.validate(program_front)
    bottom_validator.validate(program_bottom)
    checks.append(
        {
            "name": "program_markdown_contract",
            "status": "pass",
            "details": [{"file": "program.md", "status": "pass"}],
        }
    )

    return checks
