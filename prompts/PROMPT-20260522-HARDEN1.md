---
artifact_type: governed_triad_follow_up_prompt
prompt_id: PROMPT-20260522-HARDEN1
handoff_id: HANDOFF-20260522-HARDEN1
structured_prompt_artifact: prompts/PROMPT-20260522-HARDEN1.yaml
acting_role: orchestrator-validator
recommended_option_id: option-a
repo_root: /Volumes/PixelTable/VW_iTWIN_Bridge/meta
parent_only: true
machine_truth_source: structured_contract_family
---

# Governed Triad Follow-Up Prompt

This markdown artifact is the parent-only companion surface for the multi-phase
repo hardening run. The structured YAML prompt remains the machine-truth
artifact.

## Consumption Order

1. Read `evaluation/tool-health/status.json`.
2. Read `prompts/PROMPT-20260522-HARDEN1.yaml`.
3. Use this markdown companion only to preserve operator-facing context,
   sequencing, and dispatch clarity.

## Parent-Only Guardrails

- Stay inside the standalone parent wrapper scope.
- Keep parent-only governance and runtime truth explicit.
- Do not convert fixture, dry, or credential-gated lanes into stronger statuses
  without fresh evidence.
- Treat missing launcher config or missing tests as findings, not as hidden
  assumptions.

## Decision Space

- Recommended option id: `option-a`
- Why this option was selected: the requested work is not a single narrow slice;
  it is a phased hardening run that should begin with a health audit and then
  land portability, testability, and structural-debt reductions in sequence.
- Expected artifact families:
  - repo-health report artifacts
  - refreshed tool-health artifacts
  - split validator or validator-family surfaces
  - smoke and runtime tests
  - doctrine source-of-truth pattern updates
  - runbook clarifications

## Required Reads

- Health authority: `evaluation/tool-health/status.json`
- Portability and truth surface: `scripts/refresh-parent-tool-health.py`
- Validator surface: `tests/validate_parent_wrapper_contract.py`
- Runtime surface:
  - `app/server.ts`
  - `package.json`
  - `pyproject.toml`
- Doctrine surfaces:
  - `README.md`
  - `GOAL.md`
  - `program.md`
  - `library.yaml`

## Execution Notes

- Acting role: `orchestrator-validator`
- Upstream handoff: `evaluation/tool-health/status.json`
- Packet artifact type: `.plan.md`
- Required gate state: `amber`
- Dispatch target: `copilot`
- Known blockers or escalation path: if `.mcp.json` is absent, harden the real
  launcher surfaces that exist and keep that absence explicit in the report.

---bottom-matter---
validation_status: draft
dispatch_message_ref: "evaluation/tool-health/status.json"
structured_prompt_ref: "prompts/PROMPT-20260522-HARDEN1.yaml"
gate_progress:
  - gate: triad_handoff_consumed
    status: pending
    notes: "Awaiting the multi-phase repo hardening run."
  - gate: structured_prompt_emitted
    status: pending
    notes: "Structured prompt path is reserved and aligned with prompt_id."
  - gate: markdown_companion_emitted
    status: pending
    notes: "Markdown companion path is reserved and aligned with prompt_id."
open_questions:
  - "If phase 3 proves too broad for one bounded run, which remaining structural debt should become the next governed follow-up slice?"
