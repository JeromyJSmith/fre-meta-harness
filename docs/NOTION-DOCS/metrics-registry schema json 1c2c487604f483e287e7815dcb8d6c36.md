# metrics-registry.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "metrics-registry.schema.json",
  "title": "Meta-Harness Metrics Registry Row",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "metric_id",
    "metric_group",
    "metric_name",
    "description",
    "architecture_layer",
    "target_component",
    "measurement_strategy",
    "unit",
    "target_operator",
    "target_value",
    "target_text",
    "status",
    "priority",
    "owner",
    "measurement_cadence",
    "data_source",
    "breach_action"
  ],
  "properties": {
    "metric_id": {"type": "string"},
    "metric_group": {
      "type": "string",
      "enum": [
        "Retrieval",
        "Generation",
        "Agent Behavior",
        "Operations",
        "Harness Health",
        "Governance Gate"
      ]
    },
    "metric_name": {"type": "string"},
    "description": {"type": "string"},
    "architecture_layer": {
      "type": "string",
      "enum": ["source", "execution", "governance", "evaluation", "reflection", "document"]
    },
    "target_component": {"type": "string"},
    "measurement_strategy": {"type": "string"},
    "unit": {"type": "string"},
    "baseline_value": {"type": ["string", "null"]},
    "current_value": {"type": ["string", "null"]},
    "target_operator": {"type": "string", "enum": [">", "<", ">=", "<="]},
    "target_value": {"type": "string"},
    "target_text": {"type": "string"},
    "status": {"type": "string"},
    "priority": {"type": "string", "enum": ["P0", "P1", "P2"]},
    "owner": {"type": "string"},
    "measurement_cadence": {"type": "string"},
    "data_source": {"type": "string"},
    "related_spec": {"type": ["string", "null"]},
    "related_test_or_evaluator": {"type": ["string", "null"]},
    "evidence_path_or_url": {"type": ["string", "null"]},
    "last_measured_at": {"type": ["string", "null"]},
    "next_review_at": {"type": ["string", "null"]},
    "trend": {"type": ["string", "null"]},
    "breach_action": {"type": "string"},
    "source_reference": {"type": ["string", "null"]},
    "notes": {"type": ["string", "null"]}
  }
}
```