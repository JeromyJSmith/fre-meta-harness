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
- Treat inbox packets as front-door governance documents only until an explicit
  routing decision and delegation bundle name the target runtime role and mode.
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

## Runtime Separation

The inbox-first front-door runtime roles for this slice are:

- `user-facing-agent`
- `spec-interpreter`
- `filesystem-router`
- `intake-mapper`
- `semantic-cartographer`
- `wrapper-synthesizer`

These roles remain separate from both the governance triad and the older
peer-mesh runtime roles defined in `contracts/agent-role-contract.yaml`.
The triad governs handoff readiness from above; the front-door runtime consumes
only routed inbox artifacts.

## Inbox Front Door

The front door for runtime-facing work is the governed packet family:

- `contracts/inbox-packet.yaml`
- `contracts/inbox-routing-decision.yaml`
- `contracts/delegation-bundle.yaml`
- `contracts/front-door-runtime-topology.yaml`

Rules:

- Inbox packets use YAML front matter, a Markdown body, and
  `---bottom-matter---`.
- Packet prose is not machine truth by itself; routing and delegation authority
  come from the linked structured packet, routing, and delegation artifacts.
- The front-door runtime topology names the bridge between governance review,
  runtime intake, and routed delegation, but it does not collapse the role
  sets.

## Handoff Rules

- Governance review must name the triggering triad role, the next consumers,
  the bounded execution objective, and the evidence expectations.
- Runtime work starts only after an explicit inbox packet, routing decision,
  and delegation bundle exist as a routed chain.
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
- inbox/front-door protocol:
  - `contracts/inbox-packet.yaml`
  - `contracts/inbox-routing-decision.yaml`
  - `contracts/delegation-bundle.yaml`
  - `contracts/front-door-runtime-topology.yaml`
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
  - gate_id: schema_gate
    status: green
    notes: "Parent wrapper role, governance triad, and inbox packet shape are declared."
  - gate_id: scope_gate
    status: green
    notes: "Canonical parent references and parent-only scope remain explicit."
  - gate_id: consumer_gate
    status: green
    notes: "Front-door runtime consumers and triad boundaries are named."
  - gate_id: evidence_gate
    status: green
    notes: "Validator-backed packet, routing, and delegation surfaces exist in the parent repo."
  - gate_id: freshness_gate
    status: green
    notes: "State is tied to current parent artifacts and current run timestamps."
  - gate_id: readiness_gate
    status: green
    notes: "Parent scaffold now points at packet, routing, delegation, and front-door topology surfaces."

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
