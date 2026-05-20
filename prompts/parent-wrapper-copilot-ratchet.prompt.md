# Parent Wrapper Copilot Ratchet Prompt

Treat this as one continuous autonomous heavy run on the parent Meta-Harness
wrapper only.

Mission:

- run a real non-dry parent-wrapper ratchet
- validate everything
- challenge the metric if it is saturated or too binary
- keep looping until genuine plateau or an exact blocker
- implement the loop using the local imported authorities under `external/`

Current verified state:

- parent wrapper root: `/Volumes/PixelTable/VW_iTwin_Bridge/meta`
- scaffold exists: `README.md`, `AGENTS.md`, `CLAUDE.md`, `GOAL.md`,
  `GOLDENPATH.md`, `MEMORY.md`
- governed prompt contract exists
- InfraNodus phase-tool map exists
- local imported authority clones exist under:
  - `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/goal-md`
  - `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/meta-harness`
  - `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/autoresearch-mlx`
- parent validator currently passes
- current parent score is low because there is no real
  `evaluation/copilot-ratchet-report.json` yet
- promotion is correctly blocked until a real multi-cycle report exists

Hard rules:

- use `uv` for all Python execution
- do not broaden beyond `/Volumes/PixelTable/VW_iTwin_Bridge/meta`
- do not use a dry run as proof
- do not stop after one real cycle unless an exact blocker is proven
- if the score is saturated or gameable, treat that as an instrument problem
  and repair the scorer first
- do not edit the imported local authority clones under
  `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external`
- no fake green states

Read first:

- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/GOAL.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/program.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/domain_spec.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/library.yaml`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/agent-heavy-run-prompt-schema.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/infranodus-phase-tool-map.json`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/README.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/goal-md/README.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/goal-md/template/GOAL.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/meta-harness/README.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/meta-harness/ONBOARDING.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/autoresearch-mlx/README.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/external/autoresearch-mlx/program.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py`

Tasks:

1. Capture the true baseline by running the validator and scorer.
2. Decide whether the current metric is trustworthy. If not, improve the
   metric first by following the imported local `goal-md` ruler pattern.
3. Treat `external/meta-harness/ONBOARDING.md` as the search-boundary contract:
   fixed domain, fixed harness, bounded mutable surface.
4. Treat `external/autoresearch-mlx/program.md` as the keep-or-revert protocol:
   fixed budget, report, keep if improved, revert if not.
5. Run at least 2 real non-dry ratchet cycles once the metric is trustworthy.
6. Write `/Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/copilot-ratchet-report.json` with:
   - `status`
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
7. Stop only after 2 consecutive non-improving real cycles with a trustworthy
   metric, or after proving an exact blocker.
8. Refresh:
   - `/Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/validation-report.json`
   - `/Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/metrics-latest.json`
   - `/Volumes/PixelTable/VW_iTwin_Bridge/meta/promotion/readiness.json`
   - `/Volumes/PixelTable/VW_iTwin_Bridge/meta/runs/iterations.jsonl`

Validation loop:

- `uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py`
- `uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py --json`
- `bash scripts/pre-commit-docs-check.sh` from `/Volumes/PixelTable/VW_iTWIN_Bridge/VW_iTwin_Bridge` if needed

Important:

- do not call `/Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/run-parent-ratchet.sh`
  from inside this run; that is the outer launcher
- keep all edits inside `/Volumes/PixelTable/VW_iTwin_Bridge/meta`
- append real non-dry iteration evidence to
  `/Volumes/PixelTable/VW_iTwin_Bridge/meta/runs/iterations.jsonl` as one compact
  JSON object per line
- treat the iteration ledger and refreshed artifacts as the primary execution
  evidence; the final report must agree with them instead of replacing them

Report at end:

1. `pass` or `blocked`
2. whether the original metric was accepted or repaired
3. number of real non-dry cycles executed
4. before and after scores
5. files changed
6. fresh artifact paths
7. iteration ledger entries appended
8. structured report path
