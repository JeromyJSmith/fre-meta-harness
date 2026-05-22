---
id: "packet-fre-meta-harness-front-door-plan"
slug: "fre-meta-harness-front-door-plan"
doctype: "inbox_packet"
status: "ready_for_routing"
version: "1.0.0"
owner: "fre-meta-harness"
artifact_id: "PACKET-20260521-FRONTDOOR"
artifact_type: ".plan.md"
producer_role: "architect"
target_scope: "portable_parent_wrapper"
repo_root: "/Volumes/PixelTable/VW_iTWIN_Bridge/meta"
parent_only: true
structured_contract_ref: "contracts/inbox-packet.yaml"
structured_artifact_ref: "inbox/FRE-META-HARNESS_PLAN.plan.json"
routing_tags:
  - "front-door"
  - "runtime-scaffold"
  - "recursive-documentation"
required_consumers:
  - "filesystem-router"
  - "architect"
  - "research"
upstream_refs:
  - "contracts/three-agent-topology.yaml"
evidence_refs:
  - "library.yaml"
  - "agentics-library.md"
  - "README.md"
created_at: "2026-05-21T00:00:00Z"
updated_at: "2026-05-21T00:00:00Z"
---

# Front-Door Intake, Spec, and Recursive Wrapping Plan

## Summary
Implement the next major `fre-meta-harness` slice as the **first real project-consumption runtime** in `/Volumes/PixelTable/VW_iTWIN_Bridge/meta`, built on top of the already-landed governance triad.

This slice introduces:
- a Bun/TypeScript `app/` surface as the conversational front door, dashboard, and living documentation UI
- a Python single-file agent/workflow plane plus FastAPI/FastMCP service layer as the executable backend for intake, mapping, analysis, and governed wrapping

Core separation rules:
- governance roles review, decide, and promote
- runtime roles intake, interpret, map, wrap, and document
- every subdivision emits both a working map and a documentation map

## First executable lifecycle
1. `project_attach`
2. `conversation_capture`
3. `spec_interpretation`
4. `user_confirmation`
5. `drop_ingest`
6. `content_inventory`
7. `semantic_map`
8. `subsystem_registry`
9. `wrapper_binding`
10. `improvement_queue`
11. `triad_review`
12. `promotion_or_block`

## Runtime roles to scaffold
- `user-facing-agent`
- `spec-interpreter`
- `intake-mapper`
- `semantic-cartographer`
- `filesystem-router`
- `wrapper-synthesizer`

## Governing rule
The inbox-first packet protocol must sit in front of this lifecycle so plans,
specs, analyses, tests, and handoffs are persisted and routed before deeper
runtime work begins.

---bottom-matter---
validation_status: "pending_runtime_validation"
status_summary:
  completeness: 0.84
  confidence: high
  doc_state: "governed_inbox_packet"
gate_progress:
  - gate_id: schema_gate
    status: amber
    notes: "Awaiting the dedicated inbox packet schema and validator wiring."
  - gate_id: scope_gate
    status: green
    notes: "The packet is scoped to the parent repo only."
  - gate_id: consumer_gate
    status: green
    notes: "The packet names the router and bounded governance consumers."
  - gate_id: evidence_gate
    status: green
    notes: "The packet points at parent governance and library surfaces."
  - gate_id: freshness_gate
    status: green
    notes: "The packet is local to the current parent implementation stage."
  - gate_id: readiness_gate
    status: amber
    notes: "Execution depends on the inbox-first router and prompt wiring landing."
  - gate_id: promotion_gate
    status: amber
    notes: "Promotion waits on runnable front-door scaffolding and packet routing proof."
open_questions:
  - "Which front-door lifecycle stages should become fully active in the first real runtime release after the inbox protocol lands?"
pending_validations:
  - "Validate this plan packet against the inbox packet schema."
promotion_criteria:
  - "Front-door lifecycle contracts and runtime role surfaces validate."
  - "The inbox protocol routes this packet without bypassing gatekeeping."
blocked_by:
  - "The packet remains advisory until the inbox watcher and routing contracts are active."
next_iteration:
  owner: "architect"
  objective: "Consume this packet through the inbox-first routing path and emit the next bounded implementation slice."
