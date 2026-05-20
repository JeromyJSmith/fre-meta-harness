# Domain Spec: FRE Meta Harness Wrapper

## Domain Summary

The target domain is the portable parent Meta-Harness wrapper that sits above a
child implementation repo and governs:

- scaffold contracts
- governed prompt contracts
- InfraNodus comparison doctrine
- Pixeltable substrate doctrine
- proof-package surfaces
- promotion readiness

Unit of evaluation: one bounded parent-wrapper improvement cycle.

Fixed for the first pass:

- parent wrapper root at `/Volumes/PixelTable/VW_iTwin_Bridge/meta`
- child body registry entry for `body.vw_itwin_bridge`
- governed prompt contract shape
- seven-gate lifecycle
- seven-part proof package
- imported local authorities under `external/goal-md`,
  `external/meta-harness`, and `external/autoresearch-mlx`

Allowed to change:

- parent wrapper docs and contracts
- scoring and ratchet scripts
- validation and promotion evidence surfaces

Out of scope:

- broad child-repo feature work
- changing the meaning of readiness while claiming improvement
- changing model, metric, and harness shape in the same first loop

## Harness And Search Plan

Candidate harness shape:

```text
meta/
  scaffold/
  source/
  schemas/
  examples/
  expected-failures/
  tests/
  evaluation/
  promotion/
  scripts/
  runs/
  external/
```

Every candidate cycle must:

- run the parent validator
- run the parent scorer
- preserve iteration evidence
- keep or revert based on score
- preserve the imported local upstream clones as read-only authorities

## Evaluation Plan

Search-set evaluation:

- parent contract validation pass
- parent score calculation
- InfraNodus gap-artifact alignment
- local-upstream-authority alignment against the cloned `goal-md`,
  `meta-harness`, and `autoresearch-mlx` surfaces

Held-out evaluation:

- replay inside the future standalone `fre-meta-harness` repo

Primary metric:

- `total_score` from `scripts/score-parent-wrapper.py`

Secondary metrics:

- `outcome_score`
- `instrument_score`
- changed-file count
- unresolved blockers
- iteration count without improvement
- real non-dry cycle count

## Experience And Logging

Store per cycle:

- before and after scores
- weakest component
- action taken
- keep or revert decision
- validator report path
- promotion readiness path

Iteration log:

- `runs/iterations.jsonl`
- `evaluation/copilot-ratchet-report.json`

## Open Questions And Unknowns

- Which fixed proposer should be default for the first standalone parent repo loop?
- Should the standalone repo keep root-level contracts exactly or shift some into subdirectories?
