# wrapper_synthesizer

## Purpose

Define the late-bound parent-owned wrapper synthesis boundary that turns
approved subsystem outputs into wrapper-facing contracts, prompts, and handoff
bundles.

## Wrap Boundary

- starts only after subsystem outputs are reviewed and routed
- ends at governed wrapper-binding candidates and follow-up prompt requests
- remains gated until an explicit downstream runtime owner and proof artifact exist

## Consumes

- `source/subsystems/registry.json`
- `evaluation/research/compiled/gap-placement-map.json`
- `contracts/delegation-bundle.yaml`

## Emits

- wrapper binding candidates
- governed handoff bundles
- parent-owned prompt follow-up requests

## Reusable Repo Lens

- `sandeco/reversa`
- `chorus-codes/chorus`
- `open-bias/open-bias`

## Non-Activation Truth

No wrapper synthesis execution is activated by this scaffold.
