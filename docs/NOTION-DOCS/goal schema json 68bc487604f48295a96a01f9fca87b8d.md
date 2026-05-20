# goal.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "goal.schema.json",
  "title": "goal.md Schema (semantic contract)",
  "type": "object",
  "additionalProperties": false,
  "required": ["primaryMetric", "secondaryMetrics", "keepRevertRule", "acceptanceCriteria"],
  "properties": {
    "primaryMetric": { "type": "string" },
    "secondaryMetrics": { "type": "array", "items": { "type": "string" } },
    "keepRevertRule": { "type": "string" },
    "acceptanceCriteria": { "type": "array", "items": { "type": "string" } }
  }
}
```