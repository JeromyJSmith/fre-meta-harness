# Agent Heavy-Run Prompt Schema

This parent wrapper uses the same portable execution contract as the child
Meta-Harness.

Required blocks:

1. `mode`
2. `mission`
3. `current_verified_state`
4. `hard_rules`
5. `allowed_paths`
6. `disallowed_paths`
7. `tasks`
8. `validation_loop`
9. `success_criteria`
10. `report_contract`

Every heavy or bounded parent-wrapper prompt must map back to this same schema.

When the run touches runtime activation or runtime-proof hardening, the
`report_contract` block must also name:

- runtime-truth fields
- blocker fields
- freshness fields
- score-saturation fields
- command-evidence fields

When an architect or research run is expected to hand work to a follow-on
agent, the report contract should also name follow-up prompt fields and emit a
handoff artifact that conforms to `architect-review-handoff-prompt.schema.json`.
