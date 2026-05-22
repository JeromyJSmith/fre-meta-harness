---
id: "parent-meta-claude"
slug: "parent-meta-claude"
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

# CLAUDE.md

Parent wrapper operational note:

- start with the parent scaffold and the active body registry
- use the governed prompt schema for every heavy run
- use `program.md` for every real parent ratchet run
- use InfraNodus at every lifecycle gate
- treat Pixeltable as the durable substrate
- read the local imported upstream authority clones before modifying the ratchet
- read and write durable wrapper artifacts before claiming state
- keep governance triad roles separate from front-door runtime roles and from
  peer-mesh runtime roles
- send any self-extension proposal through
  `contracts/agent-extension-request.yaml` as a governed request only
- treat inbox packets as front-door governance artifacts until a structured
  routing decision and delegation bundle explicitly hand off to runtime
- do not claim child-runtime adoption or activation from parent artifacts alone

Governance triad:

- `orchestrator-validator` governs parent review, handoff readiness, and
  blocker truth
- `research` gathers bounded evidence and dependency truth for review
- `architect` shapes parent contracts, prompts, and handoff artifacts

Front-door runtime roles for the inbox-first slice are:

- `user-facing-agent`
- `spec-interpreter`
- `filesystem-router`
- `intake-mapper`
- `semantic-cartographer`
- `wrapper-synthesizer`

The older peer-mesh runtime roles remain defined in
`contracts/agent-role-contract.yaml` and are not overwritten by this slice.

Handoff rule:

- when execution is needed, the triad emits an inbox packet, routing decision,
  and delegation bundle instead of replacing runtime role definitions
- use the inbox/front-door contract family when that handoff begins:
  `contracts/inbox-packet.yaml`,
  `contracts/inbox-routing-decision.yaml`,
  `contracts/delegation-bundle.yaml`, and
  `contracts/front-door-runtime-topology.yaml`
- parent-only work stops at governed contracts, docs, prompts, handoffs,
  review outputs, extension requests, and promotion or blocker evidence unless
  a downstream runtime owner is explicitly named

---bottom-matter---
status_summary:
  completeness: 0.98
  confidence: high
  doc_state: active_contract

gate_progress:
  - gate_id: schema_gate
    status: green
    notes: "Parent execution rules and governed packet shape are explicit."
  - gate_id: scope_gate
    status: green
    notes: "Required authority references and parent-only scope remain explicit."
  - gate_id: consumer_gate
    status: green
    notes: "Front-door runtime consumers and triad separation are declared."
  - gate_id: evidence_gate
    status: green
    notes: "Contract validator checks packet, routing, and delegation surfaces while runtime adoption claims remain bounded."
  - gate_id: freshness_gate
    status: green
    notes: "State is backed by current parent artifacts rather than implied child-runtime integration."
  - gate_id: readiness_gate
    status: green
    notes: "No dangling parent execution references remain and inbox-first handoff rules are explicit."

open_questions: []

pending_validations:
  - "Rerun parent contract validator after governance topology and tool-health doctrine changes."

promotion_criteria:
  - "Operational rules survive transport into the standalone parent repo."
  - "Governance triad and runtime mesh roles remain explicitly separated."

blocked_by:
  - "Live InfraNodus MCP analysis remains optional; the bounded local parent-layer substitute is the default until runtime access is intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Keep this parent operational note aligned with the published wrapper, its governance topology, and its tool-health evidence."
