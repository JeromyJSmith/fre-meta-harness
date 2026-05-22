# research_harvest

## Purpose

Define the parent-owned harvest boundary that compiles normalized evidence into
capability, feature, gap, and source-index views while preserving provenance.

## Wrap Boundary

- starts from normalized packet and extract outputs
- ends at compiled research artifacts and their handoff-ready summaries
- keeps compiled artifacts truthful current-state evidence rather than runtime proof

## Consumes

- `evaluation/research/harvest-manifest.json`
- `contracts/research-packet-manifest.yaml`
- `source/subsystems/registry.json`

## Emits

- `evaluation/research/compiled/capability-harvest.json`
- `evaluation/research/compiled/feature-matrix.json`
- `evaluation/research/compiled/gap-placement-map.json`

## Reusable Repo Lens

- `VectifyAI/OpenKB`
- `sandeco/reversa`
- `Imbad0202/academic-research-skills`

## Non-Activation Truth

No LLM-backed harvest subsystem is activated by this scaffold.
