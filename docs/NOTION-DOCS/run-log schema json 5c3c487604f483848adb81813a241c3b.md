# run-log.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "run-log.schema.json",
  "title": "runs/000X.md Schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["runId", "timestamp", "planRef", "artifacts", "scoreRef", "decision"],
  "properties": {
    "runId": { "type": "string", "pattern": "^\\d{4}$" },
    "timestamp": { "type": "string" },
    "planRef": { "type": "string" },
    "artifacts": { "type": "array", "items": { "type": "string" } },
    "scoreRef": { "type": "string" },
    "decision": { "type": "string", "enum": ["keep", "revert", "investigate"] }
  }
}
```

<aside>
📎

**Purpose**: Machine contract for the run log metadata fields (run id, plan ref, artifacts, score ref, decision).

**Inputs**: Run logging conventions in `runs/README.md` and evaluation/decision workflow.

**Outputs**: A schema for validating that every run is auditable and link-complete.

**Validation tie-in**: Replay tests (evidence completeness), Publish decision (keep/revert requires evidence).

**Failure modes**: Missing plan/artifact/score links makes decisions unverifiable.

**Update / upstream path**: If run format evolves, update this schema + matching examples and preserve backward compatibility where possible.

</aside>

```yaml
page_contract:
  purpose: "Schema for run log metadata."
  inputs: ["Run conventions", "Plan + scorecard/report pointers"]
  outputs: ["JSON Schema used to validate run logs"]
  validation_tie_in:
    gates: ["Replay tests", "Publish decision"]
    checks:
      - "Run log contains required pointers"
  failure_modes:
    - "Unverifiable keep/revert decisions"
    - "Broken replay chain"
  upstream:
    update_artifact: "Run-log schema update artifact"
    proposal_path: "Patch schema+example + rerun validate"
```