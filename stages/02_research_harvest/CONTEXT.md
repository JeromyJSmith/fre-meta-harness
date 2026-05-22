# Stage 02: Research Harvest

Compile capability evidence, feature matrix, and gap placement from the current harness state and lib/ repos.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../01_inbox_intake/output/routing-decision.json` | Full file | Scope of the harvest pass |
| Reference | `references/research-packet-manifest.yaml` | Full file | Required output artifacts schema |
| Reference | `../../contracts/capability-matrix.yaml` | Full file | Canonical capability surface |
| Reference | `../../contracts/gap-map-strength.yaml` | Full file | Gap placement taxonomy |
| Lib repos | `../../lib/` | README.md per repo | Installed capabilities and their readiness |
| Existing harvest | `../../evaluation/research/compiled/` | All JSON files | Prior evidence baseline |

## Process

1. Read routing-decision from `../01_inbox_intake/output/` to understand harvest scope
2. Walk `../../lib/` repos — read each README and note installed/not-installed status
3. Load `references/capability-matrix.yaml` and mark each capability as `available`, `installed`, or `missing`
4. Identify gap placements using `references/gap-map-strength.yaml` taxonomy
5. Compile `source-index.json` listing all code roots, lib repos, and contract files with their paths
6. Emit all five artifacts to `output/`

## Audit

| Check | Pass Condition |
|-------|---------------|
| All 5 artifacts emitted | capability-harvest, feature-matrix, gap-placement-map, source-index, operational-feature-matrix |
| Lib repos inventoried | Every dir in lib/ has an entry in source-index.json |
| No overclaim | Artifacts list proof-state per capability; none upgraded without fresh evidence |

## Outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Capability harvest | `output/capability-harvest.json` | Per-capability installed/missing status |
| Feature matrix | `output/feature-matrix.json` | Feature × readiness grid |
| Gap placement map | `output/gap-placement-map.json` | Gap taxonomy with strength scores |
| Source index | `output/source-index.json` | All code roots, lib repos, contracts |
| Operational feature matrix | `output/operational-feature-matrix.json` | Runtime-activated features only |
