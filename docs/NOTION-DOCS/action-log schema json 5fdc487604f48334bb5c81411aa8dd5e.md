# action-log.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "action-log.schema.json",
  "title": "actions.jsonl Record Schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["ts", "runId", "actionType"],
  "properties": {
    "ts": { "type": "string" },
    "runId": { "type": "string" },
    "actionType": { "type": "string", "enum": ["prompt", "tool_call", "file_edit", "decision", "hook"] },
    "inputs": { "type": "object" },
    "outputs": { "type": "object" },
    "hashes": { "type": "object" },
    "claudeCodeVersion": { "type": "string" }
  }
}
```

<aside>
📎

**Purpose**: Machine schema for each line-record in the append-only action log (`actions.jsonl`).

**Inputs**: Hook/tool logging requirements; run IDs; action types.

**Outputs**: A schema validators can use to lint action-log records for required fields.

**Validation tie-in**: Observability checks (logging completeness), Replay tests (reconstructability).

**Failure modes**: Missing required fields makes runs unauditable and breaks replay/debugging.

**Update / upstream path**: If logging fields change, update schema + example + any hook docs that emit the records.

</aside>

```yaml
page_contract:
  purpose: "Schema for action-log JSONL records."
  inputs: ["Logging contract", "Hook outputs", "Run IDs"]
  outputs: ["JSON Schema used to validate action log records"]
  validation_tie_in:
    gates: ["Observability checks", "Replay tests"]
    checks:
      - "Records contain ts/runId/actionType"
  failure_modes:
    - "Untraceable actions"
    - "Unreplayable runs"
  upstream:
    update_artifact: "Action-log schema update artifact"
    proposal_path: "Patch schema+example + rerun validate"
```