---
id: "arch-control-runtime-planes"
slug: "arch-control-runtime-planes"
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

# Control Planes and Runtime Planes

## Plane definitions
- Governance/control plane: triad review and gate decisions
- Runtime plane: delegated role execution
- Evidence plane: metrics, validation, tool-health, readiness

## L1: Control vs runtime diagram
```mermaid
flowchart TB
  subgraph GovernancePlane
    OV[orchestrator-validator]
    RS[research]
    AR[architect]
  end
  subgraph RuntimePlane
    UFA[user-facing-agent]
    SI[spec-interpreter]
    FR[filesystem-router]
    IM[intake-mapper]
    SC[semantic-cartographer]
    WS[wrapper-synthesizer]
  end
  GovernancePlane -->|routing + delegation policy| RuntimePlane
```

## Separation rules
- Governance roles cannot self-declare runtime completion
- Runtime roles cannot self-promote governance outcomes

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
