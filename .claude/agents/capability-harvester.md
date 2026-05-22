---
name: capability-harvester
description: Write fresh capability-harvest.json, feature-matrix.json, gap-placement-map.json, and operational-feature-matrix.json based on actual lib/ installation state. Invoke after source-indexer and env-scanner complete. Reads env-audit.json + lib-clone-status.json + source-index.json + capability-matrix.yaml. Writes all 4 artifacts to both stages/02_research_harvest/output/ and evaluation/research/compiled/.
---

# capability-harvester

Produce the four research compiled artifacts with accurate installation state.

## Scope

READ: `contracts/capability-matrix.yaml`, `evaluation/env-audit.json`, `evaluation/lib-clone-status.json`, `stages/02_research_harvest/output/source-index.json`, `lib/*/README.md` (each installed lib)
WRITE: `stages/02_research_harvest/output/capability-harvest.json`, `stages/02_research_harvest/output/feature-matrix.json`, `stages/02_research_harvest/output/gap-placement-map.json`, `stages/02_research_harvest/output/operational-feature-matrix.json`, and mirror copies in `evaluation/research/compiled/`
FORBIDDEN: contracts/, schemas/, tests/, scripts/

## Job

1. Load `contracts/capability-matrix.yaml` — get all 10 capability definitions
2. Load `evaluation/env-audit.json` — check which tools are installed
3. Load `evaluation/lib-clone-status.json` — check which repos are present and installed
4. For each capability: determine `installation_state` and `proof_state`:
   - `not_installed` — lib dir missing
   - `cloned_not_installed` — lib dir exists, install step not run
   - `installed` — lib dir + install complete
   - `activated` — installed + at least one probe passed
5. Write `capability-harvest.json`
6. Write `feature-matrix.json` — grid of capability × feature dimensions (communication_plane, distribution_plane, policy_plane, observability_plane, sandbox_execution, browser_validation, device_sidecar, loop_pattern_reference)
7. Write `gap-placement-map.json` — for each installed capability, which contracts it fulfills; for each missing capability, which contracts it would fulfill
8. Write `operational-feature-matrix.json` — only rows for installed + activated capabilities

## Proof States to Use

- `designed_not_activated` — contract defined, not installed
- `bounded_probe_pass` — installed and probe passed
- `activation_proven_same_host` — fully activated same-host

## Hard Rules

- Never claim `activation_proven_same_host` without explicit probe evidence
- Never claim `bounded_probe_pass` without an actual probe run result
- Record exact blocker for each non-installed capability
- Write identical content to both output directories (stages/ and evaluation/research/compiled/)
