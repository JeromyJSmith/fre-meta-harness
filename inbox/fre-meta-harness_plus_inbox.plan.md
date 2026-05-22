---
id: "packet-fre-meta-harness-plus-inbox-plan"
slug: "fre-meta-harness-plus-inbox-plan"
doctype: "inbox_packet"
status: "ready_for_routing"
version: "1.0.0"
owner: "fre-meta-harness"
artifact_id: "PACKET-20260521-INBOXPLAN"
artifact_type: ".plan.md"
producer_role: "orchestrator-validator"
target_scope: "portable_parent_wrapper"
repo_root: "/Volumes/PixelTable/VW_iTWIN_Bridge/meta"
parent_only: true
structured_contract_ref: "contracts/inbox-packet.yaml"
structured_artifact_ref: "inbox/fre-meta-harness_plus_inbox.plan.json"
routing_tags:
  - "inbox-first"
  - "front-door"
  - "delegation"
  - "gatekeeping"
required_consumers:
  - "filesystem-router"
  - "architect"
  - "orchestrator-validator"
upstream_refs:
  - "inbox/FRE-META-HARNESS_PLAN.plan.md"
evidence_refs:
  - "AGENTS.md"
  - "CLAUDE.md"
  - "prompts/governed-triad-follow-up-prompt.template.md"
  - "agent-heavy-run-prompt.schema.json"
  - "architect-review-handoff-prompt.schema.json"
created_at: "2026-05-21T00:00:00Z"
updated_at: "2026-05-21T00:00:00Z"
---

# Inbox-First Front-Door and Delegation Control Plane Plan

## Summary
Implement the next parent-only `fre-meta-harness` tranche in `/Volumes/PixelTable/VW_iTWIN_Bridge/meta` as an **inbox-first control plane** that sits in front of all existing triad governance and future runtime work.

From this point forward, every meaningful artifact created by the system or by human collaboration must enter through the governed inbox first:
- brainstorms
- plans
- analyses
- tests
- review outcomes
- handoff prompts
- extension requests
- confirmed specs
- checkpoint reviews

This tranche makes that rule executable by adding:
- a governed **inbox artifact protocol**
- a **routing and delegation protocol**
- a **front-door runtime role family**
- a **recursive documentation protocol**
- a **dual-stack parent runtime scaffold**:
  - Bun/TypeScript `app/` for the front door, dashboard, and living HTML documentation
  - Python single-file agents/workflows plus FastAPI/FastMCP service adapters for watch, routing, analysis, and execution

The triad remains the governance layer. The new runtime/front-door roles remain operational intake and mapping roles. The two layers must never collapse into each other.

## Implementation Changes
### 1. Inbox-first protocol becomes the required entrypoint
Define the inbox as the only valid first destination for new work artifacts.

Add governed contracts and schemas for:
- `inbox-envelope`
- `inbox-routing-decision`
- `brainstorm-record`
- `plan-record`
- `analysis-record`
- `test-record`
- `delegation-bundle`
- `checkpoint-review`
- `confirmed-spec`
- `recursive-documentation-bundle`

Every inbox artifact must carry:
- artifact id
- artifact class
- producer role
- source context
- project or target scope
- status
- required consumers
- routing tags
- evidence refs
- freshness metadata
- validation status
- next expected artifact classes

The inbox protocol must support both:
- human-authored drops
- system-authored artifact emission

The default rule is:
- no direct agent-to-agent action without an inbox artifact or inbox-derived handoff reference
- no plan/analyze/test result remains only in chat text
- every actionable result gets persisted as a governed inbox artifact first

### 2. Routing and delegation model
Add a dedicated runtime routing layer that watches the inbox and determines who should consume each artifact.

Define a first-class runtime role:
- `filesystem-router`

Its responsibilities:
- watch inbox directories and registered ingestion events
- validate artifact envelopes
- classify artifact intent
- map artifacts to governed consumers
- emit `inbox-routing-decision` artifacts
- emit `delegation-bundle` artifacts for downstream roles

The routing model must support:
- single target
- multi-target fanout
- ordered review chain
- blocked routing with exact reasons
- escalation back to the user-facing layer
- checkpoint return to governance triad

Routing decisions must never be implicit. They must be saved as governed artifacts and be reviewable.

### 3. Runtime/front-door role family
Keep the triad exactly as governance:
- `orchestrator-validator`
- `research`
- `architect`

Add explicit runtime/front-door roles:
- `user-facing-agent`
- `spec-interpreter`
- `intake-mapper`
- `semantic-cartographer`
- `filesystem-router`
- `wrapper-synthesizer` as a later-bound runtime consumer, defined now but not deeply activated yet

Required separation rules:
- governance roles must not perform intake conversation work
- runtime roles must not self-certify truth or promotion
- user-facing roles may clarify and represent intent, but may not claim implementation completion
- spec-interpreter may structure meaning, but may not approve the resulting spec
- router may delegate, but may not invent missing evidence
- triad may review and steer, but may not replace the inbox-first artifact flow

### 4. Gatekeeping and routing proof
The first slice should make these things materially real:
- `.plan.md` packet validation
- front matter plus bottom matter parsing
- gate-status evaluation before routing
- blocked routing when gates fail
- role-based routing artifacts
- dual structured plus markdown packet pairing

### 5. Runtime scaffold
This stage introduces only the minimum real scaffold needed to make the inbox protocol truthful:
- Bun/TypeScript app surface for inbox queue and gate-state viewing
- Python watcher and service for packet scanning, validation, and routing
- documented install and start path using Bun plus `uv`

---bottom-matter---
validation_status: "pending_runtime_validation"
status_summary:
  completeness: 0.88
  confidence: high
  doc_state: "governed_inbox_packet"
gate_progress:
  - gate_id: schema_gate
    status: amber
    notes: "Packet follows the governed markdown pattern but awaits the dedicated inbox packet schema."
  - gate_id: scope_gate
    status: green
    notes: "All work remains bounded to the standalone parent repo under meta/."
  - gate_id: consumer_gate
    status: green
    notes: "Required consumers are explicit and start with filesystem-router."
  - gate_id: evidence_gate
    status: green
    notes: "Prompt and governance evidence refs are named in front matter."
  - gate_id: freshness_gate
    status: green
    notes: "The packet is local to the current implementation stage and timestamped."
  - gate_id: readiness_gate
    status: amber
    notes: "Routing depends on the watcher and validator surfaces landing cleanly."
  - gate_id: promotion_gate
    status: amber
    notes: "Promotion waits on schema-backed routing proof and refreshed parent artifacts."
open_questions:
  - "Should later front-door lifecycle packets live at inbox/ root or in inbox/packets/ once the watcher is active?"
pending_validations:
  - "Validate the packet against the dedicated inbox packet schema once added."
  - "Run the inbox watcher and confirm it emits routing and delegation artifacts."
promotion_criteria:
  - "Dedicated inbox packet contracts and schemas validate."
  - "Watcher emits routing decisions for the packet."
  - "Prompt and handoff contracts consume upstream inbox packet refs."
blocked_by:
  - "The routing and packet schemas are not active until the inbox protocol slice lands."
next_iteration:
  owner: "filesystem-router"
  objective: "Validate this packet, emit a routing decision, and hand it to the architect plus orchestrator-validator surfaces."
