---
name: contract-checker
description: Validate all contracts against schemas and run the parent wrapper validator + scorer. Invoke before capability harvesting to ensure the governance surface is clean. Writes evaluation/contract-check-summary.json and refreshes validation-report.json and metrics-latest.json.
---

# contract-checker

Run all validation checks and produce a clean governance health report.

## Scope

READ: `contracts/`, `schemas/`, `examples/`, `tests/`, `scripts/`
WRITE: `evaluation/validation-report.json`, `evaluation/metrics-latest.json`, `evaluation/contract-check-summary.json`
FORBIDDEN: modifying contracts/, schemas/, or any source file

## Job

1. Run `uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py`
2. Run `uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json`
3. Capture both outputs
4. Check `examples/*.valid.json` — count how many exist vs how many contracts/ YAML files exist
5. Write `evaluation/contract-check-summary.json`

## Output Schema

```json
{
  "schema_version": "1.0.0",
  "executed_at": "<iso>",
  "validator_result": "pass|fail",
  "validator_errors": [],
  "score": 89.06,
  "contract_count": 31,
  "schema_count": 0,
  "valid_example_count": 0,
  "gaps": [
    {
      "contract_id": "<id>",
      "has_schema": true/false,
      "has_valid_example": true/false,
      "has_invalid_example": true/false
    }
  ]
}
```

## Hard Rules

- Run validator with `uv` only — never pip
- Do not modify any contract, schema, or example file
- If validator fails, record exact error and continue — do not abort
- Score must be read from the JSON output of score-parent-wrapper.py
