# scorecard.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "scorecard.schema.json",
  "title": "scorecard.json Schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["runId", "primaryMetric", "secondaryMetrics"],
  "properties": {
    "runId": { "type": "string" },
    "primaryMetric": { "type": "object" },
    "secondaryMetrics": { "type": "object" },
    "notes": { "type": "array", "items": { "type": "string" } }
  }
}
```