---
id: "parent-red-green-pipeline"
doctype: "pipeline_map"
status: "active"
version: "1.0.0"
scope: "portable_parent_wrapper"
generated_at: "2026-05-22"
authority:
  - contracts/subsystem-runner-proof-family.yaml
  - contracts/subsystem-bounded-probe.yaml
  - contracts/subsystem-observability-handshake.yaml
  - contracts/contract-to-runner-map.yaml
  - contracts/peer-lifecycle.yaml
  - contracts/peer-mesh-runtime.yaml
  - contracts/peer-mesh.yaml
  - contracts/hook-manifest.yaml
  - contracts/observability-event.yaml
  - contracts/observability-ingest.yaml
  - contracts/policy-decision.yaml
  - contracts/benchmark-emission.yaml
  - contracts/three-agent-topology.yaml
  - contracts/front-door-runtime-topology.yaml
  - contracts/inbox-packet.yaml
  - contracts/inbox-routing-decision.yaml
  - contracts/delegation-bundle.yaml
  - contracts/gap-map-strength.yaml
  - contracts/capability-matrix.yaml
  - contracts/research-packet-manifest.yaml
  - contracts/tool-packaging-family.yaml
  - contracts/agent-eval-parent-lane.yaml
  - contracts/parent-capability-metrics.yaml
  - contracts/recursive-documentation-bundle.yaml
  - contracts/subsystem-registry.yaml
  - contracts/subsystem-harness-topology.yaml
  - contracts/agent-role-contract.yaml
  - contracts/hook-manifest.yaml
  - contracts/library-distribution.yaml
---

# RED → GREEN: The Real Pipeline

This is the actual multi-phase proof-state pipeline derived from ALL contracts.
Not "things broken → things working." A formal chain of proof states, artifact
gates, lifecycle events, and benchmark emissions that must all resolve in order.

---

## PROOF STATE VOCABULARY (from subsystem-runner-proof-family.yaml)

Each subsystem moves through these states — in order, no skipping:

```
designed_not_activated
       │
       ▼  bounded probe executed + observability artifacts emitted
bounded_probe_pass
       │
       ▼  subsystem-specific probe + observability handshake + tool-health evidence
activation_proven_same_host
```

`bounded_probe_blocked` is a lateral state — exact prerequisite missing and
documented. Not a step forward.

**Current state of all 4 subsystems: `designed_not_activated`**
Required evidence for each: `evaluation/subsystem-runner-probes/{id}/probe-status.json`,
`events.jsonl`, `benchmarks.json`.

---

## PHASE 0 — GOVERNANCE PRE-FLIGHT

**Before any work proceeds, every inbox packet must pass 6 gates.**
Source: `contracts/inbox-packet.yaml` → `completion_boundary.required_gate_ids`

```
┌─────────────────────────────────────────────────────────────┐
│  INBOX PACKET GATE CHAIN                                    │
│                                                             │
│  [schema_gate]    front-matter + bottom-matter valid        │
│       ↓                                                     │
│  [scope_gate]     parent_only = true, scope matches         │
│       ↓                                                     │
│  [consumer_gate]  required_consumers named + reachable      │
│       ↓                                                     │
│  [evidence_gate]  structured_contract_ref + artifact_ref    │
│       ↓                                                     │
│  [freshness_gate] timestamps current, not stale             │
│       ↓                                                     │
│  [readiness_gate] all above green, delegation_bundle_ref    │
│                   exists                                    │
└─────────────────────────────────────────────────────────────┘
```

After ALL 6 gates pass → inbox-routing-decision.yaml is emitted →
delegation-bundle.yaml is emitted → front-door runtime receives routed work.

Routing requires 3+ options (decision_space minimum). Triad bypass is forbidden.
Direct agent-to-agent without inbox is forbidden.

---

## PHASE 1 — INGRESS LANES (front-door-runtime-topology.yaml)

Four ingress lanes, each with its own contract chain:

```
conversation_capture  →  inbox-packet  →  inbox-routing-decision
                         user-facing-agent, spec-interpreter

governed_inbox        →  inbox-packet  →  inbox-routing-decision  →  delegation-bundle
                         filesystem-router

triad_review          →  inbox-routing-decision  →  delegation-bundle
                         orchestrator-validator, research, architect

routed_delegation     →  delegation-bundle  →  recursive-documentation-bundle
                         ALL 6 front-door runtime roles
```

Separation rules (hard — not optional):
- Governance roles cannot originate conversational packets.
- Runtime roles cannot self-promote governance.
- Router cannot invent missing evidence.
- Triad bypass forbidden.
- Recursive documentation required.
- Explicit packet pairing required.

---

## PHASE 2 — THREE-AGENT GOVERNANCE LOOP

Each triad dispatch requires ALL of the following artifacts:
Source: `contracts/three-agent-topology.yaml` + `validation_gates`

```
┌──────────────────────────────────────────────────┐
│  TRIAD DISPATCH CHECKLIST (per governed slice)   │
│                                                  │
│  [ ] decision_space — 3+ options, 1 recommended  │
│  [ ] dispatch_message — explicit target + obj    │
│  [ ] markdown_companion — human-readable         │
│  [ ] machine_truth_stays_structured — YAML/JSON  │
│  [ ] extension_request (if new capability needed)│
└──────────────────────────────────────────────────┘
```

Role dispatch flow:
```
orchestrator-validator ←→ research ←→ architect
        ↑___________________________________|
```
All three can route to any other. No one role is terminal.
Extension requests route through `contracts/agent-extension-request.yaml` only.

---

## PHASE 3 — PEER MESH LIFECYCLE (peer-lifecycle.yaml)

Per message, the full lifecycle must complete:

```
bootstrapping
     │ session_start
     ▼
   ready ◄──────────────── retry_requested
     │ message_dispatch              │
     ▼                               │
awaiting_response ─────────────────►│
     │ response_received
     ▼
verifying_completion
     │ verification_passed        verification_failed
     ▼                               ▼
 completed                        blocked
```

Terminal states: `completed` OR `blocked`. No ambiguous completion allowed.
Required completion tokens: `done` | `failed` | `needs-human`
Loop budget: max 8 per scenario. Retry budget: max 2 per message.
Fail mode: `fail_loud`.

---

## PHASE 4 — HOOK EXECUTION (hook-manifest.yaml)

Five hooks, each with required capabilities and fail_loud on failure:

```
peer-session-start       → session_start event
  requires: pi-vs-claude-code, the-library
  validates: mesh transport, role registry, bootstrap evidence
  ↓
peer-membership-refresh  → peer_join event
  requires: pi-vs-claude-code, the-library
  validates: role package, capability mapping
  ↓
peer-prompt-guard        → before_send_prompt
  requires: claude-code-hooks-mastery, multi-agent-observability
  outcomes: allow | block | ask
  ↓
peer-command-guard       → before_send_command
  requires: claude-code-hooks-mastery, agent-sandbox-skill
  outcomes: allow | block | ask
  ↓
completion-verification  → response_complete
  requires: hooks-mastery, multi-agent-observability, agent-sandbox-skill
  outcomes: allow | block | ask
  validates: completion token, loop-budget, PII-safe closure
```

---

## PHASE 5 — OBSERVABILITY + POLICY EVENTS (observability-event.yaml + policy-decision.yaml)

Every governed operation must emit events to the durable sink (Pixeltable):

**Required event types per session:**
```
peer_session_started    ─ lifecycle
peer_session_ended      ─ lifecycle
peer_joined             ─ lifecycle
peer_message_sent       ─ messaging
peer_message_received   ─ messaging
peer_response_completed ─ messaging
policy_decision_emitted ─ policy
```

**Policy decision record required fields:**
`decision_id`, `message_id`, `correlation_id`, `scenario_id`, `outcome`,
`reason`, `actor_role`

Outcome vocabulary: `allow` | `block` | `ask`
- `allow` requires observability event emission.
- `block` is terminal, no retry.
- `ask` routes to `mesh_verifier`.
- PII/secrets in prod→dev path require redaction before allow.

Durable sink: `pixeltable` (currently `blocked_not_activated`).
Correlation keys: `message_id`, `correlation_id`, `scenario_id`.

---

## PHASE 6 — SUBSYSTEM PROBE EXECUTION

Per subsystem, in order: `intake_etl` → `research_harvest` →
`semantic_cartography` → `wrapper_synthesizer` (gated last).

Each probe must emit this exact artifact set before proof state advances:

```
evaluation/subsystem-runner-probes/{subsystem_id}/
  probe-status.json       ← subsystem_probe_status class
  events.jsonl            ← subsystem_probe_events class
  benchmarks.json         ← subsystem_probe_benchmarks class

evaluation/validation-report.json   ← refreshed
evaluation/metrics-latest.json      ← refreshed
```

Required observability handshake event sequence per probe:
```
probe_started → evidence_recorded → validation_refreshed
```

Required validation commands run after each probe:
```bash
uv run --isolated --with jsonschema --with pyyaml \
  python tests/validate_parent_wrapper_contract.py

uv run --isolated --with jsonschema --with pyyaml \
  python scripts/score-parent-wrapper.py --json
```

Required graph analysis command after semantic_cartography probe:
```bash
uv run python scripts/build-parent-infranodus-artifacts.py
```

### intake_etl probe design (designed_not_activated → bounded_probe_pass)
```
probe mode: inbox_fixture_reconciliation
planned inputs:
  - contracts/inbox-packet.yaml
  - any fixture packet in inbox/
planned outputs:
  - evaluation/subsystem-runner-probes/intake_etl/probe-status.json
  - evaluation/subsystem-runner-probes/intake_etl/events.jsonl
blocker: No intake_etl runner harness exists yet.
```

### research_harvest probe design (designed_not_activated → bounded_probe_pass)
```
probe mode: compiled_output_reconciliation
planned inputs:
  - evaluation/research/compiled/capability-harvest.json
  - contracts/research-packet-manifest.yaml
planned outputs:
  - evaluation/subsystem-runner-probes/research_harvest/probe-status.json
  - evaluation/subsystem-runner-probes/research_harvest/events.jsonl
blocker: No research_harvest runner harness exists yet.
```

### semantic_cartography probe design (designed_not_activated → bounded_probe_pass)
```
probe mode: graph_boundary_reconciliation
planned inputs:
  - evaluation/infranodus-gap-analysis.json
  - evaluation/infranodus-conceptual-bridges.json
planned outputs:
  - evaluation/subsystem-runner-probes/semantic_cartography/probe-status.json
  - evaluation/subsystem-runner-probes/semantic_cartography/events.jsonl
blocker: No semantic_cartography runner harness exists yet.
         Live InfraNodus must remain blocked unless auth proof exists separately.
```

### wrapper_synthesizer probe design (late_bound_not_activated → bounded_probe_pass)
```
probe mode: handoff_bundle_reconciliation
planned inputs:
  - contracts/delegation-bundle.yaml
  - source/subsystems/registry.json
GATE: Requires explicit triad review + named downstream runtime owner FIRST.
blocker: No downstream runtime owner named yet.
```

---

## PHASE 7 — GAP-MAP-STRENGTH ANALYSIS (gap-map-strength.yaml)

After each probe, a gap-map-strength report must cover ALL 11 required sections:

```
selected_slice          what slice was run and why
infranodus_path         InfraNodus graph path used or local substitute
strong_content          ≥4 areas: governance_kernel, same_host_runtime_truth,
                        compiled_research_baseline, subsystem_architecture_truth
weak_content            ≥4 missing classes: better_source_material, better_schema,
                        better_observability, better_tool_probe
workflow_structure      workflow_edge_map, contract_to_runner_map, evidence_strength_map
runnable_tools          ≥6 tools across: gap_mapping, graph_extraction, etl_structuring,
                        semantic_cartography, observability, spec_compilation
exact_blockers          exact dependency + exact artifact path per blocker
freshness               timestamps, last-run dates, stale artifact detection
score_saturation        comparison vs prior run, plateau or regression flag
command_evidence        exact commands + expected artifact paths per claim
follow_up_prompt        structured prompt pointing to agent-heavy-run-prompt.schema.json
targeted_validation     specific validation results with pass/fail per contract surface
```

---

## PHASE 8 — BENCHMARK EMISSION (benchmark-emission.yaml)

After each improvement cycle, three required benchmark groups must emit:

```
peer_mesh_regression    ─ regression detection across peer mesh changes
observability_ingest    ─ event emission and ingest completeness
library_distribution    ─ library reference resolution and distribution
```

Emits to:
```
evaluation/metrics-latest.json    ← append + compare
evaluation/validation-report.json ← refresh
promotion/readiness.json          ← update
runs/iterations.jsonl             ← append record
```

Benchmark tuple required fields:
`benchmark_id`, `benchmark_group`, `contract_surface`, `scenario_id`,
`run_ref`, `status`, `measurement_ref`

Regression signal fields: `baseline_run_ref`, `candidate_run_ref`,
`delta_summary`, `regression_detected`

---

## PHASE 9 — TOOL PACKAGING (tool-packaging-family.yaml)

Each tool that the parent wraps must pass through the packaging gate:

```
tool-spec              ─ named endpoint, input schema, output schema, artifact class
agent-card             ─ /.well-known/agent.json (discovery endpoint)
tool-task              ─ task state machine
tool-artifact          ─ artifact registry linkage
tool-packaging-family  ─ family binding all four
```

Task state machine (allowed_task_states):
```
queued → running → succeeded
                 → failed
                 → blocked
                 → cancelled
```

Required endpoints (not yet wired):
```
/.well-known/agent.json              ← discovery
/v1/tools/{toolId}/tasks             ← task create
/v1/tasks/{taskId}                   ← task status
/v1/tasks/{taskId}/artifacts         ← task artifacts
```

Storage truth:
- Filesystem registry: REQUIRED
- Pixeltable sync: `blocked_not_activated` ← exact blocker, needs activation slice
- DuckDB query surface: `planned_not_activated` ← explicit, not implied

---

## PHASE 10 — CAPABILITY METRICS SCORING (parent-capability-metrics.yaml)

Each kept cycle is scored against 4+ metric families:

| Metric | Unit | Passing Rule | Anti-gaming |
|--------|------|--------------|-------------|
| `documentation_quality` | 0–5 | ≥4, canonical command + artifact paths present | Docs alone max 1/5 |
| `execution_success` | boolean | exit 0 + expected artifacts exist | Planned commands = 0 |
| `validation_pass_rate` | 0–1 ratio | 1.0 for kept cycle + last kept run | Skipped checks = fail |
| `tool_health_availability` | ... | tool-health/status.json updated | Stale = fail |

Freshness window: 7 days. Regression window: last 3 runs.
Docs-only maximum score: 1 across all metrics.
Behavior required: no fake-green on doc edits alone.

---

## PHASE 11 — AGENT EVAL (agent-eval-parent-lane.yaml)

Three levels:

```
dry   ─ DONE (evaluation/tool-health/agent-eval-dry.log)
        Discovers experiment without API calls. No credentials needed.

smoke ─ BLOCKED (needs OPENAI_API_KEY + Docker)
        One Codex run against parent-wrapper boundary fixture.
        Required artifacts: evaluation/tool-health/agent-eval-smoke.log
                           evaluation/agent-eval/results/

live  ─ FUTURE (needs: OPENAI_API_KEY + Docker + a kept parent change)
        Repeatable non-dry runs with durable comparison artifacts.
```

---

## PHASE 12 — PROMOTION (benchmark-emission.yaml + capability-matrix.yaml)

Promotion is NOT a state flip. It requires ALL of:

```
[ ] promotion/readiness.json updated with current evidence
[ ] evaluation/validation-report.json passing (1.0 ratio)
[ ] evaluation/metrics-latest.json showing non-regression
[ ] runs/iterations.jsonl contains at least one non-dry kept cycle
[ ] All 4 subsystem probes at bounded_probe_pass or higher
[ ] No blocked_by fields unresolved
[ ] Gap-map-strength report 11 sections complete
[ ] Benchmark groups: peer_mesh_regression, observability_ingest, library_distribution
[ ] tool-health/status.json freshness ≤7 days
[ ] Parent validator passes end-to-end
```

---

## CURRENT STATUS vs FULL PIPELINE

```
PHASE 0  Inbox gate chain          YELLOW  Gates defined, no live project packet yet
PHASE 1  Ingress lanes             GREEN   Same-host active (inbox_protocol.same_host)
PHASE 2  Triad governance loop     GREEN   three-agent-topology.yaml active, prompts exist
PHASE 3  Peer mesh lifecycle       GREEN   same_host bounded_pass (evaluation/tool-health/peer-mesh-local.json)
                                   RED     cross_device BLOCKED (PI_COMS_NET_AUTH_TOKEN missing)
PHASE 4  Hook execution            YELLOW  Hooks defined in hook-manifest.yaml
                                   RED     No live hook adapter running against Claude Code lifecycle
PHASE 5  Observability + Policy    YELLOW  Events emitted in peer-mesh-local-events.jsonl
                                   RED     Pixeltable sink blocked_not_activated
                                   RED     No live policy-decision records emitting
PHASE 6  Subsystem probes          RED     ALL 4 at designed_not_activated
                                           Missing: evaluation/subsystem-runner-probes/{id}/*
PHASE 7  Gap-map-strength          YELLOW  Report exists but does not yet cover all 11 sections
PHASE 8  Benchmark emission        YELLOW  metrics-latest.json + validation-report.json exist
                                   RED     No benchmark tuple records for the 3 required groups
PHASE 9  Tool packaging            RED     agent.json not wired
                                   RED     /v1/tools + /v1/tasks endpoints not wired
                                   RED     Pixeltable sync blocked_not_activated
PHASE 10 Capability metrics        YELLOW  Scorer runs, metrics-latest.json exists
                                   RED     validation_pass_rate depends on Phase 6 probes
PHASE 11 Agent eval                GREEN   dry pass
                                   BLOCKED smoke (OPENAI_API_KEY)
PHASE 12 Promotion                 RED     Blocked by Phases 6, 7, 8, 9
```

---

## THE ACTUAL NEXT STEPS (in contract-defined order)

### Step 1 — Build subsystem probe harnesses (Phase 6, sequentially)
Write three runner scripts, one per non-gated subsystem:

**`scripts/run-intake-etl-probe.sh`**
- Takes a fixture inbox packet as input
- Calls `scripts/watchers/inbox_router.py` then normalizes output
- Writes `evaluation/subsystem-runner-probes/intake_etl/probe-status.json`
- Emits `events.jsonl` with: `probe_started`, `evidence_recorded`, `validation_refreshed`
- Writes `benchmarks.json`
- Runs validator + scorer after

**`scripts/run-research-harvest-probe.sh`**
- Calls `scripts/ingest-consume-sources.py` + `scripts/compile-operational-feature-matrix.py`
- Reconciles against `contracts/research-packet-manifest.yaml`
- Writes `evaluation/subsystem-runner-probes/research_harvest/probe-status.json`
- Emits events + benchmarks
- Runs validator + scorer

**`scripts/run-semantic-cartography-probe.sh`**
- Runs InfraNodus analysis via `scripts/build-parent-infranodus-artifacts.py`
- Reconciles gaps against `contracts/gap-map-strength.yaml` required sections
- Writes `evaluation/subsystem-runner-probes/semantic_cartography/probe-status.json`
- Emits events + benchmarks
- Runs validator + scorer

### Step 2 — Wire hook adapter (Phase 4)
The five hooks in `hook-manifest.yaml` need a live adapter against Claude Code's
PreToolUse / PostToolUse / Stop lifecycle. Currently doctrine only.

### Step 3 — Wire benchmark emission (Phase 8)
After each probe, emit benchmark tuples for the three required groups into
`evaluation/metrics-latest.json` and append to `runs/iterations.jsonl`.

### Step 4 — Wire tool packaging endpoints (Phase 9)
`app/server.ts` needs:
- `/.well-known/agent.json`
- `/v1/tools/{toolId}/tasks`
- `/v1/tasks/{taskId}`
- `/v1/tasks/{taskId}/artifacts`

### Step 5 — Activate Pixeltable observation sink (Phases 5, 9)
`pixeltable_sync_status: blocked_not_activated` → needs its own activation slice
with exact proof artifacts. This is the Pixeltable persistence contract.

### Step 6 — wrapper_synthesizer (Phase 6, gated last)
Only after Steps 1–3 produce their proof artifacts AND triad issues a
delegation-bundle naming a downstream runtime owner.

---
bottom-matter:
  status_summary:
    completeness: 1.0
    confidence: high
    doc_state: active_pipeline_map
  generated_from: all 31 contracts in contracts/
  current_git: a57cfb6
