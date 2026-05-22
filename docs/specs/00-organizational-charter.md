---
id: "org-charter"
slug: "org-charter"
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

# Organizational Charter

## Mission
Deliver a project-agnostic parent harness that turns governed capabilities into truthful tools, workflows, and ETL-ready evidence pipelines.

## Scope
- Parent governance contracts and promotion doctrine
- Front-door inbox/routing/delegation lifecycle
- Capability productization into reusable tooling threads
- Data and evidence pipeline planning

## Non-goals
- Claiming child-runtime adoption from parent docs
- Promoting cross-device runtime without exact proof
- Treating docs-only edits as runtime activation evidence

## Decision rights
- Governance triad approves promotion boundaries
- Runtime role owners execute only routed delegation bundles
- Metrics and validation contracts arbitrate promotion readiness

## Escalation model
- Any blocked dependency escalates with exact blocker detail
- Any fallback downgrade must be fail-loud and logged
- Any topology ambiguity escalates to triad review

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
