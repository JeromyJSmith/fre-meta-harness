# output-style.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "output-style.schema.json",
  "title": "Output Style Registry Entry Schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["styleId", "format", "consumer", "purpose"],
  "properties": {
    "styleId": { "type": "string", "pattern": "^[a-z0-9:-]+$" },
    "format": { "type": "string", "enum": ["yaml", "json", "markdown", "html"] },
    "consumer": { "type": "string", "enum": ["human", "agent", "tool"] },
    "purpose": { "type": "string" },
    "schemaRef": { "type": "string" },
    "examples": { "type": "array", "items": { "type": "string" } }
  }
}
```