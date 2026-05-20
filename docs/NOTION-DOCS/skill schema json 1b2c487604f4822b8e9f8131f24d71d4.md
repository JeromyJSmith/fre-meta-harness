# skill.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "skill.schema.json",
  "title": "SKILL.md Frontmatter + Body Schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["frontmatter", "body"],
  "properties": {
    "frontmatter": {
      "type": "object",
      "additionalProperties": true,
      "required": ["description"],
      "properties": {
        "description": { "type": "string" }
      }
    },
    "body": {
      "type": "object",
      "additionalProperties": true,
      "required": ["mission", "inputsRequired", "outputs", "procedure", "completionCriteria"],
      "properties": {
        "mission": { "type": "string" },
        "inputsRequired": { "type": "array", "items": { "type": "string" } },
        "outputs": { "type": "array", "items": { "type": "string" } },
        "procedure": { "type": "array", "items": { "type": "string" } },
        "completionCriteria": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```