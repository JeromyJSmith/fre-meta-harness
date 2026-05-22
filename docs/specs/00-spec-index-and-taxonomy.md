---
id: "spec-00-index"
slug: "spec-00-index"
doctype: "spec"
status: "active"
version: "1.0.0"
owner: "fre-meta-harness"
scope: "portable_parent_wrapper"
anchors:
  - "contracts/capability-matrix.yaml"
  - "contracts/front-door-runtime-topology.yaml"
  - "contracts/subsystem-harness-topology.yaml"
  - "contracts/parent-capability-metrics.yaml"
  - "infranodus-phase-tool-map.json"
created_at: "2026-05-22"
---

# Specification Suite Index and Taxonomy

This index defines the complete planning and implementation specification suite for the parent harness.

## Taxonomy

- **00–03**: Organizational planning and governance
- **10–15**: Core architecture
- **20–24**: Capability-to-tool productization and pipelines
- **30–35**: ETL and data processing
- **40–43**: Implementation and operations
- **artifacts/**: Capability Matrix Master + Promotion Stateboard

## Baseline alignment constraints

1. All specs are anchored to the capability matrix, front-door topology, subsystem topology, metrics doctrine, and phase/tool map.
2. Same-host lanes are active truth; cross-device lanes remain blocked-until-proven.
3. Governance triad roles and runtime roles remain explicitly separated.
4. Subsystem documents remain non-activation scaffolds unless explicit runtime evidence exists.

## Deliverables map

- Organizational suite: `00`, `01`, `02`, `03`
- Architecture suite: `10`, `11`, `12`, `13`, `14`, `15`
- Productization suite: `20`, `21`, `22`, `23`, `24`
- ETL suite: `30`, `31`, `32`, `33`, `34`, `35`
- Operations suite: `40`, `41`, `42`, `43`
- Mapping artifacts: `artifacts/capability-matrix-master.md`, `artifacts/promotion-stateboard.md`

---bottom-matter---
status_summary:
  completeness: 1.0
  confidence: high
  doc_state: active_spec

gate_progress:
  - gate_id: schema_gate
    status: green
    notes: "Anchored to parent contract truth."
  - gate_id: scope_gate
    status: green
    notes: "Preserves same-host active and cross-device blocked boundaries."
  - gate_id: consumer_gate
    status: green
    notes: "Maintains governance/runtime role separation."
  - gate_id: evidence_gate
    status: green
    notes: "Maps to contract-backed artifacts and evidence paths."
  - gate_id: promotion_gate
    status: amber
    notes: "Requires implementation execution to promote beyond planning."

open_questions: []
pending_validations:
  - "Run parent validator after spec updates to confirm no contract regressions."
promotion_criteria:
  - "Spec suite remains aligned to capability matrix and topology contracts."
blocked_by: []
next_iteration:
  owner: "codex"
  objective: "Execute P0 implementation checklist against this specification suite."
