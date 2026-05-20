# claude-settings.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "claude-settings.schema.json",
  "title": ".claude/settings.json Schema (minimal)",
  "type": "object",
  "additionalProperties": true,
  "required": ["permissions", "hooks", "env"],
  "properties": {
    "permissions": { "type": "object" },
    "hooks": { "type": "object" },
    "env": { "type": "object" }
  }
}
```