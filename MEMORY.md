---
id: "parent-meta-memory"
slug: "parent-meta-memory"
doctype: "memory"
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

# MEMORY.md

## Stable Truths

- This directory is the parent wrapper, not the project runtime body.
- The active body cell is `body.vw_itwin_bridge`.
- The child wrapper currently lives at
  `/Volumes/PixelTable/VW_iTWIN_Bridge/VW_iTwin_Bridge/meta/`.
- The wrapper model is fractal: every level should expose `README.md`,
  `AGENTS.md`, `CLAUDE.md`, `MEMORY.md`, `GOAL.md`, and `GOLDENPATH.md`.
- Every heavy or bounded prompt must trace back to the governed prompt schema.
- Every real parent ratchet run must pass through `program.md`.
- Every lifecycle gate should be challengeable through InfraNodus.
- Durable state is designed to flow toward Pixeltable as the substrate.
- The imported local authority clones under `external/` are read-only truth
  sources for the current ratchet design.

## Current Wrapper Doctrine

- Parent wrapper stores reusable contracts, body registry, memory, evidence,
  runs, prompt contract, comparison doctrine, and substrate doctrine.
- Child wrapper owns project-local goals, golden paths, scorers, verifiers,
  and proof loops.
- Parent and child communicate through durable artifacts, not chat-only
  context.

## Open Decisions

- Exact bridge artifact format between parent and child wrappers.
- Canonical rollout order for future gate directories once the standalone repo
  exists.
- Schema parity strategy across JSON Schema, Pydantic, Zod, and TypeScript.

---bottom-matter---
status_summary:
  completeness: 1.0
  confidence: high
  doc_state: active_memory

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Stable truths include prompt, comparison, and substrate doctrine."
  - gate_id: registry_gate
    status: green
    notes: "Parent and child responsibilities are separated."
  - gate_id: manifest_gate
    status: green
    notes: "Memory is placed as a parent authority surface."
  - gate_id: verification_gate
    status: green
    notes: "Validator checks this file for front and bottom matter."
  - gate_id: state_gate
    status: green
    notes: "Open decisions are explicit instead of implicit drift."
  - gate_id: health_gate
    status: green
    notes: "No missing doctrine joins remain in memory."
  - gate_id: promotion_gate
    status: amber
    notes: "Promotion still depends on standalone parent repo creation."

open_questions:
  - "Should future standalone repo memory include rollout summaries or only canonical doctrine?"

pending_validations:
  - "Revalidate this memory surface in the standalone repo."

promotion_criteria:
  - "Parent memory remains transportable and validator-backed."

blocked_by:
  - "Standalone repo not yet initialized."

next_iteration:
  owner: "codex"
  objective: "Promote this memory contract into the standalone parent repo."
