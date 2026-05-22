---
id: "arch-security-fail-loud"
slug: "arch-security-fail-loud"
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

# Security, Policy, and Fail-Loud Controls

## Policy model
- Governed operations by role and trigger
- Explicit allow/block/ask decisions
- Fail-loud handling for blocked escalations

## Controls
- Runtime blocker precision is mandatory
- Fallbacks cannot silently replace blocked live paths
- Promotion requires explicit retained lower evidence level

## L9: Runtime mode diagram
```mermaid
stateDiagram-v2
  [*] --> SameHostActive
  SameHostActive --> CrossDeviceCandidate: prerequisites declared
  CrossDeviceCandidate --> CrossDeviceBlocked: missing exact dependency
  CrossDeviceCandidate --> CrossDeviceActive: exact dependency proven
  CrossDeviceBlocked --> SameHostActive: retain truthful baseline
```

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
