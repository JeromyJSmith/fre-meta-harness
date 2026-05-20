---
id: "parent-meta-claude"
slug: "parent-meta-claude"
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

# CLAUDE.md

Parent wrapper operational note:

- start with the parent scaffold and the active body registry
- use the governed prompt schema for every heavy run
- use `program.md` for every real parent ratchet run
- use InfraNodus at every lifecycle gate
- treat Pixeltable as the durable substrate
- read the local imported upstream authority clones before modifying the ratchet
- read and write durable wrapper artifacts before claiming state

---bottom-matter---
status_summary:
  completeness: 0.98
  confidence: high
  doc_state: active_contract

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Parent execution rules are explicit."
  - gate_id: registry_gate
    status: green
    notes: "Required authority references are declared."
  - gate_id: manifest_gate
    status: green
    notes: "Operational note is correctly placed at the parent root."
  - gate_id: verification_gate
    status: green
    notes: "Contract validator checks front matter and bottom matter."
  - gate_id: state_gate
    status: green
    notes: "State is backed by evaluation outputs."
  - gate_id: health_gate
    status: green
    notes: "No dangling parent execution references remain."
  - gate_id: promotion_gate
    status: amber
    notes: "Published parent repo exists; promotion now depends on refreshed parent evidence."

open_questions: []

pending_validations:
  - "Rerun parent contract validator after tool-health doctrine changes."

promotion_criteria:
  - "Operational rules survive transport into the standalone parent repo."

blocked_by:
  - "Live InfraNodus analysis remains API/OAuth-bound until runtime credentials are intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Keep this parent operational note aligned with the published wrapper and its tool-health evidence."
