# Architect Review Handoff Prompt Schema

This schema defines the artifact an architect or research agent should emit when
it finishes a bounded slice and wants the next agent to review, verify, and
continue the work efficiently.

## Purpose

The handoff prompt artifact does two jobs:

1. summarize the exact run, proof surfaces, and review expectations for the next
   agent
2. require that the next follow-up prompt is generated against the governed
   `agent-heavy-run-prompt` schema rather than as loose prose
3. require a parent-only markdown companion prompt artifact that stays aligned
   to the structured contract family instead of replacing it

## Required Blocks

1. `producer_run`
2. `inbox_context`
3. `linked_consumers`
4. `auto_consume_policy`
5. `handoff_goal`
6. `decision_space`
7. `review_scope`
8. `required_inputs`
9. `review_protocol`
10. `validation_loop`
11. `expected_outputs`

## Core Rule

Every architect/research handoff must preserve runtime-truth, blocker,
freshness, and command-evidence expectations in the follow-up prompt artifact.

It must also carry the upstream inbox packet reference, the packet artifact
type, the required gate state, the required consumers, the bottom-matter
reference, and the structured contract reference that made the handoff
actionable.

It must also be able to target:

- the orchestrator-validator role
- the architect agent
- the research agent
- either architect or research through the selector role
- a governed fanout through policy mode

## Decision Space Requirement

The `decision_space` block is required and must include:

1. at least three options
2. one `recommended_option_id`
3. option-level rationale
4. `expected_artifacts` for each option
5. one `blocker_or_escalation_path`

## Follow-Up Output Requirements

The `expected_outputs.follow_up_prompt_artifact` block must point at:

- `agent-heavy-run-prompt.schema.json`
- `agent-heavy-run-prompt.template.yaml`

and must preserve:

- runtime-truth fields
- blocker fields
- freshness fields
- command-evidence fields

The `expected_outputs.dispatch_message` block is also required. It must point to
an artifact that tells the next governed consumer which decision option to
execute and which structured outputs to read first.

The `expected_outputs.companion_markdown_prompt_artifact` block is required as a
companion surface. It must point at:

- `prompts/governed-triad-follow-up-prompt.template.md`

and it must guarantee:

- front matter is present
- the bottom matter marker is present
- the artifact is explicitly parent-only and governed-handoff oriented
- machine truth stays with the structured YAML/JSON contract family

The handoff artifact must also declare whether the next prompt is intended for a
single consumer, either architect or research, or a governed fanout selected by
policy mode.
