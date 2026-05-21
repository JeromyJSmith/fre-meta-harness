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

## Required Blocks

1. `producer_run`
2. `consumer_agent`
3. `handoff_goal`
4. `review_scope`
5. `required_inputs`
6. `review_protocol`
7. `validation_loop`
8. `expected_outputs`

## Core Rule

Every architect/research handoff must preserve runtime-truth, blocker,
freshness, and command-evidence expectations in the follow-up prompt artifact.

## Follow-Up Prompt Requirement

The `expected_outputs.follow_up_prompt_artifact` block must point at:

- `agent-heavy-run-prompt.schema.json`
- `agent-heavy-run-prompt.template.yaml`

and must preserve:

- runtime-truth fields
- blocker fields
- freshness fields
- command-evidence fields
