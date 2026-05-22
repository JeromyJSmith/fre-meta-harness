---
id: "capability-matrix-master"
slug: "capability-matrix-master"
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

# Capability Matrix Master

This artifact is the exhaustive normalized capability registry table.

| capability_id | upstream source | lane classification | trigger | actor | governed operations | target contracts | dependencies/blockers | evidence artifacts | current promotion state | next gate |
|---|---|---|---|---|---|---|---|---|---|---|
| pi-vs-claude-code | https://github.com/disler/pi-vs-claude-code | core | mesh_bootstrap | peer_mesh_host | list_agents, send_command, send_prompt, await_response | contracts/peer-mesh-runtime.yaml | Requires Bun >= 1.3.2, Pi Coding Agent CLI, and just; cross-device mode additionally requires `PI_COMS_NET_AUTH_TOKEN` and a declared hub URL. | examples/peer-mesh.valid.json | contractized | schema_contract_conformance_gate |
| the-library | https://github.com/disler/the-library | core | peer_join | peer_mesh_host | list_agents | contracts/library-distribution.yaml | Requires private Git or local-path access to the referenced artifacts and a governed catalog inside the parent wrapper. | examples/library-distribution.valid.json | contractized | schema_contract_conformance_gate |
| claude-code-hooks-mastery | https://github.com/disler/claude-code-hooks-mastery | core | before_send_prompt | prod_gatekeeper | send_prompt, send_command | contracts/policy-decision.yaml | Requires an adapter that exposes pre-prompt, pre-tool, post-tool, and stop lifecycle hooks; the parent contract is core even when a runtime adapter is still pending. | examples/hook-manifest.valid.json | contractized | schema_contract_conformance_gate |
| claude-code-hooks-multi-agent-observability | https://github.com/disler/claude-code-hooks-multi-agent-observability | core | peer_event_emit | mesh_verifier | list_agents, send_command, send_prompt, await_response | contracts/observability-ingest.yaml | Requires a running ingest sink (Bun/HTTP plus durable store) or an equivalent local sidecar; otherwise the lane must stay blocked or fixture-only. | examples/observability-ingest.valid.json | contractized | schema_contract_conformance_gate |
| just-prompt | https://github.com/disler/just-prompt | gated | challenge_review | prod_gatekeeper | send_prompt, await_response | contracts/agent-role-contract.yaml | Requires a running just-prompt MCP server plus provider credentials or a local-model equivalent; without those, the lane remains gated and must not be treated as default. | promotion/readiness.json | mapped | runtime_truth_blocker_precision_gate |
| agent-sandbox-skill | https://github.com/disler/agent-sandbox-skill | blocked_with_exact_dependency | delegated_build | dev_driver | send_command, await_response | contracts/agent-role-contract.yaml | Blocked until a real sandbox provider is configured; exact dependencies are an E2B account/API key today or a parity implementation such as exe.dev. | examples/agent-role-contract.valid.json | discovered | exact_dependency_gate |
| bowser | https://github.com/disler/bowser | gated | promotion_browser_check | mesh_verifier | send_command, await_response | contracts/capability-matrix.yaml | Gated on a real browser-validation requirement plus Playwright CLI or an equivalent browser control surface; otherwise the parent should not pretend this lane is active. | promotion/readiness.json | mapped | runtime_truth_blocker_precision_gate |
| mac-mini-agent | https://github.com/disler/mac-mini-agent | deployment_specific | deployment_sidecar_boot | peer_mesh_host | list_agents, send_command, await_response | contracts/capability-matrix.yaml | Deployment-specific: requires macOS, Accessibility + Screen Recording + Full Disk Access permissions, tmux, SSH/remote connectivity, and the paired host topology. | evaluation/tool-health/status.json | mapped | deployment_dependency_gate |
| fork-repository-skill | https://github.com/disler/fork-repository-skill | reference | manual_parallel_branch | dev_driver | send_command, await_response | contracts/capability-matrix.yaml | Reference only because it overlaps with existing delegation and peer-mesh lanes and depends on a Claude-style skill runtime. | evaluation/research/compiled/gap-placement-map.json | discovered | workflow_reuse_justification_gate |
| infinite-agentic-loop | https://github.com/disler/infinite-agentic-loop | reference | bounded_generation_wave | dev_driver | send_prompt, await_response | program.md | Reference only because the upstream infinite mode conflicts with bounded stop, plateau, and exact-blocker doctrine. | evaluation/research/compiled/gap-placement-map.json | discovered | workflow_reuse_justification_gate |
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
