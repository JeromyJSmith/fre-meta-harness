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
- keep governance triad roles separate from runtime mesh roles
- send any self-extension proposal through
  `contracts/agent-extension-request.yaml` as a governed request only
- do not claim child-runtime adoption or activation from parent artifacts alone

Governance triad:

- `orchestrator-validator` governs parent review, handoff readiness, and
  blocker truth
- `research` gathers bounded evidence and dependency truth for review
- `architect` shapes parent contracts, prompts, and handoff artifacts

Runtime mesh roles remain defined in `contracts/agent-role-contract.yaml`:

- `peer_mesh_host`
- `prod_gatekeeper`
- `dev_driver`
- `mesh_verifier`

Handoff rule:

- when execution is needed, the triad maps into runtime mesh roles through an
  explicit handoff instead of replacing runtime role definitions
- parent-only work stops at governed contracts, docs, prompts, handoffs,
  review outputs, extension requests, and promotion or blocker evidence unless
  a downstream runtime owner is explicitly named

---bottom-matter---
status_summary:
  completeness: 0.98
  confidence: high
  doc_state: active_contract

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Parent execution rules and governance triad separation are explicit."
  - gate_id: registry_gate
    status: green
    notes: "Required authority references and governance contracts are declared."
  - gate_id: manifest_gate
    status: green
    notes: "Operational note is correctly placed at the parent root with parent-only boundaries."
  - gate_id: verification_gate
    status: green
    notes: "Contract validator checks front matter and bottom matter while runtime adoption claims remain bounded."
  - gate_id: state_gate
    status: green
    notes: "State is backed by evaluation outputs, not by implied child-runtime integration."
  - gate_id: health_gate
    status: green
    notes: "No dangling parent execution references remain and runtime handoff rules are explicit."
  - gate_id: promotion_gate
    status: amber
    notes: "Published parent repo exists; promotion now depends on refreshed parent evidence and truthful triad-to-runtime handoffs."

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
