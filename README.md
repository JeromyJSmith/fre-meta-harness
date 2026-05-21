---
id: "parent-meta-readme"
slug: "parent-meta-readme"
doctype: "readme"
status: "active"
version: "1.0.0"
owner: "fre-meta-harness"
scope: "portable_parent_wrapper"
library_refs:
  - "library.yaml"
program_refs:
  - "program.md"
prompt_contract_refs:
  - "agent-heavy-run-prompt-index.md"
  - "agent-heavy-run-prompt-schema.md"
  - "agent-heavy-run-prompt.schema.json"
  - "agent-heavy-run-prompt.template.yaml"
  - "architect-review-handoff-prompt-schema.md"
  - "architect-review-handoff-prompt.schema.json"
  - "architect-review-handoff-prompt.template.yaml"
  - "copilot-prompting-playbook.md"
comparison_refs:
  - "infranodus-phase-tool-map.json"
substrate_refs:
  - "pixeltable-operational-substrate.md"
upstream_local_refs:
  - "external/goal-md"
  - "external/meta-harness"
  - "external/autoresearch-mlx"
---

# FRE Meta Harness

This directory is the published portable outer wrapper for the
`VW_iTwin_Bridge` body cell. It is the standalone `fre-meta-harness` parent
repository root.

## What Lives Here

- fractal scaffold:
  - `README.md`
  - `AGENTS.md`
  - `CLAUDE.md`
  - `GOAL.md`
  - `GOLDENPATH.md`
  - `MEMORY.md`
- library and configuration:
  - `library.yaml`
  - `agentics-library.md`
  - `pixeltable-operational-substrate.md`
- imported upstream authorities:
  - `external/goal-md/`
  - `external/meta-harness/`
  - `external/autoresearch-mlx/`
- governed prompt contract:
  - `agent-heavy-run-prompt-index.md`
  - `agent-heavy-run-prompt-schema.md`
  - `agent-heavy-run-prompt.schema.json`
  - `agent-heavy-run-prompt.template.yaml`
  - `architect-review-handoff-prompt-schema.md`
  - `architect-review-handoff-prompt.schema.json`
  - `architect-review-handoff-prompt.template.yaml`
  - `copilot-prompting-playbook.md`
- ratchet execution protocol:
  - `program.md`
- comparison engine map:
  - `infranodus-phase-tool-map.json`
- seven-part proof package:
  - `source/`
  - `schemas/`
  - `examples/`
  - `expected-failures/`
  - `tests/`
  - `evaluation/`
  - `promotion/`

## Clone And Bootstrap

Clone with submodules so the imported upstream authorities are present locally:

```bash
git clone --recurse-submodules git@github.com:JeromyJSmith/fre-meta-harness.git
```

## Current Role

This wrapper:

- identifies the active child body
- carries reusable wrapper doctrine
- carries local imported upstream authorities under `external/`
- carries the governed prompt schema
- carries the MLX-style execution protocol in `program.md`
- carries the InfraNodus full-phase map
- carries Pixeltable substrate doctrine
- carries a `goal-md` style improvement loop with metrics and iteration logs
- emits durable validation and readiness artifacts

## Improvement Layer

- goal contract: `GOAL.md`
- onboarding/domain boundary: `domain_spec.md`
- execution protocol: `program.md`
- reusable metrics contract: `contracts/parent-capability-metrics.yaml`
- parent-native orchestration contracts:
  - `contracts/research-packet-manifest.yaml`
  - `contracts/peer-mesh.yaml`
  - `contracts/peer-message.yaml`
  - `contracts/peer-lifecycle.yaml`
  - `contracts/observability-event.yaml`
  - `contracts/observability-ingest.yaml`
  - `contracts/policy-decision.yaml`
  - `contracts/library-distribution.yaml`
  - `contracts/benchmark-emission.yaml`
  - `contracts/peer-mesh-runtime.yaml`
  - `contracts/agent-role-contract.yaml`
  - `contracts/hook-manifest.yaml`
  - `contracts/capability-matrix.yaml`
- Phase 1 communication slice truth:
  - peer-mesh primitives are explicit at the contract layer (`list_agents`,
    `send_command`, `send_prompt`, `await_response`)
  - runtime roles are validated by role classes and coverage invariants instead of
    a closed-world fixed ID list
  - prompt and command delivery both require policy plus observability guards
- Phase 2 observability-distribution-evaluation slice truth:
  - observability is routed through a decoupled ingest plane with explicit session
    start or end, correlation, swimlane, and durable-store expectations
  - typed library units propagate by reference across same-host and cross-device
    peers instead of copy-first workflow assumptions
  - peer-mesh changes are measured through emitted benchmark tuples and required
    regression groups across runs
- Research governance slice truth:
  - the packetized harvest under `evaluation/research/` is now governed through
    `contracts/research-packet-manifest.yaml`
  - `contracts/capability-matrix.yaml` now aligns to the compiled feature matrix
    instead of a narrower hand-curated subset
  - compiled capability harvest, feature matrix, gap placement map, and source
    index are validator-backed authoritative views rather than loose artifacts
- scorer: `scripts/score-parent-wrapper.py`
- CLI-first local runner harvest: `scripts/harvest-local-runner-capabilities.py`
- bounded ratchet runner: `scripts/run-parent-ratchet.sh`
- bounded InfraNodus substitute: `scripts/build-parent-infranodus-artifacts.py`
- structured report: `evaluation/copilot-ratchet-report.json`
  - now required to carry structured runtime truth, blocked lanes, freshness,
    command evidence, and score-saturation explanation for runtime-facing kept
    slices
- iteration ledger: `runs/iterations.jsonl` (one compact JSON object per line)
- latest metrics: `evaluation/metrics-latest.json`
- bounded tool-health evidence: `evaluation/tool-health/status.json`
- bounded same-host peer-mesh runtime proof: `scripts/run-parent-peer-mesh-local.sh`
- same-host peer-mesh evidence:
  - `evaluation/tool-health/peer-mesh-local.json`
  - `evaluation/tool-health/peer-mesh-local.log`
  - `evaluation/tool-health/peer-mesh-local-events.jsonl`
- local runner availability matrix: `evaluation/tool-health/local-runners.json`
- parent agent-eval fixture: `evaluation/agent-eval/`

## Parent Tool-Health Doctrine

- GitNexus: use an isolated fixture smoke when validating the mutable parent
  surface; indexing the full repo currently reaches read-only `external/`
  authorities and can surface upstream parse warnings that are outside the kept
  parent slice.
- Graphify: use a bounded parent fixture and `graphify update` for a local
  no-LLM smoke before relying on Graphify output in parent claims.
- Local runners: treat CLI-first local harvests as the baseline parent
  evaluation path and report missing runners explicitly instead of assuming any
  paid-provider fallback.
- Peer mesh runtime: same-host is the first active runtime lane and must be
  proven through the bounded local peer-mesh runner plus observability evidence;
  cross-device remains blocked until authenticated transport is really present.
- InfraNodus: keep the phase-tool doctrine local and prefer the bounded local
  parent-layer substitute when live MCP graph analysis is not actually
  configured.
- Vercel agent-eval: use the parent-scoped fixture under `evaluation/agent-eval/`
  and the contract in `contracts/agent-eval-parent-lane.yaml`. In this repo,
  dry is the strongest honest lane-specific local evidence today. Smoke and
  live remain exact remote-provider exceptions, so the default parent path is
  the CLI-first local runner harvest plus dry agent-eval, not
  `OPENAI_API_KEY`.

## Acknowledgments

This harness was shaped in part by the examples, teaching, and inspiration from:

- Disler — https://github.com/disler
- IndyDevDan — https://www.youtube.com/@IndyDevDan

---bottom-matter---
status_summary:
  completeness: 1.0
  confidence: high
  doc_state: active_readme

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Parent wrapper surfaces and imported upstream authorities are enumerated."
  - gate_id: registry_gate
    status: green
    notes: "Canonical parent authority files and local clones are named."
  - gate_id: manifest_gate
    status: green
    notes: "Seven-part proof package is placed at the parent root."
  - gate_id: verification_gate
    status: green
    notes: "Validator and readiness artifacts exist."
  - gate_id: state_gate
    status: green
    notes: "Parent role is explicit and bounded."
  - gate_id: health_gate
    status: green
    notes: "README now points at missing formerly-unwired surfaces."
  - gate_id: promotion_gate
    status: green
    notes: "Standalone fre-meta-harness repo is initialized and published."

open_questions: []

pending_validations:
  - "Refresh the parent tool-health evidence after changes to GitNexus, Graphify, InfraNodus, or agent-eval lanes."

promotion_criteria:
  - "README remains aligned after transport into standalone repo."

blocked_by:
  - "Live InfraNodus MCP analysis remains optional; the bounded local parent-layer substitute is the default until runtime access is intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Keep the published parent wrapper and its tool-health evidence aligned."
