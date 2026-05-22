# Proof State Vocabulary

Condensed from `contracts/subsystem-runner-proof-family.yaml`.

## State Hierarchy (ordered)

| State | Meaning | When to Use |
|-------|---------|-------------|
| `designed_not_activated` | Parent owns only the contract boundary; no bounded runner proof executed | Default for any new subsystem |
| `bounded_probe_blocked` | Probe ran but exact prerequisite is missing; blocker recorded in machine-readable artifacts | Probe executed, prerequisite absent |
| `bounded_probe_pass` | Bounded same-host proof tranche passed; observability artifacts and validator refresh present | Probe passed locally |
| `activation_proven_same_host` | Subsystem-specific probe + observability handshake + tool-health evidence all exist for same-host lane | Full same-host activation proven |

## Promotion Rules

1. Never skip a state — each requires its predecessor's artifacts.
2. `bounded_probe_blocked` requires exact blocker recorded in probe-status.json.
3. `bounded_probe_pass` requires: probe-status.json, events.jsonl, benchmarks.json — all in `evaluation/subsystem-runner-probes/<id>/`.
4. `activation_proven_same_host` additionally requires: evaluation/tool-health/status.json updated with the subsystem entry.

## Do Not Overclaim

- Do not promote intake_etl, research_harvest, semantic_cartography, or wrapper_synthesizer beyond `designed_not_activated` without fresh subsystem-specific proof artifacts.
- Do not convert same-host evidence into cross-device claims.
- Do not imply Pixeltable sync, DuckDB query proof, or child-runtime adoption from parent artifacts alone.

## Current States (as of last probe run)

| Subsystem | Current State |
|-----------|--------------|
| peer_mesh_local.same_host | activation_proven_same_host |
| inbox_protocol.same_host | activation_proven_same_host |
| intake_etl | bounded_probe_pass |
| research_harvest | bounded_probe_pass |
| semantic_cartography | bounded_probe_pass |
| wrapper_synthesizer | designed_not_activated |
