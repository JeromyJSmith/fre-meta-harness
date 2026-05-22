---
id: "arch-system-overview"
slug: "arch-system-overview"
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

# System Architecture Overview

## Architecture summary
This parent harness is a governance-first wrapper coordinating capability contracts, runtime handoffs, and evidence-backed promotion outcomes.

## L0: System context diagram
```mermaid
flowchart LR
  U[Users / Operators] --> I[inbox/*.md packets]
  I --> R[Routing + Delegation]
  R --> RT[Runtime role executions]
  RT --> E[evaluation/tool-health + reports]
  E --> P[promotion/readiness.json]
  G[Governance triad] --> R
  C[Contracts/Schemas] --> R
  C --> P
```

## Key boundaries
- Same-host runtime lanes are active baseline
- Cross-device lanes are blocked until exact dependencies are proven
- Parent docs cannot overclaim subsystem activation

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
