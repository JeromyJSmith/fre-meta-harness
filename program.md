---
id: "parent-meta-program"
slug: "parent-meta-program"
doctype: "program"
status: "active"
version: "1.0.0"
owner: "fre-meta-harness"
scope: "portable_parent_wrapper"
library_refs:
  - "library.yaml"
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

# program.md

This is the parent-wrapper execution protocol. It is the local adaptation layer
that combines:

- `external/goal-md` for the ruler and keep-or-revert loop
- `external/meta-harness` for the harness-bound domain spec and evaluation frame
- `external/autoresearch-mlx` for the Apple Silicon fixed-budget experiment
  protocol

## Setup

1. Read these local authority files before a real run:
   - `GOAL.md`
   - `domain_spec.md`
   - `library.yaml`
   - `source/parent-operational-doctrine.md`
   - `infranodus-phase-tool-map.json`
   - `external/goal-md/README.md`
   - `external/goal-md/template/GOAL.md`
   - `external/meta-harness/README.md`
   - `external/meta-harness/ONBOARDING.md`
   - `external/autoresearch-mlx/README.md`
   - `external/autoresearch-mlx/program.md`
2. Verify the parent validator runs:
   ```bash
   uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py
   ```
3. Record the baseline:
   ```bash
   uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json
   ```
4. Establish the parent tool-health baseline with the strongest honest bounded
   checks available for:
   - GitNexus
   - Graphify
   - InfraNodus
   - CLI-first local runner harvests
   - Vercel agent-eval when the run is scoped to improvement evaluation, using
     `scripts/run-parent-agent-eval.sh dry` only after the local runner
     harvest, and before any smoke or live exception claim

## Mutable Surface

These are the only parent-wrapper files a ratchet run may change:

- `GOAL.md`
- `domain_spec.md`
- `program.md`
- `library.yaml`
- `agentics-library.md`
- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `MEMORY.md`
- `GOLDENPATH.md`
- `source/**`
- `schemas/**`
- `examples/**`
- `expected-failures/**`
- `tests/**`
- `evaluation/**`
- `promotion/**`
- `prompts/**`
- `runs/**`
- `scripts/**`

The imported local clones under `external/` are read-only authority surfaces.

## Required Loop

LOOP UNTIL plateau or exact blocker:

1. Read `runs/iterations.jsonl`
2. Run the baseline scorer
3. If the metric is saturated or dishonest, repair the instrument first
4. Propose one bounded change inside the mutable parent-wrapper surface
5. Validate:
   - parent validator
   - parent scorer
   - bounded parent tool-health evidence when tool doctrine or invocation paths changed
   - docs sync if shared docs changed
6. If the score improved without truth regressions, keep
7. If the score regressed or the stop reason is dishonest, revert or reject
8. Append a structured row to `runs/iterations.jsonl`
9. Continue until:
   - at least 2 real non-dry cycles executed and
   - 2 consecutive non-improving cycles occurred, or
   - an exact blocker is proven

## Report Contract

Every real run must write:

- `evaluation/copilot-ratchet-report.json`
- `evaluation/tool-health/status.json` when the kept slice changes parent tool
  invocation doctrine or improvement-evaluation guidance
- refresh `source/parent-operational-doctrine.md` when runtime truth, launcher
  truth, or credential-required boundaries change

Required fields:

- `status` (`running` during active loops, `pass` or `blocked` at the final stop)
- `metric_decision`
- `metric_reason`
- `metric_review`
- `real_non_dry_cycles_executed`
- `stop_reason`
- `stop_evidence`
- `score_history`
- `files_changed`
- `artifacts`
- `iteration_ledger_entries_appended`

## Hard Rules

- Use `uv` for Python execution.
- Do not treat a dry run as proof.
- Treat CLI-first local runner harvests as the default parent evaluation path.
- Do not promote the parent agent-eval lane above dry unless the configured
  experiment actually runs; smoke and live are remote-provider exceptions rather
  than the normal parent path.
- Do not stop after one real cycle unless an exact blocker is proven.
- Do not edit the imported upstream local clones under `external/`.
- Keep `runs/iterations.jsonl` as real JSONL: one compact JSON object per line.
- Do not claim improvement without fresh validation, fresh metrics, and a
  structured report.
- Living docs must be refreshed when truth changes, but doc-only edits do not
  count as improvement evidence in the scorer.
- Treat live API-backed tool lanes as blocked until runtime access is actually
  configured; prefer dry, smoke, or fixture-bound checks over fake-green claims.

---bottom-matter---
status_summary:
  completeness: 0.98
  confidence: high
  doc_state: active_program

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Program starts from imported local upstream authorities."
  - gate_id: registry_gate
    status: green
    notes: "Mutable and read-only authority surfaces are split."
  - gate_id: manifest_gate
    status: green
    notes: "Execution and report contracts are placed at the parent root."
  - gate_id: verification_gate
    status: green
    notes: "Program requires validator and scorer on every kept cycle."
  - gate_id: state_gate
    status: green
    notes: "Stop conditions are explicit and bounded."
  - gate_id: health_gate
    status: green
    notes: "No clone is treated as a citation-only source anymore."
  - gate_id: promotion_gate
    status: amber
    notes: "Needs refreshed multi-cycle evidence tied to current tool-health doctrine."

open_questions: []

pending_validations:
  - "Refresh the current multi-cycle ratchet evidence with the parent tool-health lane."

promotion_criteria:
  - "Structured ratchet report exists."
  - "At least 2 real non-dry cycles executed."

blocked_by:
  - "Live InfraNodus MCP analysis remains optional; the bounded local parent-layer substitute is the default until runtime access is intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Run Copilot through this local program, refresh tool-health evidence, and emit a real report."
