# Subsystem runner proof family

## Purpose

Define the parent-owned contract boundary between subsystem scaffolds and any
future runner proof without claiming that a subsystem runner is already active.

## Boundaries

1. The current parent runtime truth stays limited to same-host peer mesh and
   same-host inbox protocol.
2. Cross-device transport remains blocked until authenticated transport proof
   exists in fresh artifacts.
3. Intake ETL, research harvest, semantic cartography, and wrapper synthesizer
   remain non-activated subsystem lanes in this slice.
4. Pixeltable sync, DuckDB query proof, and child runtime adoption remain out of
   scope for this family.

## Family members

- `contracts/subsystem-runner-proof-family.yaml`
- `contracts/contract-to-runner-map.yaml`
- `contracts/subsystem-bounded-probe.yaml`
- `contracts/subsystem-observability-handshake.yaml`
- `schemas/subsystem-runner-proof-family.schema.json`
- `schemas/contract-to-runner-map.schema.json`
- `schemas/subsystem-bounded-probe.schema.json`
- `schemas/subsystem-observability-handshake.schema.json`
- `schemas/subsystem-runner-proof-strengthening-report.schema.json`

## Truth guardrails

- Keep `designed_not_activated` as the truthful default unless a subsystem probe
  is actually executed and evidenced.
- Treat bounded probe design as governed preparation, not as activation proof.
- Require fail-loud observability and validator refresh before any proof state
  can move beyond design-only.
- Keep contract-to-runner mapping separate from governance-triad, front-door
  runtime, and peer-mesh runtime role definitions.
