# intake_etl

## Purpose

Define the parent-owned intake boundary that turns governed inbox drops and
consume-folder assets into normalized packet, extract, and provenance records.

## Wrap Boundary

- enters through governed packet and delegation surfaces
- stops at normalized packet, extract, and source-index artifacts
- does not claim live watchers beyond the already-kept inbox protocol

## Consumes

- `contracts/inbox-packet.yaml`
- `contracts/inbox-routing-decision.yaml`
- `contracts/delegation-bundle.yaml`

## Emits

- `evaluation/research/harvest-manifest.json`
- `evaluation/research/compiled/source-index.json`

## Reusable Repo Lens

- `oven-sh/bun`
- `oxc-project/oxc`
- `colbymchenry/codegraph`

## Non-Activation Truth

No intake ETL subsystem runner is activated by this scaffold.
