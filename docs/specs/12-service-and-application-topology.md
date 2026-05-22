---
id: "arch-service-app-topology"
slug: "arch-service-app-topology"
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

# Service and Application Topology

## Runtime service surfaces
- FastAPI service: `service/main.py`
- Inbox runtime implementation: `service/inbox_runtime.py`
- UI/dashboard application: `app/server.ts`

## L2: Governance triad + front-door handoff sequence
```mermaid
sequenceDiagram
  participant OP as Operator
  participant PK as Inbox Packet
  participant RT as Router
  participant TR as Triad
  participant DL as Delegation Bundle
  participant RR as Runtime Role
  OP->>PK: submit packet
  PK->>RT: validate + classify
  RT->>TR: triad review for gated paths
  TR->>DL: approve routing/delegation
  DL->>RR: execute bounded task
  RR->>RT: emit evidence + status
```

## Topology constraints
- Router cannot invent missing evidence
- Triad bypass forbidden
- Recursive documentation required for governed handoffs

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
