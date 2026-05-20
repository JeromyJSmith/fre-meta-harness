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
   - `infranodus-phase-tool-map.json`
   - `external/goal-md/README.md`
   - `external/goal-md/template/GOAL.md`
   - `external/meta-harness/README.md`
   - `external/meta-harness/ONBOARDING.md`
   - `external/autoresearch-mlx/README.md`
   - `external/autoresearch-mlx/program.md`
2. Verify the parent validator runs:
   ```bash
   uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py
   ```
3. Record the baseline:
   ```bash
   uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py --json
   ```

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
- Do not stop after one real cycle unless an exact blocker is proven.
- Do not edit the imported upstream local clones under `external/`.
- Keep `runs/iterations.jsonl` as real JSONL: one compact JSON object per line.
- Do not claim improvement without fresh validation, fresh metrics, and a
  structured report.

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
    notes: "Needs one real non-dry multi-cycle run."

open_questions: []

pending_validations:
  - "Execute the first real non-dry copilot ratchet through this program."

promotion_criteria:
  - "Structured ratchet report exists."
  - "At least 2 real non-dry cycles executed."

blocked_by:
  - "No real copilot-ratchet-report.json yet."

next_iteration:
  owner: "codex"
  objective: "Run Copilot through this local program and emit a real report."
