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
- scorer: `scripts/score-parent-wrapper.py`
- bounded ratchet runner: `scripts/run-parent-ratchet.sh`
- structured report: `evaluation/copilot-ratchet-report.json`
- iteration ledger: `runs/iterations.jsonl` (one compact JSON object per line)
- latest metrics: `evaluation/metrics-latest.json`
- bounded tool-health evidence: `evaluation/tool-health/status.json`
- parent agent-eval fixture: `evaluation/agent-eval/`

## Parent Tool-Health Doctrine

- GitNexus: use an isolated fixture smoke when validating the mutable parent
  surface; indexing the full repo currently reaches read-only `external/`
  authorities and can surface upstream parse warnings that are outside the kept
  parent slice.
- Graphify: use a bounded parent fixture and `graphify update` for a local
  no-LLM smoke before relying on Graphify output in parent claims.
- InfraNodus: keep the phase-tool doctrine local, but treat live graph analysis
  as API/OAuth-bound unless runtime access is actually configured.
- Vercel agent-eval: use the parent-scoped fixture under `evaluation/agent-eval/`
  and the contract in `contracts/agent-eval-parent-lane.yaml`. In this repo,
  dry is the strongest honest local evidence today; the next bounded smoke lane
  is `scripts/run-parent-agent-eval.sh smoke`, which only needs
  `OPENAI_API_KEY` because the experiment is pinned to Docker.

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
  - "Live InfraNodus analysis remains API/OAuth-bound until local runtime credentials are intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Keep the published parent wrapper and its tool-health evidence aligned."
