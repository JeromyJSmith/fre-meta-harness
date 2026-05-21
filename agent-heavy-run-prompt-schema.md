# Agent Heavy-Run Prompt Schema

This parent wrapper uses the same portable execution contract as the child
Meta-Harness.

Required blocks:

1. `triad_context`
2. `mode`
3. `mission`
4. `current_verified_state`
5. `hard_rules`
6. `allowed_paths`
7. `disallowed_paths`
8. `tasks`
9. `validation_loop`
10. `handoff_inputs`
11. `success_criteria`
12. `report_contract`

The triad context names the acting governance role:

- `orchestrator-validator`
- `research`
- `architect`

and binds the next heavy run to an upstream governed handoff artifact.

The handoff input block is required whenever a prompt is emitted for a follow-on
agent. It preserves:

- the handoff artifact path
- the source report paths
- the required follow-up roles
- the consumption requirements

Every heavy or bounded parent-wrapper prompt must map back to this same schema.

When the run touches runtime activation or runtime-proof hardening, the
`report_contract` block must also name:

- runtime-truth fields
- blocker fields
- freshness fields
- score-saturation fields
- command-evidence fields

When an architect, research, or orchestrator-validator run is expected to hand
work to a follow-on agent, the report contract must also name follow-up prompt
fields and emit:

1. a machine-readable handoff artifact that conforms to
   `architect-review-handoff-prompt.schema.json`
2. a governed Markdown companion prompt artifact with front matter and bottom
   matter that points back to the structured prompt family

The Markdown companion is a routing and operator-facing surface only. The
structured YAML/JSON contract family remains machine truth.
