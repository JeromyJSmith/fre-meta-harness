---
id: "parent-meta-goal"
slug: "parent-meta-goal"
doctype: "goal"
status: "active"
version: "1.1.0"
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
upstream_refs:
  - "external/goal-md/README.md"
  - "external/goal-md/template/GOAL.md"
  - "external/meta-harness/README.md"
  - "external/meta-harness/ONBOARDING.md"
  - "external/autoresearch-mlx/README.md"
  - "external/autoresearch-mlx/program.md"
---

# GOAL.md

## Goal

Improve the parent Meta-Harness wrapper until it becomes a portable,
evidence-backed outer loop that can:

1. identify and govern child body cells
2. carry the reusable contract scaffold
3. carry the governed prompt contract
4. use InfraNodus for diagnosis at every lifecycle gate
5. bind durable evidence to Pixeltable-facing substrate surfaces
6. absorb the local `goal-md`, `meta-harness`, and `autoresearch-mlx` clones
   as live authorities instead of dead references
7. emit measurable improvement artifacts over repeated iterations
8. run a real proposer-evaluator ratchet where the prompt and loop behavior are
   themselves judged by durable evidence
9. measure parent improvement tactics such as docs, MCP, and tool-surface
   changes through an honest agent-eval lane when dry, smoke, or credentialed
   runs are actually available

## Fitness Function

Run this to get the current parent-wrapper score:

```bash
uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py --json
```

### Metric Definition

This is a **split** process score. It does not ask "are files present?" It asks
"did the parent wrapper behave like a real local `goal-md` plus `meta-harness`
plus `autoresearch-mlx` loop, with trustworthy ledger and artifact evidence?"

```text
outcome_score =
  ratchet_execution
+ non_dry_cycle_depth
+ plateau_or_blocker_truth
+ artifact_refresh

instrument_score =
  validator_health
+ report_completeness
+ metric_decision_truth

total_score = 0.75 * outcome_score + 0.25 * instrument_score
```

| Component | Weight | What it measures |
|---|---:|---|
| `ratchet_execution` | 25 | Real non-dry cycles exist in the iteration ledger and agree with the structured report |
| `non_dry_cycle_depth` | 25 | The run executed multiple real non-dry cycles with partial credit before convergence |
| `plateau_or_blocker_truth` | 25 | The run reports an honest continuing, plateau, or blocker state without fake-green stop logic |
| `artifact_refresh` | 25 | Validation, metrics, promotion, and ledger artifacts were refreshed and cross-referenced |
| `validator_health` | 40 | Parent validator passes end-to-end |
| `report_completeness` | 30 | Copilot ratchet report satisfies the schema and carries per-cycle score evidence |
| `metric_decision_truth` | 30 | The run explicitly accepted or repaired the metric with a trustworthy review of the instrument |

### Metric Mutability

- [ ] **Locked**
- [x] **Split**
- [ ] **Open**

The agent may improve the measuring instrument, but it may not silently loosen
the definition of "portable parent wrapper readiness." Instrument repair must
make the score less binary or less gameable, not easier to satisfy.

## Operating Mode

- [x] **Converge**
- [ ] **Continuous**
- [ ] **Supervised**

### Stopping Conditions

Stop and report when ANY of:

- `total_score >= 95`
- `instrument_score < 80` after a proposal attempt
- `2` consecutive real non-dry iterations show no improvement
- InfraNodus comparison, validator, or substrate references become unavailable

## Bootstrap

1. Confirm the active child body in `body-registry.yaml`.
2. Read `domain_spec.md`.
3. Read `library.yaml`, `agent-heavy-run-prompt-schema.md`, and
   `infranodus-phase-tool-map.json`.
4. Read imported upstream authorities:
   - `external/goal-md/README.md`
   - `external/goal-md/template/GOAL.md`
   - `external/meta-harness/README.md`
   - `external/meta-harness/ONBOARDING.md`
   - `external/autoresearch-mlx/README.md`
   - `external/autoresearch-mlx/program.md`
5. Read `program.md`.
6. Run the parent validator:
   ```bash
   uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py
   ```
7. Record the baseline:
   ```bash
   uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py --json
   ```
8. Run the strongest honest bounded parent-layer checks for GitNexus,
   Graphify, and InfraNodus, and capture the result in
   `evaluation/tool-health/status.json`.

## Improvement Loop

The loop follows the imported local authorities directly:

- `goal-md`: explicit fitness function, action catalog, and keep-or-revert loop
- `meta-harness`: explicit `domain_spec.md` and harness-bound search surface
- `autoresearch-mlx`: explicit `program.md`, fixed mutable surface, fixed
  budget, and keep-or-revert discipline

```text
repeat:
  0. Read runs/iterations.jsonl if it exists
  1. Run score-parent-wrapper.py --json > /tmp/parent-before.json
  2. Re-read program.md and the imported local upstream authorities
  3. Read whether the last real Copilot run executed multiple non-dry cycles
  4. If the metric is saturated or untrusted, repair the instrument first
  5. Launch one bounded real Copilot ratchet cycle through program.md
  6. Score from ledger rows and refreshed artifacts, not from self-report alone
  7. Require a structured copilot-ratchet-report.json once the run stops
  7. Run validate_parent_wrapper_contract.py
  8. Run score-parent-wrapper.py --json > /tmp/parent-after.json
  9. If process score improved without truth regressions, keep
  10. If regressed or the stop reason is dishonest, revert or reject
  11. Append iteration evidence to runs/iterations.jsonl
  12. Continue until plateau or exact blocker
```

Commit messages, when this becomes its own repo:

```text
[PARENT:S:NN.N->NN.N] <component>: <bounded change>
```

## Fixed Search Boundary

For the first parent-wrapper ratchet:

- fixed artifact family: parent wrapper contracts and proof-package surfaces
- fixed source authorities: the local clones under `external/`
- fixed metric: `score-parent-wrapper.py`
- fixed budget: one bounded proposal per cycle
- preferred fixed proposer on this Apple Silicon machine:
  - `HARNESS_BACKEND=mlx-lm:prism-ml/Ternary-Bonsai-8B-mlx-2bit`
- allowed alternative proposer surfaces:
  - Claude CLI
  - Codex
  - Copilot

The first loop must not change model, task, metric, and harness shape all at
once.

## Iteration Log

File: `runs/iterations.jsonl`

One JSON object per line:

```jsonl
{"iteration":1,"cycle_kind":"real_non_dry","before_total_score":78.5,"after_total_score":82.0,"before_outcome_score":72.0,"after_outcome_score":78.0,"before_instrument_score":98.0,"after_instrument_score":94.0,"action":"add parent prompt-contract layer","result":"kept","validator_status":"pass","changed_files":["prompts/parent-wrapper-copilot-ratchet.prompt.md"],"artifacts":["evaluation/validation-report.json","evaluation/metrics-latest.json","promotion/readiness.json","runs/iterations.jsonl"],"note":"closed missing prompt-schema gap"}
{"iteration":2,"cycle_kind":"real_non_dry","before_total_score":82.0,"after_total_score":82.0,"before_outcome_score":78.0,"after_outcome_score":78.0,"before_instrument_score":94.0,"after_instrument_score":94.0,"action":"rewrite scaffold prose only","result":"rejected","validator_status":"pass","changed_files":["README.md"],"artifacts":["evaluation/validation-report.json","evaluation/metrics-latest.json","promotion/readiness.json","runs/iterations.jsonl"],"note":"no metric improvement"}
```

## Action Catalog

### `ratchet_execution` (target: 25)

| Action | Impact | How |
|---|---:|---|
| Make Copilot emit the structured ratchet report | +8 | Require `evaluation/copilot-ratchet-report.json` and rerun |
| Force multiple real non-dry cycles | +8 | Ensure the prompt and loop run at least 2 real cycles |
| Add explicit plateau or blocker reasoning | +5 | Require stop reason fields and fresh evidence |

### `report_completeness` (target: 30)

| Action | Impact | How |
|---|---:|---|
| Add missing required report fields | +6 | Expand the Copilot report contract and rerun |
| Refresh fresh artifact references in the report | +4 | Point to validation, metrics, promotion, and iteration outputs |

### `metric_decision_truth` (target: 30)

| Action | Impact | How |
|---|---:|---|
| Make the run explicitly accept or repair the metric | +6 | Add `metric_decision` and `metric_reason` to the report |
| Prevent false max-score convergence | +6 | Require saturation challenge before acceptance |

### `non_dry_cycle_depth` (target: 25)

| Action | Impact | How |
|---|---:|---|
| Force 2 or more real cycles | +8 | Require Copilot to run non-dry ratchet multiple times |
| Record each cycle in iterations.jsonl | +5 | Append one structured entry per real cycle |

### `artifact_refresh` (target: 25)

| Action | Impact | How |
|---|---:|---|
| Refresh validation, metrics, promotion, and gap artifacts after each kept cycle | +8 | Re-run validator and scorer and write outputs |
| Keep report and iteration ledger synchronized | +5 | Ensure artifacts reference the same cycle count |
| Refresh parent tool-health evidence when tool doctrine changes | +4 | Re-run bounded GitNexus, Graphify, InfraNodus, and agent-eval checks honestly |

## Constraints

1. **Do not fake green** — validator, examples, and gap artifacts must support the score.
2. **Do not widen the search space mid-cycle** — keep one bounded proposal per cycle.
3. **Do not modify the score definition and claim outcome improvement in the same cycle** — split mode means instrument work must stay explicit.
4. **Do not remove InfraNodus, prompt-contract, or substrate authority surfaces** — they are load-bearing.
5. **Keep Apple Silicon runs fixed-budget** — the first loop should remain compatible with MLX-backed bounded iterations.

## File Map

| File | Role | Editable? |
|---|---|---|
| `GOAL.md` | Parent fitness function and improvement loop | Yes |
| `domain_spec.md` | Parent onboarding/domain boundary | Yes |
| `program.md` | Parent autoresearch-style execution protocol | Yes |
| `external/goal-md/**` | Imported local `goal-md` authority surface | No |
| `external/meta-harness/**` | Imported local Stanford `meta-harness` authority surface | No |
| `external/autoresearch-mlx/**` | Imported local MLX autoresearch authority surface | No |
| `scripts/score-parent-wrapper.py` | Process scorer for the real Copilot ratchet | Yes |
| `scripts/run-parent-ratchet.sh` | Fixed-budget parent ratchet runner | Yes |
| `prompts/parent-wrapper-copilot-ratchet.prompt.md` | Mutable proposer prompt under evaluation | Yes |
| `evaluation/copilot-ratchet-report.json` | Structured report from the real Copilot run | Written by Copilot only |
| `tests/validate_parent_wrapper_contract.py` | Contract validator | Yes |
| `evaluation/validation-report.json` | Fresh validator evidence | Written by script only |
| `evaluation/infranodus-gap-analysis.json` | Gap-analysis evidence | Yes |
| `promotion/readiness.json` | Promotion readiness evidence | Written by script only |
| `runs/iterations.jsonl` | Iteration history | Appended by script only |

## When to Stop

```text
Starting score: NN.N
Ending score:   NN.N
Iterations:     N
Changes made:   (list)
Remaining gaps: (list)
Next actions:   (what to improve next)
```

---bottom-matter---
status_summary:
  completeness: 1.0
  confidence: high
  doc_state: active_goal

gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Parent goal now includes upstream improvement-loop lineage and local score surfaces."
  - gate_id: registry_gate
    status: green
    notes: "Metrics, loop files, and upstream refs are explicit."
  - gate_id: manifest_gate
    status: green
    notes: "Improvement-layer files are placed in the parent wrapper."
  - gate_id: verification_gate
    status: amber
    notes: "New scorer and ratchet runner still need to be executed after creation."
  - gate_id: state_gate
    status: green
    notes: "State is tied to measurable split scores."
  - gate_id: health_gate
    status: green
    notes: "Improvement layer is no longer missing from the parent wrapper contract."
  - gate_id: promotion_gate
    status: amber
    notes: "Published parent repo exists; promotion now depends on refreshed tool-health and ratchet evidence."

open_questions:
  - "Which fixed proposer should be default for the first standalone parent repo ratchet: MLX Bonsai, Claude CLI, or Codex?"

pending_validations:
  - "Refresh the bounded tool-health evidence after parent-wrapper tool-surface changes."

promotion_criteria:
  - "Parent scorer runs and emits a baseline metrics artifact."
  - "Parent ratchet runner appends iteration evidence."
  - "Parent tool-health evidence remains honest about GitNexus, Graphify, InfraNodus, and agent-eval."

blocked_by:
  - "Live InfraNodus analysis remains API/OAuth-bound until credentials are supplied for a real runtime check."

next_iteration:
  owner: "codex"
  objective: "Execute the published parent score loop with refreshed tool-health evidence and honest evaluator boundaries."
