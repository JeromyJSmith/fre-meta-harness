---
id: "parent-meta-agents"
slug: "parent-meta-agents"
doctype: "contract"
status: "active"
version: "1.1.0"
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
governance_contract_refs:
  - "contracts/three-agent-topology.yaml"
  - "contracts/agent-extension-request.yaml"
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
It is the governance layer above runtime execution, not the runtime mesh itself.

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
- Keep governance triad decisions separate from runtime mesh execution roles.
- Route any self-extension proposal through
  `contracts/agent-extension-request.yaml` as a request artifact only.
- Do not claim live child-runtime integration from parent docs alone.

## Governance Triad

The governance core for this parent wrapper is defined in
`contracts/three-agent-topology.yaml`.

- `orchestrator-validator`: owns the parent governance loop, triad review, and
  promotion or blocker decisions
- `research`: harvests bounded evidence and dependency truth for governance
  review
- `architect`: turns approved governance intent into parent-owned contracts,
  prompts, and handoff structure

These role ids are governance and control roles only. They do not replace the
runtime mesh roles defined in `contracts/agent-role-contract.yaml`.

## Runtime Mesh Separation

Runtime mesh roles remain the execution authority:

- `peer_mesh_host`
- `prod_gatekeeper`
- `dev_driver`
- `mesh_verifier`

The triad governs the mesh from above. When execution is needed, triad roles
map into runtime mesh roles through an explicit handoff instead of overwriting
the runtime role contract.

## Handoff Rules

- Governance review must name the triggering triad role, the target runtime
  role, the bounded execution objective, and the evidence expectations.
- Runtime work starts only after an explicit handoff from the triad into the
  runtime mesh.
- A blocker must stay explicit when evidence, dependency, or policy conditions
  are not met.
- Self-extension loops stay governed at the request-contract layer until a
  downstream owner is named; no parent document implies auto-provisioning.

## Parent-Only Boundaries

- This repo owns parent doctrine, governed prompts, governed handoffs, review
  outputs, extension requests, and promotion or blocker evidence.
- This repo does not claim that the child body repo or runtime mesh has already
  adopted or executed those parent artifacts.
- Parent changes must preserve the distinction between portable wrapper
  governance and child/runtime implementation.

## Required Parent References

- library spine: `library.yaml`
- prompt contract: `agent-heavy-run-prompt-*` plus
  `copilot-prompting-playbook.md`
- execution protocol: `program.md`
- comparison engine: `infranodus-phase-tool-map.json`
- substrate doctrine: `pixeltable-operational-substrate.md`
- governance topology: `contracts/three-agent-topology.yaml`
- governed self-extension requests: `contracts/agent-extension-request.yaml`
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
    notes: "Parent wrapper role, governance triad, and required authority surfaces are declared."
  - gate_id: registry_gate
    status: green
    notes: "Canonical parent references and governance contract surfaces are explicitly listed."
  - gate_id: manifest_gate
    status: green
    notes: "Proof-package families, parent-only boundaries, and bridge surfaces are placed."
  - gate_id: verification_gate
    status: green
    notes: "Validator-backed contract checks exist in tests/, while governance claims stay bounded to parent-owned surfaces."
  - gate_id: state_gate
    status: green
    notes: "State is derived from durable validation and readiness outputs, not from implied child-runtime adoption."
  - gate_id: health_gate
    status: green
    notes: "Parent scaffold now points at library, prompts, comparison, substrate, and governance topology."
  - gate_id: promotion_gate
    status: amber
    notes: "Parent wrapper is published; promotion now depends on keeping triad governance, handoff rules, and evidence aligned."

open_questions: []

pending_validations:
  - "Refresh the validator after parent governance topology additions and tool-health doctrine changes."

promotion_criteria:
  - "Parent scaffold validates cleanly."
  - "Governance triad separation from runtime mesh remains explicit."
  - "Standalone parent repo carries the same scaffold and proof package."

blocked_by:
  - "Live InfraNodus MCP analysis remains optional; the bounded local parent-layer substitute is the default until runtime access is intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Keep the published parent wrapper contract aligned with current governance topology, handoff rules, and tool-health evidence."
