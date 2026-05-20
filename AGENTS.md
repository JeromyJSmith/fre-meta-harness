---
id: "parent-meta-agents"
slug: "parent-meta-agents"
doctype: "contract"
status: "active"
version: "1.0.0"
owner: "fre-meta-harness"
scope: "portable_parent_wrapper"
library_refs:
  - "library.yaml"
program_refs:
  - "program.md"
prompt_contract_refs:
  - "agent-heavy-run-prompt-index.md"
  - "agent-heavy-run-prompt-schema.md"
  - "agent-heavy-run-prompt.schema.json"
  - "agent-heavy-run-prompt.template.yaml"
  - "copilot-prompting-playbook.md"
comparison_refs:
  - "infranodus-phase-tool-map.json"
substrate_refs:
  - "pixeltable-operational-substrate.md"
upstream_local_refs:
  - "external/goal-md"
  - "external/meta-harness"
  - "external/autoresearch-mlx"
---

# AGENTS.md

## Purpose

This directory is the reusable parent Meta-Harness wrapper for the
`VW_iTwin_Bridge` body cell family. It owns portable wrapper doctrine,
contracts, prompt governance, proof-package surfaces, and promotion state.

## Active Body Cell

- `body.vw_itwin_bridge`
- Path: `/Volumes/PixelTable/VW_iTWIN_Bridge/VW_iTwin_Bridge`

## Parent Wrapper Rules

- Treat this directory as the outer wrapper, not the child runtime body.
- Keep the parent scaffold reusable across child repos.
- Bind every heavy or bounded execution prompt to the governed prompt contract.
- Use the InfraNodus phase-tool map for graph-backed gap analysis in every gate.
- Treat Pixeltable as the durable operational substrate and evidence sink.
- Keep parent-child bridge state in durable artifacts, not chat history.

## Required Parent References

- library spine: `library.yaml`
- prompt contract: `agent-heavy-run-prompt-*` plus
  `copilot-prompting-playbook.md`
- execution protocol: `program.md`
- comparison engine: `infranodus-phase-tool-map.json`
- substrate doctrine: `pixeltable-operational-substrate.md`
- imported local authorities: `external/goal-md/`, `external/meta-harness/`,
  `external/autoresearch-mlx/`
- proof package: `source/`, `schemas/`, `examples/`, `expected-failures/`,
  `tests/`, `evaluation/`, `promotion/`

---bottom-matter---
status_summary:
  completeness: 1.0
  confidence: high
  doc_state: active_contract

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Parent wrapper role and required authority surfaces are declared."
  - gate_id: registry_gate
    status: green
    notes: "Canonical parent references are explicitly listed."
  - gate_id: manifest_gate
    status: green
    notes: "Proof-package families and bridge surfaces are placed."
  - gate_id: verification_gate
    status: green
    notes: "Validator-backed contract checks exist in tests/."
  - gate_id: state_gate
    status: green
    notes: "State is derived from durable validation and readiness outputs."
  - gate_id: health_gate
    status: green
    notes: "Parent scaffold now points at library, prompts, comparison, and substrate."
  - gate_id: promotion_gate
    status: amber
    notes: "Parent wrapper is published; promotion now depends on keeping doctrine and evidence aligned."

open_questions: []

pending_validations:
  - "Refresh the validator after parent tool-health doctrine changes."

promotion_criteria:
  - "Parent scaffold validates cleanly."
  - "Standalone parent repo carries the same scaffold and proof package."

blocked_by:
  - "Live InfraNodus MCP analysis remains optional; the bounded local parent-layer substitute is the default until runtime access is intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Keep the published parent wrapper contract aligned with current tool-health evidence."
