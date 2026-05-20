# sources.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "sources.schema.json",
  "title": "sources.md Schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["canonicalDocs", "versionPins", "skillsSupplyChain"],
  "properties": {
    "canonicalDocs": { "type": "array", "items": { "type": "string", "format": "uri" } },
    "versionPins": {
      "type": "object",
      "additionalProperties": true,
      "required": ["claudeCodeVersion", "exportedAt"],
      "properties": {
        "claudeCodeVersion": { "type": "string" },
        "exportedAt": { "type": "string" }
      }
    },
    "skillsSupplyChain": {
      "type": "object",
      "additionalProperties": false,
      "required": ["mustRecord", "requiredFields"],
      "properties": {
        "mustRecord": { "type": "boolean" },
        "requiredFields": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```