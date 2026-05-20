# project.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "project.schema.json",
  "title": "Portable Harness Project (root) Schema",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schemaVersion",
    "projectId",
    "entrypoints",
    "paths",
    "artifacts"
  ],
  "properties": {
    "schemaVersion": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "projectId": { "type": "string", "pattern": "^[a-z0-9-]+$" },
    "name": { "type": "string" },
    "entrypoints": {
      "type": "object",
      "additionalProperties": false,
      "required": ["bootstrap", "claude"],
      "properties": {
        "bootstrap": { "type": "string" },
        "claude": { "type": "string" }
      }
    },
    "paths": {
      "type": "object",
      "additionalProperties": false,
      "required": ["docsHarness", "dotClaude", "schemas", "examples", "reports", "compiler", "runs"],
      "properties": {
        "docsHarness": { "type": "string" },
        "dotClaude": { "type": "string" },
        "schemas": { "type": "string" },
        "examples": { "type": "string" },
        "reports": { "type": "string" },
        "compiler": { "type": "string" },
        "runs": { "type": "string" }
      }
    },
    "artifacts": {
      "type": "array",
      "items": { "$ref": "artifact.schema.json" }
    }
  }
}
```

<aside>
📎

**Purpose**: Defines the machine-validated contract for the portable harness project “root descriptor” shape (entrypoints, paths, artifact list).

**Inputs**: Project metadata + artifact registry expectations; `artifact.schema.json` reference.

**Outputs**: A schema for validating project root descriptors consistently across exports/runs.

**Validation tie-in**: Contract validation (project structure), Drift detection (schema version changes).

**Failure modes**: Without this, project structure can fragment and replayability breaks.

**Update / upstream path**: Any change must bump schemaVersion policy (if applicable) and update examples + run logs.

</aside>

```yaml
page_contract:
  purpose: "Schema for portable harness project root descriptor."
  inputs: ["Artifact expectations", "artifact.schema.json"]
  outputs: ["JSON Schema used to validate project root descriptors"]
  validation_tie_in:
    gates: ["Contract validation", "Drift detection"]
    checks:
      - "Schema parses and refs resolve"
  failure_modes:
    - "Project structure drift"
    - "Broken artifact references"
  upstream:
    update_artifact: "Project schema update artifact"
    proposal_path: "Patch schema+example + rerun validate + record drift"
```