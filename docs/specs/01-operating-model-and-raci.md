---
id: "org-operating-model"
slug: "org-operating-model"
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

# Operating Model and RACI

## Governance vs runtime role model
- Governance plane: orchestrator-validator, research, architect
- Runtime plane: user-facing-agent, spec-interpreter, filesystem-router, intake-mapper, semantic-cartographer, wrapper-synthesizer

## RACI summary
- **Accountable**: orchestrator-validator for gate and promotion outcomes
- **Responsible**: runtime role owner per routed delegation bundle
- **Consulted**: research and architect during contract and capability transitions
- **Informed**: operator and evidence consumers via tool-health and readiness artifacts

## Handoff ownership map
1. Inbox packet authored and validated
2. Routing decision emitted
3. Delegation bundle created
4. Runtime execution and evidence emission
5. Governance review and promotion state update

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
