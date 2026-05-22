# Consume source-quality pipeline

This source note defines the parent-owned bounded lane that turns consume inputs
into machine-validated source-quality artifacts without promoting new runtime
activation claims.

## Scope

- first-party consume packet inventory
- bounded extraction mapping
- evidence-strength normalization
- compiled-output ingestion mapping
- operational feature matrix generation

## Truth boundary

- same-host `peer_mesh_local` and `inbox_protocol` remain the only active parent
  runtime lanes
- transcript-derived workflow claims remain blocked unless frame or terminal
  proof is stored in fresh parent artifacts
- compiled derivatives inherit the strongest truthful limit from their source
  packets

## Required outputs

- `evaluation/research/compiled/operational-feature-matrix.json`
- refreshed `evaluation/research/compiled/source-index.json`
- refreshed `evaluation/research/compiled/capability-harvest.json`
- refreshed `evaluation/research/compiled/feature-matrix.json`
- refreshed `evaluation/research/compiled/gap-placement-map.json`
- outbox handoff artifacts for operational matrix, capability extension, consume
  extraction mapping, and compiled-output ingestion mapping
