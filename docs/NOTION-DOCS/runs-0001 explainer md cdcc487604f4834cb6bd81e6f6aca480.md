# runs-0001.explainer.md

## Run log explainer (human readable)

A run log is append-only history. Every run must include:

- runId
- timestamp
- plan used
- list of produced/modified artifacts
- score reference
- keep/revert/investigate decision

This enables meta-harness improvement across runs.