---
id: "org-roadmap-release"
slug: "org-roadmap-release"
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

# Roadmap and Release Model

## Milestone tranches
- **Tranche A (P0)**: planning baseline, capability mapping, L0-L4 diagrams
- **Tranche B (P1)**: validation and observability alignment, L5-L8 diagrams
- **Tranche C (P2)**: deployment expansion, L9 diagram, migration/cutover hardening

## Release model
- Gate-based release from planning -> implementation-ready
- Readiness.json remains final promotion authority
- Regression windows use previous kept cycles as baseline

## Promotion criteria by tranche
- P0: complete capability stateboard + gate model + dependency-linked checklist
- P1: complete test strategy + operational playbooks + observability topology
- P2: complete runtime mode expansion plan + recurrent review cadence

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
