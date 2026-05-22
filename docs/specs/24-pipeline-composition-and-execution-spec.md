---
id: "pipeline-composition-execution"
slug: "pipeline-composition-execution"
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

# Pipeline Composition and Execution Specification

## Pipeline DAG conventions
- Explicit entry trigger
- Explicit contract boundary between nodes
- Deterministic terminal state per node

## Execution states
- queued
- running
- blocked
- failed
- completed
- reverted

## Retry and stop/fail boundaries
- Retry only with retained blocker context
- Fail-loud on dependency gaps
- Preserve lower truthful evidence level when escalation fails

## L4: Capability-to-tool productization map
```mermaid
flowchart LR
  CM[Capability Matrix] --> CD[Contractized Definition]
  CD --> TD[Tool Definition]
  TD --> WT[Workflow Thread]
  WT --> ETL[ETL Pipeline Stage]
  ETL --> PR[Promotion Readiness]
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
