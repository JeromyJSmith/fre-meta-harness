---
artifact_type: governed_triad_follow_up_prompt
prompt_id: PROMPT-YYYYMMDD-XXXX
handoff_id: HANDOFF-YYYYMMDD-XXXX
structured_prompt_artifact: ""
acting_role: orchestrator-validator
recommended_option_id: ""
repo_root: /Volumes/PixelTable/VW_iTWIN_Bridge/meta
parent_only: true
machine_truth_source: structured_contract_family
---

# Governed Triad Follow-Up Prompt

This markdown artifact is the parent-only companion surface for the governed
triad. It is not the machine-truth contract. The structured YAML/JSON prompt and
handoff artifacts remain authoritative.

## Consumption Order

1. Read the structured architect-review handoff artifact first.
2. Read the structured heavy-run prompt artifact next.
3. Use this markdown companion only to preserve operator-facing context,
   sequencing, and dispatch clarity.

## Parent-Only Guardrails

- Stay inside the standalone parent wrapper scope.
- Preserve the triad role ids exactly: `orchestrator-validator`, `research`,
  `architect`.
- Carry forward runtime-truth and command-evidence requirements from the
  structured prompt.
- Do not replace the structured contract family with prose.

## Decision Space

- Recommended option id: `{{recommended_option_id}}`
- Why this option was selected:
- Expected artifacts:

## Required Reads

- Structured handoff artifact:
- Structured heavy-run prompt artifact:
- Runtime-truth evidence artifacts:
- Command-evidence artifacts:

## Execution Notes

- Acting role:
- Upstream handoff:
- Dispatch target:
- Known blockers or escalation path:

---bottom-matter---
validation_status: draft
dispatch_message_ref: ""
structured_prompt_ref: ""
gate_progress:
  - gate: triad_handoff_consumed
    status: pending
    notes: ""
  - gate: structured_prompt_emitted
    status: pending
    notes: ""
  - gate: markdown_companion_emitted
    status: pending
    notes: ""
open_questions:
  - ""
