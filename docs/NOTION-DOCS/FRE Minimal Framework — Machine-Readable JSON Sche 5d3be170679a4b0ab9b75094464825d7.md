# FRE Minimal Framework — Machine-Readable JSON Schema

<aside>
🧾

**Purpose**: This page contains the complete machine-readable JSON Schema for the smallest FRE framework loop. It can be saved as `schemas/fre-loop.schema.json`.

</aside>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fre.local/schemas/fre-loop.schema.json",
  "title": "FRE Minimal Loop Schema",
  "description": "Machine-readable validating schema for the smallest complete Fractal Research Engineering loop: one governed artifact, validation gates, evidence, promotion decision, and repair tasks.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "fre_version",
    "loop_id",
    "name",
    "purpose",
    "scale",
    "status",
    "authority_chain",
    "stages",
    "gates",
    "artifacts",
    "run",
    "validation_pass_criteria"
  ],
  "properties": {
    "fre_version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$",
      "description": "Semantic version of the FRE framework contract."
    },
    "loop_id": {
      "type": "string",
      "pattern": "^FRE-LOOP-[0-9]{4,}$",
      "description": "Stable identifier for this loop definition."
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "purpose": {
      "type": "string",
      "minLength": 1
    },
    "scale": {
      "type": "string",
      "enum": [
        "artifact",
        "task",
        "feature",
        "project",
        "program",
        "workspace"
      ]
    },
    "status": {
      "type": "string",
      "enum": [
        "draft",
        "active",
        "validated",
        "canonical",
        "superseded",
        "archived"
      ]
    },
    "authority_chain": {
      "type": "array",
      "minItems": 9,
      "items": {
        "type": "string",
        "enum": [
          "sources",
          "research",
          "spec",
          "tasks",
          "build",
          "tests",
          "evaluation",
          "promotion_decision",
          "repair"
        ]
      },
      "contains": {
        "const": "promotion_decision"
      }
    },
    "stages": {
      "type": "array",
      "minItems": 10,
      "items": {
        "$ref": "#/$defs/stage"
      }
    },
    "gates": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/gate"
      }
    },
    "artifacts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/artifact"
      }
    },
    "schemas": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/schema_record"
      },
      "default": []
    },
    "examples": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/example_record"
      },
      "default": []
    },
    "sources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/source_record"
      },
      "default": []
    },
    "run": {
      "$ref": "#/$defs/run"
    },
    "validation_pass_criteria": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "enum": [
          "all_blocking_gates_pass",
          "gate_results_written",
          "report_written",
          "promotion_decision_written",
          "repair_tasks_written_if_failed",
          "no_silent_blocking_failures"
        ]
      }
    }
  },
  "$defs": {
    "stage": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "purpose",
        "order",
        "required_inputs",
        "required_outputs",
        "failure_modes"
      ],
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^STAGE-[A-Z0-9-]+$"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "purpose": {
          "type": "string",
          "minLength": 1
        },
        "order": {
          "type": "integer",
          "minimum": 1
        },
        "required_inputs": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "default": []
        },
        "required_outputs": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "default": []
        },
        "failure_modes": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "default": []
        }
      }
    },
    "gate": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "blocking",
        "checks",
        "failure_classes"
      ],
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^GATE-[A-Z0-9-]+$"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "blocking": {
          "type": "boolean"
        },
        "checks": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "failure_classes": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "pattern": "^[A-Z0-9_]+$"
          }
        }
      }
    },
    "artifact": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "artifact_id",
        "title",
        "artifact_type",
        "path",
        "status",
        "owner"
      ],
      "properties": {
        "artifact_id": {
          "type": "string",
          "pattern": "^[A-Z]+-[A-Z]+-[0-9]{4,}$"
        },
        "title": {
          "type": "string",
          "minLength": 1
        },
        "artifact_type": {
          "type": "string",
          "enum": [
            "spec",
            "schema",
            "example",
            "test",
            "source_map",
            "report",
            "run_log",
            "promotion_decision",
            "repair_task",
            "golden_path",
            "diagram",
            "policy",
            "implementation"
          ]
        },
        "path": {
          "type": "string",
          "minLength": 1
        },
        "status": {
          "type": "string",
          "enum": [
            "draft",
            "active",
            "validated",
            "canonical",
            "needs_repair",
            "superseded",
            "archived"
          ]
        },
        "owner": {
          "type": "string",
          "minLength": 1
        },
        "sources": {
          "type": "array",
          "items": {
            "type": "string",
            "pattern": "^SRC-[A-Z0-9-]+$"
          },
          "default": []
        },
        "related_schemas": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "default": []
        },
        "related_examples": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "default": []
        },
        "related_tests": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "default": []
        },
        "promotion_readiness": {
          "type": "string",
          "enum": [
            "blocked",
            "needs_trace",
            "needs_test",
            "needs_docs_parity",
            "needs_validation",
            "ready_for_review",
            "ready_to_promote",
            "canonical"
          ],
          "default": "needs_validation"
        }
      }
    },
    "source_record": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "source_id",
        "title",
        "type",
        "accessed_at",
        "confidence"
      ],
      "properties": {
        "source_id": {
          "type": "string",
          "pattern": "^SRC-[A-Z0-9-]+$"
        },
        "title": {
          "type": "string",
          "minLength": 1
        },
        "type": {
          "type": "string",
          "enum": [
            "notion_page",
            "web_page",
            "repo_file",
            "book",
            "paper",
            "meeting_note",
            "human_decision",
            "local_file",
            "other"
          ]
        },
        "url": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "accessed_at": {
          "type": "string",
          "format": "date"
        },
        "confidence": {
          "type": "string",
          "enum": [
            "low",
            "medium",
            "high"
          ]
        },
        "notes": {
          "type": "string",
          "default": ""
        }
      },
      "anyOf": [
        {
          "required": [
            "url"
          ]
        },
        {
          "required": [
            "path"
          ]
        }
      ]
    },
    "schema_record": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "schema_id",
        "path",
        "validates_artifact_types"
      ],
      "properties": {
        "schema_id": {
          "type": "string",
          "pattern": "^SCHEMA-[A-Z0-9-]+$"
        },
        "path": {
          "type": "string",
          "minLength": 1
        },
        "validates_artifact_types": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string"
          }
        },
        "required_examples": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "default": []
        }
      }
    },
    "example_record": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "example_id",
        "path",
        "schema_id",
        "expected_valid"
      ],
      "properties": {
        "example_id": {
          "type": "string",
          "pattern": "^EXAMPLE-[A-Z0-9-]+$"
        },
        "path": {
          "type": "string",
          "minLength": 1
        },
        "schema_id": {
          "type": "string",
          "pattern": "^SCHEMA-[A-Z0-9-]+$"
        },
        "expected_valid": {
          "type": "boolean"
        }
      }
    },
    "run": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "run_id",
        "loop_id",
        "target_artifact",
        "started_at",
        "actor",
        "status",
        "gate_results"
      ],
      "properties": {
        "run_id": {
          "type": "string",
          "pattern": "^RUN-[0-9]{4,}$"
        },
        "loop_id": {
          "type": "string",
          "pattern": "^FRE-LOOP-[0-9]{4,}$"
        },
        "target_artifact": {
          "type": "string",
          "pattern": "^[A-Z]+-[A-Z]+-[0-9]{4,}$"
        },
        "started_at": {
          "type": "string",
          "format": "date-time"
        },
        "completed_at": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time"
        },
        "actor": {
          "type": "string",
          "minLength": 1
        },
        "status": {
          "type": "string",
          "enum": [
            "not_started",
            "in_progress",
            "passed",
            "failed",
            "repaired",
            "promoted"
          ]
        },
        "gate_results": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/gate_result"
          },
          "default": []
        },
        "reports": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "default": []
        },
        "repair_tasks": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/repair_task"
          },
          "default": []
        },
        "promotion_decision": {
          "anyOf": [
            {
              "$ref": "#/$defs/promotion_decision"
            },
            {
              "type": "null"
            }
          ],
          "default": null
        }
      }
    },
    "gate_result": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "gate_id",
        "artifact_id",
        "status",
        "blocking",
        "severity",
        "message",
        "repair_required"
      ],
      "properties": {
        "gate_id": {
          "type": "string",
          "pattern": "^GATE-[A-Z0-9-]+$"
        },
        "artifact_id": {
          "type": "string",
          "pattern": "^[A-Z]+-[A-Z]+-[0-9]{4,}$"
        },
        "status": {
          "type": "string",
          "enum": [
            "pass",
            "fail",
            "warning",
            "skipped"
          ]
        },
        "blocking": {
          "type": "boolean"
        },
        "severity": {
          "type": "string",
          "enum": [
            "info",
            "warning",
            "error",
            "critical"
          ]
        },
        "message": {
          "type": "string",
          "minLength": 1
        },
        "failure_class": {
          "type": [
            "string",
            "null"
          ],
          "pattern": "^[A-Z0-9_]+$"
        },
        "evidence": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "path": {
              "type": "string"
            },
            "line": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 1
            },
            "details": {
              "type": "string"
            }
          },
          "default": {}
        },
        "repair_required": {
          "type": "boolean"
        }
      }
    },
    "promotion_decision": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "decision_id",
        "run_id",
        "artifact_id",
        "decision",
        "reason",
        "evidence",
        "next_action",
        "decided_at",
        "decider"
      ],
      "properties": {
        "decision_id": {
          "type": "string",
          "pattern": "^DECISION-[0-9]{4,}$"
        },
        "run_id": {
          "type": "string",
          "pattern": "^RUN-[0-9]{4,}$"
        },
        "artifact_id": {
          "type": "string",
          "pattern": "^[A-Z]+-[A-Z]+-[0-9]{4,}$"
        },
        "decision": {
          "type": "string",
          "enum": [
            "keep",
            "repair",
            "reject"
          ]
        },
        "reason": {
          "type": "string",
          "minLength": 1
        },
        "evidence": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string"
          }
        },
        "next_action": {
          "type": "string",
          "minLength": 1
        },
        "decided_at": {
          "type": "string",
          "format": "date-time"
        },
        "decider": {
          "type": "string",
          "minLength": 1
        }
      }
    },
    "repair_task": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "repair_id",
        "run_id",
        "artifact_id",
        "from_gate",
        "failure_class",
        "blocking",
        "owner",
        "recommended_action",
        "acceptance_criteria",
        "status"
      ],
      "properties": {
        "repair_id": {
          "type": "string",
          "pattern": "^REPAIR-[0-9]{4,}$"
        },
        "run_id": {
          "type": "string",
          "pattern": "^RUN-[0-9]{4,}$"
        },
        "artifact_id": {
          "type": "string",
          "pattern": "^[A-Z]+-[A-Z]+-[0-9]{4,}$"
        },
        "from_gate": {
          "type": "string",
          "pattern": "^GATE-[A-Z0-9-]+$"
        },
        "failure_class": {
          "type": "string",
          "pattern": "^[A-Z0-9_]+$"
        },
        "blocking": {
          "type": "boolean"
        },
        "owner": {
          "type": "string",
          "minLength": 1
        },
        "recommended_action": {
          "type": "string",
          "minLength": 1
        },
        "acceptance_criteria": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "status": {
          "type": "string",
          "enum": [
            "open",
            "in_progress",
            "done",
            "wont_do"
          ]
        }
      }
    }
  }
}
```

## Prompt contract schema extension

The FRE machine-readable layer also governs **agent prompt contracts**. Prompt schemas belong to the same authority stack because they control bounded execution, validation behavior, and promotion integrity.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fre.local/schemas/agent-heavy-run-prompt.schema.json",
  "title": "FRE Agent Heavy Run Prompt Contract",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "mode",
    "mission",
    "current_verified_state",
    "hard_rules",
    "tasks",
    "validation_loop",
    "success_criteria",
    "report_contract"
  ],
  "properties": {
    "schema_version": {"type": "string"},
    "mode": {
      "type": "string",
      "enum": ["heavy_run", "bounded_run", "review_run", "research_run"]
    },
    "mission": {"type": "string", "minLength": 1},
    "current_verified_state": {
      "type": "array",
      "items": {"type": "string", "minLength": 1},
      "minItems": 1
    },
    "hard_rules": {
      "type": "array",
      "items": {"type": "string", "minLength": 1},
      "minItems": 1
    },
    "allowed_paths": {
      "type": "array",
      "items": {"type": "string"},
      "default": []
    },
    "disallowed_paths": {
      "type": "array",
      "items": {"type": "string"},
      "default": []
    },
    "tasks": {
      "type": "array",
      "items": {"type": "string", "minLength": 1},
      "minItems": 1
    },
    "validation_loop": {
      "type": "array",
      "items": {"type": "string", "minLength": 1},
      "minItems": 1
    },
    "success_criteria": {
      "type": "object",
      "additionalProperties": false,
      "required": ["best_case", "acceptable_fallback"],
      "properties": {
        "best_case": {"type": "string", "minLength": 1},
        "acceptable_fallback": {"type": "string", "minLength": 1}
      }
    },
    "report_contract": {
      "type": "array",
      "items": {"type": "string", "minLength": 1},
      "minItems": 1
    },
    "environment_policy": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "python_runtime": {"type": "string", "enum": ["uv_first"]},
        "forbid_pip_default": {"type": "boolean"},
        "forbid_venv_default": {"type": "boolean"},
        "forbid_paid_api_key_default": {"type": "boolean"}
      },
      "default": {
        "python_runtime": "uv_first",
        "forbid_pip_default": true,
        "forbid_venv_default": true,
        "forbid_paid_api_key_default": true
      }
    }
  }
}
```

### Prompt contract notes

- Prompt contracts are governed execution artifacts, not operator-only prose.
- Heavy-run prompts should prefer full bounded completion in one pass when the task boundary is clear.
- Python execution policy should default to `uv`.
- Paid-model API keys should not be introduced as the default runtime path when subscribed execution surfaces exist.

### Repo-local canonical artifacts

This schema extension maps to the repo-local governed files:

- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt-index.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt-schema.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt.schema.json`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt.template.yaml`

Use the index file as the single repo-local entrypoint. These files are the executable schema/template source of truth for Meta-Harness implementation work.

## Minimal valid instance

```json
{
  "fre_version": "0.1.0",
  "loop_id": "FRE-LOOP-0001",
  "name": "Minimal FRE Kernel Loop",
  "purpose": "Validate one governed artifact and produce a promotion or repair decision.",
  "scale": "artifact",
  "status": "draft",
  "authority_chain": [
    "sources",
    "research",
    "spec",
    "tasks",
    "build",
    "tests",
    "evaluation",
    "promotion_decision",
    "repair"
  ],
  "stages": [
    {
      "id": "STAGE-ONBOARD",
      "name": "Onboard",
      "purpose": "Capture intent.",
      "order": 1,
      "required_inputs": [
        "purpose"
      ],
      "required_outputs": [
        "onboarding_record"
      ],
      "failure_modes": [
        "unclear_goal"
      ]
    },
    {
      "id": "STAGE-BRAINSTORM",
      "name": "Brainstorm",
      "purpose": "Generate and select candidate direction.",
      "order": 2,
      "required_inputs": [
        "onboarding_record"
      ],
      "required_outputs": [
        "selected_direction"
      ],
      "failure_modes": [
        "premature_convergence"
      ]
    },
    {
      "id": "STAGE-RESEARCH",
      "name": "Research",
      "purpose": "Collect source-backed information.",
      "order": 3,
      "required_inputs": [
        "selected_direction"
      ],
      "required_outputs": [
        "source_records"
      ],
      "failure_modes": [
        "unsourced_claims"
      ]
    },
    {
      "id": "STAGE-SPEC",
      "name": "Specify",
      "purpose": "Create governing spec.",
      "order": 4,
      "required_inputs": [
        "source_records"
      ],
      "required_outputs": [
        "governing_spec"
      ],
      "failure_modes": [
        "spec_ambiguity"
      ]
    },
    {
      "id": "STAGE-TASKS",
      "name": "Plan Tasks",
      "purpose": "Create measurable tasks.",
      "order": 5,
      "required_inputs": [
        "governing_spec"
      ],
      "required_outputs": [
        "task_graph"
      ],
      "failure_modes": [
        "tasks_not_testable"
      ]
    },
    {
      "id": "STAGE-BUILD",
      "name": "Build",
      "purpose": "Implement bounded task.",
      "order": 6,
      "required_inputs": [
        "task_graph"
      ],
      "required_outputs": [
        "changed_artifacts"
      ],
      "failure_modes": [
        "scope_creep"
      ]
    },
    {
      "id": "STAGE-TEST",
      "name": "Test",
      "purpose": "Run checks.",
      "order": 7,
      "required_inputs": [
        "changed_artifacts"
      ],
      "required_outputs": [
        "test_results"
      ],
      "failure_modes": [
        "test_failure"
      ]
    },
    {
      "id": "STAGE-EVALUATE",
      "name": "Evaluate",
      "purpose": "Score against gates.",
      "order": 8,
      "required_inputs": [
        "test_results"
      ],
      "required_outputs": [
        "gate_results"
      ],
      "failure_modes": [
        "ambiguous_result"
      ]
    },
    {
      "id": "STAGE-DECIDE",
      "name": "Decide",
      "purpose": "Choose keep, repair, or reject.",
      "order": 9,
      "required_inputs": [
        "gate_results"
      ],
      "required_outputs": [
        "promotion_decision"
      ],
      "failure_modes": [
        "missing_decision"
      ]
    },
    {
      "id": "STAGE-REPAIR",
      "name": "Repair or Promote",
      "purpose": "Repair failures or promote success.",
      "order": 10,
      "required_inputs": [
        "promotion_decision"
      ],
      "required_outputs": [
        "repair_tasks_or_promotion_record"
      ],
      "failure_modes": [
        "silent_failure"
      ]
    }
  ],
  "gates": [
    {
      "id": "GATE-ENVELOPE",
      "name": "Envelope Gate",
      "blocking": true,
      "checks": [
        "front_matter_present",
        "bottom_matter_present"
      ],
      "failure_classes": [
        "ENVELOPE_FRONTMATTER_MISSING",
        "ENVELOPE_BOTTOM_MATTER_MISSING"
      ]
    },
    {
      "id": "GATE-SOURCE",
      "name": "Source Gate",
      "blocking": true,
      "checks": [
        "source_records_exist"
      ],
      "failure_classes": [
        "SOURCE_RECORD_NOT_FOUND"
      ]
    },
    {
      "id": "GATE-PROMOTION",
      "name": "Promotion Decision Gate",
      "blocking": true,
      "checks": [
        "decision_exists"
      ],
      "failure_classes": [
        "PROMOTION_DECISION_MISSING"
      ]
    }
  ],
  "artifacts": [
    {
      "artifact_id": "SPEC-FRE-0001",
      "title": "FRE Method",
      "artifact_type": "spec",
      "path": "docs/specs/fre-method.md",
      "status": "draft",
      "owner": "planning-agent",
      "sources": [
        "SRC-FRE-0001"
      ],
      "related_schemas": [
        "schemas/governed-document.schema.json"
      ],
      "related_examples": [
        "examples/governed-document.valid.md"
      ],
      "related_tests": [
        "tests/test_envelope.py"
      ],
      "promotion_readiness": "needs_validation"
    }
  ],
  "sources": [
    {
      "source_id": "SRC-FRE-0001",
      "title": "FRE Method Source",
      "type": "notion_page",
      "url": "https://www.notion.so/301c487604f4820b83e601f9ddcf6771",
      "accessed_at": "2026-05-16",
      "confidence": "high",
      "notes": "Canonical FRE method page."
    }
  ],
  "run": {
    "run_id": "RUN-0001",
    "loop_id": "FRE-LOOP-0001",
    "target_artifact": "SPEC-FRE-0001",
    "started_at": "2026-05-16T00:00:00Z",
    "completed_at": null,
    "actor": "fre-kernel",
    "status": "in_progress",
    "gate_results": [],
    "reports": [],
    "repair_tasks": [],
    "promotion_decision": null
  },
  "validation_pass_criteria": [
    "all_blocking_gates_pass",
    "gate_results_written",
    "report_written",
    "promotion_decision_written",
    "repair_tasks_written_if_failed",
    "no_silent_blocking_failures"
  ]
}
```

[fre-test-eval-improvement](fre-test-eval-improvement%2076019c48ec2441c0a42a1ac7a3f9b49b.md)