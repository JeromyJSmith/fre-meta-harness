---
id: "diagram-catalog"
slug: "diagram-catalog"
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

# Architecture Diagram Catalog

## Required diagram inventory
- L0: `10-system-architecture-overview.md`
- L1: `11-control-planes-and-runtime-planes.md`
- L2: `12-service-and-application-topology.md`
- L3: `21-capability-promotion-pipeline-spec.md`
- L4: `24-pipeline-composition-and-execution-spec.md`
- L5: `23-workflow-threading-and-orchestration-spec.md`
- L6: `13-data-platform-and-etl-architecture.md`
- L7: `30-data-domain-model-and-lineage-spec.md`
- L8: `14-observability-and-operational-telemetry.md`
- L9: `15-security-policy-and-fail-loud-controls.md`

All diagrams are embedded as Mermaid definitions in the owning spec.

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
