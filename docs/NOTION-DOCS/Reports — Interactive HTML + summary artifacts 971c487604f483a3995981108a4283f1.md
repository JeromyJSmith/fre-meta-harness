# Reports — Interactive HTML + summary artifacts

## Purpose

Standardize reports so runs are comparable and improvements compound.

## Core report types

1. **Run report** (HTML)
- inputs
- artifacts produced
- diffs
- validation results
- score vs goal
- decision (keep/revert)
1. **Scorecard** (JSON)
- metrics only, machine-parsable
1. **Executive summary** (Markdown)
- what changed + why + next bet

## Interactive HTML report spec (v0)

### Required sections

- Header: runId, timestamp, Claude Code version
- Links: artifacts, logs, plan file
- Validation: pass/fail table
- Metrics: primary + secondary
- Trace: collapsible tool/actions list
    - Proof package: which of the seven parts were present/updated in this run
    - Gate snapshot: lifecycle-gate statuses for the active slice (and regression gates)

### Output rule

If HTML is produced, also produce:

- `scorecard.json`
- `summary.md`
    - `promotion.md` (explicit decision + blocker carry-forward)