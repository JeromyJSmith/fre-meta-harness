---
name: proof-runner
description: Run all subsystem probes, the parent wrapper validator, the scorer, and refresh tool-health. Invoke after capability-harvester completes. Produces evaluation/proof-run-report.json and updates evaluation/tool-health/status.json.
---

# proof-runner

Run all validation and proof scripts, collect results, and report clean or blocked.

## Scope

READ: `stages/02_research_harvest/output/`, `evaluation/research/compiled/`, `scripts/`, `tests/`
WRITE: `evaluation/proof-run-report.json`, `evaluation/tool-health/status.json` (updates subsystem_probes section)
RUNS: probe scripts via bash, validator via uv

## Job

1. Run intake_etl probe: `bash scripts/run-intake-etl-probe.sh`
2. Run research_harvest probe: `bash scripts/run-research-harvest-probe.sh`
3. Run semantic_cartography probe: `bash scripts/run-semantic-cartography-probe.sh`
4. Run validator: `uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py`
5. Run scorer: `uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json`
6. Refresh tool health: `uv run python scripts/refresh-parent-tool-health.py`
7. Write `evaluation/proof-run-report.json`

## Output Schema

```json
{
  "schema_version": "1.0.0",
  "executed_at": "<iso>",
  "probes": {
    "intake_etl": {"proof_state": "bounded_probe_pass", "blockers": []},
    "research_harvest": {"proof_state": "bounded_probe_pass", "blockers": []},
    "semantic_cartography": {"proof_state": "bounded_probe_pass", "blockers": []}
  },
  "validator_result": "pass|fail",
  "score": 89.06,
  "all_probes_pass": true,
  "blockers": []
}
```

## Hard Rules

- Run ALL probes even if one fails — collect all results before writing
- Do not modify probe scripts or validator
- Use `uv run` only — never bare `python` for scripts that need packages
- If any probe is `bounded_probe_blocked`, record exact blocker in output
