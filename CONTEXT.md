# fre-meta-harness

Governed intake, research, cartography, and synthesis pipeline for the VW iTWIN Bridge parent wrapper.

## Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| A file lands in `inbox/` | `stages/01_inbox_intake/CONTEXT.md` | Validate packet, emit routing + delegation |
| Research pass needed | `stages/02_research_harvest/CONTEXT.md` | Compile capability harvest, feature matrix, gap placement |
| Semantic analysis needed | `stages/03_semantic_cartography/CONTEXT.md` | Index code, map research → semantic graph |
| Triad review needed | `stages/04_triad_review/CONTEXT.md` | Dispatch ≥3 options, promote or block |
| Handoff bundle requested | `stages/05_wrapper_synthesis/CONTEXT.md` | Assemble governed handoff bundles (GATED — triad promote required) |

## Shared Resources

| Resource | Location | Contains |
|----------|----------|---------|
| Governance config | `_config/agent-roles.md` | All role definitions condensed from contracts |
| Hooks policy | `_config/hooks-policy.md` | Hook manifest rules |
| Proof vocabulary | `_config/proof-vocabulary.md` | Proof state hierarchy and rules |
| Voice rules | `_config/voice.md` | Communication style and formatting |
| Contracts | `contracts/` | 31 machine-readable governance contracts |
| Evaluation artifacts | `evaluation/` | Tool health, probes, validation reports |
| Lib repos | `lib/` | ICM, Disler foundations, Pi agent |

## Stage Map

```
stages/
  01_inbox_intake/   ← front-door: validate + route incoming packets
  02_research_harvest/  ← compile capability evidence and feature matrix
  03_semantic_cartography/ ← codegraph + InfraNodus semantic analysis
  04_triad_review/   ← triad dispatch: ≥3 options, promote or block
  05_wrapper_synthesis/ ← GATED: assemble governed handoff bundles
```

## Active Proof States

| Subsystem | State |
|-----------|-------|
| peer_mesh_local.same_host | activation_proven_same_host |
| inbox_protocol.same_host | activation_proven_same_host |
| intake_etl | bounded_probe_pass |
| research_harvest | bounded_probe_pass |
| semantic_cartography | bounded_probe_pass |
| wrapper_synthesizer | designed_not_activated (gated) |
