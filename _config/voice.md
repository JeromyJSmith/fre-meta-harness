# Voice Rules

Communication style and formatting rules for all agents in this workspace.

## Core Principles

- State results and decisions directly — no hedging on things that are decided
- Be terse: one sentence per update is almost always enough
- Never use "optional" for improvements — if it's better, do it
- Never mark something optional when it was discussed as an improvement

## Proof Language

Use exact proof state vocabulary from `proof-vocabulary.md`. Never invent synonyms:
- Wrong: "seems to work", "probably passing", "appears to be ready"
- Right: "bounded_probe_pass", "activation_proven_same_host", "bounded_probe_blocked — missing: contracts/inbox-packet.yaml"

## Artifact Language

Reference artifacts by their exact path, not by description:
- Wrong: "the capability file"
- Right: `evaluation/research/compiled/capability-harvest.json`

## Role Language

Use exact role IDs from `agent-roles.md`:
- Wrong: "the orchestrator", "the reviewer", "the validator agent"
- Right: `orchestrator-validator`, `research`, `architect`

## Blocker Language

State blockers precisely:
- Wrong: "something is missing", "this needs to be fixed first"
- Right: "bounded_probe_blocked — contracts/inbox-packet.yaml missing"

## Formatting

- Use tables for structured data (inputs, outputs, capabilities)
- Use fenced code blocks for commands
- Markdown headers are H1 for stage name, H2 for sections (Inputs, Process, Outputs)
- No emoji unless user requests it
