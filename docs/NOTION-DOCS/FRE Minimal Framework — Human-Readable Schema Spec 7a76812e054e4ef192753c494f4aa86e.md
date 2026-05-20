# FRE Minimal Framework — Human-Readable Schema Spec

<aside>
🧬

**Purpose**: This is the smallest human-readable FRE schema specification. It defines the full Fractal Research Engineering loop as a validating contract that humans can read, discuss, and implement.

</aside>

## FRE Minimal Loop

```
FRE = Fractal Research Engineering.

The smallest FRE loop is:

Onboard → Brainstorm → Research → Specify → Plan Tasks → Build → Test → Evaluate → Decide → Repair or Promote.

The loop is fractal: the same contract applies to a whole project, a sprint, a single feature, a single artifact, or a single repair task.

The method is considered real only when it can validate one governed artifact, produce evidence, and record a promotion or repair decision.
```

## 1. Canonical loop object

```json
{
  "_doc": "The top-level FRE loop contract. This object defines the smallest complete FRE run.",
  "fre_version": "0.1.0",
  "loop_id": "FRE-LOOP-0001",
  "name": "Minimal FRE Loop",
  "purpose": "Validate one governed artifact through the complete FRE loop.",
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
  "stages": [],
  "gates": [],
  "artifacts": [],
  "run": {},
  "decision": {}
}
```

```
Required principle:

The model is never the authority.
The authority chain is always:

sources → research → spec → tasks → build → tests → evaluation → promotion decision → repair or promote.
```

---

## 2. Stage definitions

```json
{
  "_doc": "Each FRE loop is made of ordered stages. Every stage has inputs, outputs, validation, and failure modes.",
  "stages": [
    {
      "id": "STAGE-ONBOARD",
      "name": "Onboard",
      "purpose": "Capture project or artifact intent.",
      "required_inputs": [
        "project_or_artifact_name",
        "purpose",
        "validation_pass_criteria",
        "constraints"
      ],
      "required_outputs": [
        "onboarding_record"
      ],
      "failure_modes": [
        "unclear_goal",
        "missing_acceptance_criteria",
        "unstated_constraints"
      ]
    },
    {
      "id": "STAGE-BRAINSTORM",
      "name": "Brainstorm",
      "purpose": "Generate candidate directions before narrowing into research and tasks.",
      "required_inputs": [
        "onboarding_record"
      ],
      "required_outputs": [
        "candidate_options",
        "selected_direction",
        "research_questions"
      ],
      "failure_modes": [
        "premature_convergence",
        "undocumented_rationale",
        "unbounded_option_set"
      ]
    },
    {
      "id": "STAGE-RESEARCH",
      "name": "Research",
      "purpose": "Collect and normalize source-backed information.",
      "required_inputs": [
        "research_questions"
      ],
      "required_outputs": [
        "source_records",
        "research_notes",
        "open_questions"
      ],
      "failure_modes": [
        "unsourced_claims",
        "stale_sources",
        "source_conflicts_unresolved"
      ]
    },
    {
      "id": "STAGE-SPEC",
      "name": "Specify",
      "purpose": "Convert research into governing specifications and schemas.",
      "required_inputs": [
        "research_notes",
        "source_records"
      ],
      "required_outputs": [
        "governing_spec",
        "schemas",
        "examples"
      ],
      "failure_modes": [
        "prose_without_contract",
        "schema_missing",
        "example_missing",
        "spec_ambiguity"
      ]
    },
    {
      "id": "STAGE-TASKS",
      "name": "Plan Tasks",
      "purpose": "Break the spec into small measurable tasks.",
      "required_inputs": [
        "governing_spec"
      ],
      "required_outputs": [
        "task_graph",
        "acceptance_criteria"
      ],
      "failure_modes": [
        "tasks_too_large",
        "tasks_not_testable",
        "missing_owner"
      ]
    },
    {
      "id": "STAGE-BUILD",
      "name": "Build",
      "purpose": "Implement only the bounded task target.",
      "required_inputs": [
        "task_graph",
        "governing_spec"
      ],
      "required_outputs": [
        "changed_artifacts",
        "action_log"
      ],
      "failure_modes": [
        "scope_creep",
        "unauthorized_file_changes",
        "missing_action_log"
      ]
    },
    {
      "id": "STAGE-TEST",
      "name": "Test",
      "purpose": "Run contract, scenario, and regression checks.",
      "required_inputs": [
        "changed_artifacts",
        "schemas",
        "examples"
      ],
      "required_outputs": [
        "test_results"
      ],
      "failure_modes": [
        "test_missing",
        "test_failure",
        "test_not_linked_to_spec"
      ]
    },
    {
      "id": "STAGE-EVALUATE",
      "name": "Evaluate",
      "purpose": "Score the run against validation pass criteria and gate requirements.",
      "required_inputs": [
        "test_results",
        "acceptance_criteria"
      ],
      "required_outputs": [
        "scorecard",
        "gate_results"
      ],
      "failure_modes": [
        "no_baseline",
        "no_threshold",
        "ambiguous_result"
      ]
    },
    {
      "id": "STAGE-DECIDE",
      "name": "Decide",
      "purpose": "Record keep, repair, or reject decision.",
      "required_inputs": [
        "gate_results",
        "scorecard"
      ],
      "required_outputs": [
        "promotion_decision"
      ],
      "failure_modes": [
        "missing_decision",
        "decision_without_evidence",
        "failed_run_without_repair"
      ]
    },
    {
      "id": "STAGE-REPAIR",
      "name": "Repair or Promote",
      "purpose": "Convert failures into repair tasks or promote successful artifacts.",
      "required_inputs": [
        "promotion_decision"
      ],
      "required_outputs": [
        "repair_tasks_or_promotion_record"
      ],
      "failure_modes": [
        "silent_failure",
        "repair_not_actionable",
        "promotion_without_gate_pass"
      ]
    }
  ]
}
```

---

## 3. Gate definitions

```json
{
  "_doc": "Gates are validation checks. In the tiny FRE kernel, a loop is not done until all blocking gates either pass or produce repair tasks.",
  "gates": [
    {
      "id": "GATE-ENVELOPE",
      "name": "Envelope Gate",
      "blocking": true,
      "checks": [
        "front_matter_present",
        "bottom_matter_present",
        "required_fields_present",
        "yaml_valid"
      ],
      "failure_classes": [
        "ENVELOPE_FRONTMATTER_MISSING",
        "ENVELOPE_BOTTOM_MATTER_MISSING",
        "ENVELOPE_REQUIRED_FIELD_MISSING",
        "ENVELOPE_INVALID_YAML"
      ]
    },
    {
      "id": "GATE-SOURCE",
      "name": "Source Gate",
      "blocking": true,
      "checks": [
        "source_ids_present",
        "source_records_exist",
        "material_claims_traceable"
      ],
      "failure_classes": [
        "SOURCE_ID_MISSING",
        "SOURCE_RECORD_NOT_FOUND",
        "CLAIM_UNSOURCED"
      ]
    },
    {
      "id": "GATE-SCHEMA-EXAMPLE",
      "name": "Schema / Example Gate",
      "blocking": true,
      "checks": [
        "schemas_exist",
        "examples_exist",
        "examples_validate_against_schemas"
      ],
      "failure_classes": [
        "SCHEMA_MISSING",
        "EXAMPLE_MISSING",
        "EXAMPLE_INVALID"
      ]
    },
    {
      "id": "GATE-TEST",
      "name": "Test Gate",
      "blocking": true,
      "checks": [
        "related_tests_present",
        "test_files_exist",
        "tests_pass"
      ],
      "failure_classes": [
        "RELATED_TEST_MISSING",
        "RELATED_TEST_FILE_NOT_FOUND",
        "TEST_RUN_FAILED"
      ]
    },
    {
      "id": "GATE-DOC-PARITY",
      "name": "Doc Parity Gate",
      "blocking": false,
      "checks": [
        "docs_updated_with_behavior_change",
        "diagrams_updated_if_structure_changed",
        "golden_path_updated_if_workflow_changed"
      ],
      "failure_classes": [
        "DOC_CODE_DRIFT",
        "DIAGRAM_STALE",
        "GOLDEN_PATH_STALE"
      ]
    },
    {
      "id": "GATE-PROMOTION",
      "name": "Promotion Decision Gate",
      "blocking": true,
      "checks": [
        "decision_exists",
        "decision_has_evidence",
        "failed_gates_have_repair_tasks"
      ],
      "failure_classes": [
        "PROMOTION_DECISION_MISSING",
        "PROMOTION_DECISION_INVALID",
        "FAILED_RUN_WITHOUT_REPAIR_TASK"
      ]
    }
  ]
}
```

---

## 4. Governed artifact contract

```json
{
  "_doc": "A governed artifact is any document, schema, test, report, or implementation file controlled by FRE.",
  "artifact": {
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
}
```

---

## 5. Run contract

```json
{
  "_doc": "A run is one execution of the FRE loop against one target artifact or bounded target set.",
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
  }
}
```

---

## 6. Gate result contract

```json
{
  "_doc": "Every validation gate emits a structured result.",
  "gate_result": {
    "gate_id": "GATE-ENVELOPE",
    "artifact_id": "SPEC-FRE-0001",
    "status": "fail",
    "blocking": true,
    "severity": "error",
    "message": "Missing bottom matter.",
    "failure_class": "ENVELOPE_BOTTOM_MATTER_MISSING",
    "evidence": {
      "path": "docs/specs/fre-method.md",
      "line": null
    },
    "repair_required": true
  }
}
```

---

## 7. Promotion decision contract

```json
{
  "_doc": "Every run ends with a decision. A failed run must produce repair tasks.",
  "promotion_decision": {
    "decision_id": "DECISION-0001",
    "run_id": "RUN-0001",
    "artifact_id": "SPEC-FRE-0001",
    "decision": "repair",
    "reason": "One or more blocking gates failed.",
    "evidence": [
      "runs/0001/gate-results.json",
      "runs/0001/report.md"
    ],
    "next_action": "Complete generated repair tasks and rerun validation.",
    "decided_at": "2026-05-16T00:00:00Z",
    "decider": "human"
  }
}
```

---

## 8. Repair task contract

```json
{
  "_doc": "Failures become repair tasks. No blocking failure is allowed to disappear silently.",
  "repair_task": {
    "repair_id": "REPAIR-0001",
    "run_id": "RUN-0001",
    "artifact_id": "SPEC-FRE-0001",
    "from_gate": "GATE-ENVELOPE",
    "failure_class": "ENVELOPE_BOTTOM_MATTER_MISSING",
    "blocking": true,
    "owner": "planning-agent",
    "recommended_action": "Add bottom matter with required fields.",
    "acceptance_criteria": [
      "Bottom matter sentinel exists",
      "Bottom matter YAML parses",
      "Envelope gate passes"
    ],
    "status": "open"
  }
}
```

---

## 9. Validation pass criteria

```jsx
The tiny FRE loop is validated when:

1. One governed artifact exists.
2. The artifact has a valid envelope.
3. All source IDs resolve.
4. Required schemas and examples exist.
5. Related tests exist and pass.
6. A gate result file is emitted.
7. A report is emitted.
8. A promotion decision is emitted.
9. If anything fails, repair tasks are emitted.
10. No blocking failure is silent.
```

## 10. Governed agent prompt contract

```jsx
Prompting is part of FRE governance when prompts are used to drive bounded agent execution.

A governed agent prompt contract exists to:
- translate specs into bounded execution instructions
- preserve validation integrity
- standardize reporting and fallback behavior
- prevent environment drift and fake-green execution
- make execution contracts portable across Copilot, Codex, Claude, and other agents

A prompt contract is not casual prose. It is an execution artifact.
```

```json
{
  "_doc": "A governed heavy-run prompt contract for agent execution.",
  "prompt_contract": {
    "schema_version": "0.1.0",
    "mode": "heavy_run",
    "mission": "Complete one bounded capability end-to-end in one run when feasible.",
    "current_verified_state": [
      "Known live facts are listed before execution begins."
    ],
    "hard_rules": [
      "Do not broaden scope beyond the bounded mission.",
      "Do not fake green results.",
      "Keep blocked states evidence-backed."
    ],
    "allowed_paths": [
      "Reuse existing local runtime surfaces.",
      "Patch only directly related files.",
      "Refresh proof artifacts when the bounded contract requires them."
    ],
    "disallowed_paths": [
      "Ad hoc architecture rewrites.",
      "Silent environment drift.",
      "Mocked success paths presented as real proofs."
    ],
    "tasks": [
      "Inspect current truth.",
      "Implement the smallest honest change.",
      "Run targeted validation.",
      "Refresh evidence.",
      "Report final truthful state."
    ],
    "validation_loop": [
      "inspect",
      "patch",
      "test",
      "proof",
      "fix",
      "rerun",
      "artifact_refresh",
      "docs_sync",
      "commit"
    ],
    "success_criteria": {
      "best_case": "The bounded capability passes honestly in one run.",
      "acceptable_fallback": "The capability remains blocked, but only with exact live evidence and no stale assumptions."
    },
    "report_contract": [
      "status",
      "proof_artifact",
      "live_evidence",
      "files_changed",
      "targeted_results",
      "commit_hash"
    ],
    "environment_policy": {
      "python_runtime": "uv_first",
      "forbid_pip_default": true,
      "forbid_venv_default": true,
      "forbid_paid_api_key_default": true
    }
  }
}
```

```jsx
Required principle:

Prompt contracts must follow the same authority chain as the rest of FRE:

sources → research → spec → tasks → build → tests → evaluation → promotion decision → repair.

If a prompt asks an agent to execute work, it must preserve that order rather than short-circuiting it.

Operational defaults:
- Prefer heavy autonomous runs when the task boundary is clear.
- Prefer `uv` for Python execution and environment management.
- Do not introduce paid-model API keys as the default runtime path when subscribed agent surfaces already exist.
```

### Repo-local canonical artifacts

The governed human-readable prompt-contract material should stay aligned with these repo-local artifacts:

- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt-index.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt-schema.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt.schema.json`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt.template.yaml`

Use the index file as the single repo-local entrypoint. These files are the concrete operator and implementation reference set for the Meta-Harness.

## 11. Minimal FRE instance

```json
{
  "fre_version": "0.1.0",
  "loop_id": "FRE-LOOP-0001",
  "name": "Minimal FRE Kernel Loop",
  "purpose": "Validate one governed artifact and produce a promotion or repair decision.",
  "scale": "artifact",
  "status": "draft",
  "target_artifact": {
    "artifact_id": "SPEC-FRE-0001",
    "title": "FRE Method",
    "artifact_type": "spec",
    "path": "docs/specs/fre-method.md"
  },
  "required_gates": [
    "GATE-ENVELOPE",
    "GATE-SOURCE",
    "GATE-SCHEMA-EXAMPLE",
    "GATE-TEST",
    "GATE-PROMOTION"
  ],
  "allowed_decisions": [
    "keep",
    "repair",
    "reject"
  ],
  "validation_pass_criteria": [
    "all_blocking_gates_pass",
    "gate_results_written",
    "report_written",
    "promotion_decision_written",
    "repair_tasks_written_if_failed"
  ]
}
```