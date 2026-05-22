# semantic_cartography

## Purpose

Define the parent-owned semantic mapping boundary that turns normalized source
and compiled research material into graph-ready summaries and subsystem
placements.

## Wrap Boundary

- starts from normalized sources and compiled feature views
- ends at semantic graph candidates and wrapper-binding inputs
- does not claim a live semantic cartography runtime

## Consumes

- `evaluation/research/compiled/source-index.json`
- `evaluation/research/compiled/feature-matrix.json`
- `contracts/subsystem-harness-topology.yaml`

## Emits

- semantic graph-ready summaries
- subsystem candidate placements
- wrapper binding inputs

## Reusable Repo Lens

- `colbymchenry/codegraph`
- `facebook/pyrefly`
- `oxc-project/oxc`

## Non-Activation Truth

No semantic cartography subsystem runner is activated by this scaffold.
