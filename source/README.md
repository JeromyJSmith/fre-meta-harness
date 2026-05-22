---
id: "parent-meta-source-readme"
slug: "parent-meta-source-readme"
doctype: "source"
status: "active"
version: "1.0.0"
owner: "fre-meta-harness"
---

# Source

This directory holds parent-wrapper source provenance, normalization, and
prompt-trace artifacts, plus the parent-owned subsystem harness scaffold.

Files:

- `provenance.json`
- `prompt-contract-trace.json`
- `normalization.md`
- `subsystems/`

---bottom-matter---
status_summary:
  completeness: 1.0
  confidence: high
  doc_state: active_source

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Parent source surfaces now exist."
  - gate_id: registry_gate
    status: green
    notes: "Source role is explicit."
  - gate_id: manifest_gate
    status: green
    notes: "Source package is placed at the parent root."
  - gate_id: verification_gate
    status: green
    notes: "Validator checks required source files."
  - gate_id: state_gate
    status: green
    notes: "Source status is derived from validation."
  - gate_id: health_gate
    status: green
    notes: "No missing source package joins remain."
  - gate_id: promotion_gate
    status: amber
    notes: "Source transport now targets fresh clones of the published parent repo."

open_questions: []
pending_validations: []
promotion_criteria:
  - "Source package survives standalone repo transport."
blocked_by: []
next_iteration:
  owner: "codex"
  objective: "Reuse source package in fresh clones of the published standalone parent repo."
