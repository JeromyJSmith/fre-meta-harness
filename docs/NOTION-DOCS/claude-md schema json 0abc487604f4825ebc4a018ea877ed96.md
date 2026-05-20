# claude-md.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "claude-md.schema.json",
  "title": "CLAUDE.md Schema (structure contract)",
  "type": "object",
  "additionalProperties": false,
  "required": ["requiredHeadings", "requiredLinks"],
  "properties": {
    "requiredHeadings": {
      "type": "array",
      "items": { "type": "string" },
      "default": [
        "Start here",
        "Hard rules",
        "How to validate"
      ]
    },
    "requiredLinks": {
      "type": "array",
      "items": { "type": "string" },
      "default": [
        "docs/harness/goal.md",
        "docs/harness/golden-path.md",
        "docs/harness/memory.md",
        "docs/harness/sources.md"
      ]
    },
    "rules": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

<aside>
📎

**Purpose**: Machine contract for `CLAUDE.md` structure (required headings + required links).

**Inputs**: `CLAUDE.md` content; nucleus docs paths (`docs/harness/*`).

**Outputs**: A schema validators can use to lint `CLAUDE.md` for completeness.

**Validation tie-in**: Contract validation (entrypoint completeness), Static checks (schema parse).

**Failure modes**: If this schema is missing or stale, `CLAUDE.md` can drift silently and the boot order breaks.

**Update / upstream path**: Any change to `CLAUDE.md` required structure must update this schema + add/adjust a matching example in `examples/`.

</aside>

```yaml
page_contract:
  purpose: "Schema for CLAUDE.md structure contract."
  inputs:
    - "CLAUDE.md"
    - "docs/harness/* paths"
  outputs:
    - "JSON Schema used to lint CLAUDE.md"
  validation_tie_in:
    gates: ["Contract validation", "Static checks"]
    checks:
      - "Schema parses"
      - "CLAUDE.md satisfies required headings/links"
  failure_modes:
    - "Entrypoint drift goes undetected"
    - "Broken navigation pointers"
  upstream:
    update_artifact: "Entrypoint schema update artifact"
    proposal_path: "Patch schema+example + rerun fresh-export validation"
```