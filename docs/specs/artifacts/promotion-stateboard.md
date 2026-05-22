---
id: "promotion-stateboard"
slug: "promotion-stateboard"
doctype: "artifact"
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

# Promotion Stateboard

This artifact tracks current promotion state per capability with next-gate and blocker precision context.

## Canonical state chain
`discovered -> mapped -> contractized -> validated-local -> workflow-integrated -> etl-integrated -> promoted`

| capability_id | lane_classification | current_state | next_gate | blocker_or_dependency | readiness_alignment_ref |
|---|---|---|---|---|---|
| pi-vs-claude-code | core | contractized | schema_contract_conformance_gate | Requires Bun >= 1.3.2, Pi Coding Agent CLI, and just; cross-device mode additionally requires `PI_COMS_NET_AUTH_TOKEN` and a declared hub URL. | promotion/readiness.json |
| the-library | core | contractized | schema_contract_conformance_gate | Requires private Git or local-path access to the referenced artifacts and a governed catalog inside the parent wrapper. | promotion/readiness.json |
| claude-code-hooks-mastery | core | contractized | schema_contract_conformance_gate | Requires an adapter that exposes pre-prompt, pre-tool, post-tool, and stop lifecycle hooks; the parent contract is core even when a runtime adapter is still pending. | promotion/readiness.json |
| claude-code-hooks-multi-agent-observability | core | contractized | schema_contract_conformance_gate | Requires a running ingest sink (Bun/HTTP plus durable store) or an equivalent local sidecar; otherwise the lane must stay blocked or fixture-only. | promotion/readiness.json |
| just-prompt | gated | mapped | runtime_truth_blocker_precision_gate | Requires a running just-prompt MCP server plus provider credentials or a local-model equivalent; without those, the lane remains gated and must not be treated as default. | promotion/readiness.json |
| agent-sandbox-skill | blocked_with_exact_dependency | discovered | exact_dependency_gate | Blocked until a real sandbox provider is configured; exact dependencies are an E2B account/API key today or a parity implementation such as exe.dev. | promotion/readiness.json |
| bowser | gated | mapped | runtime_truth_blocker_precision_gate | Gated on a real browser-validation requirement plus Playwright CLI or an equivalent browser control surface; otherwise the parent should not pretend this lane is active. | promotion/readiness.json |
| mac-mini-agent | deployment_specific | mapped | deployment_dependency_gate | Deployment-specific: requires macOS, Accessibility + Screen Recording + Full Disk Access permissions, tmux, SSH/remote connectivity, and the paired host topology. | promotion/readiness.json |
| fork-repository-skill | reference | discovered | workflow_reuse_justification_gate | Reference only because it overlaps with existing delegation and peer-mesh lanes and depends on a Claude-style skill runtime. | promotion/readiness.json |
| infinite-agentic-loop | reference | discovered | workflow_reuse_justification_gate | Reference only because the upstream infinite mode conflicts with bounded stop, plateau, and exact-blocker doctrine. | promotion/readiness.json |
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
