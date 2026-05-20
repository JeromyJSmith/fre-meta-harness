# bootstrap.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "bootstrap.schema.json",
  "title": "BOOTSTRAP.md Schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["navigationOrder", "fractalRule", "upstreamingRule", "bootSequence", "acceptanceCriteria"],
  "properties": {
    "navigationOrder": { "type": "array", "items": { "type": "string" }, "minItems": 5 },
    "fractalRule": { "type": "string" },
    "upstreamingRule": { "type": "array", "items": { "type": "string" }, "minItems": 3 },
    "bootSequence": { "type": "array", "items": { "type": "string" }, "minItems": 3 },
    "acceptanceCriteria": { "type": "array", "items": { "type": "string" }, "minItems": 2 }
  }
}
```