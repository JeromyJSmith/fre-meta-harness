# Local Models Goal — Single File Agents + Strict Contracts

<aside>
🧠

Local models goal: make the harness so opinionated and contract-driven that small local models can run it reliably.

</aside>

## Thesis

If the portable harness contracts are strict enough, we can replace expensive cloud models with small local models for most execution steps.

The mechanism is:

- single responsibility, single file agents
- hard schemas and examples for every artifact
- deterministic validators and scorers
- promotion decisions remain explicit artifacts
- minimal freeform reasoning in the critical path

This turns most work into: validate, transform, and patch against contracts, which small models can do.

## Target model family

- Small ternary models (bonsai family or equivalent)
- Local first execution for routine phases
- Cloud escalation only when required by complexity

## What must be true (requirements)

1. Each step in the golden path is fully specifiable as an input/output contract.
2. Every transformation step has:
    - schema
    - examples
    - expected failures
    - tests
    - evaluation artifacts
    - promotion decision
3. Each agent is single file, single job, with strict IO.
4. The harness provides enough deterministic tooling that the model only chooses among bounded actions.

## Implications for harness design

- Prefer structured artifacts over prose
- Stronger compiler outputs (missing, compliance, drift)
- Stronger prompt contract enforcement (prompts are artifacts)
- Avoid wide-context, open-ended reasoning in production runs

## Milestone: local-model readiness

A layer is local-model-ready when:

- a small model can run the golden path end to end with no human edits
- failures are caught by validators with actionable messages
- promotion decisions remain truthful

## Notes

This is a design target for portability and cost control, not an immediate mandate to stop using cloud models.