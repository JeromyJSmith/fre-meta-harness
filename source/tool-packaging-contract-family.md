# Tool packaging contract family

## Purpose

Make prompt-to-tool packaging machine-readable inside the parent wrapper without
claiming a live persistence lane that the repo cannot yet prove.

## Boundaries

1. The current authoritative surface is filesystem-backed contracts, schemas,
   examples, and evaluation artifacts inside the parent repo.
2. Endpoint-first packaging is defined now, but no live HTTP service is claimed.
3. Pixeltable and DuckDB remain doctrine and future-lane expectations until a
   dedicated persistence slice lands with bounded proof.

## Family members

- `contracts/tool-packaging-family.yaml`
- `schemas/tool-packaging-family.schema.json`
- `schemas/tool-spec.schema.json`
- `schemas/agent-card.schema.json`
- `schemas/tool-task.schema.json`
- `schemas/tool-artifact.schema.json`

## Required workflow

1. Discovery must resolve through `/.well-known/agent.json`.
2. Invocation must create a task through `/v1/tools/{toolId}/tasks`.
3. Status and artifact retrieval must stay explicit through `/v1/tasks/{taskId}`
   and `/v1/tasks/{taskId}/artifacts`.
4. Every task must point at explicit artifact outputs.
5. Every artifact must carry a registry entry and an honest storage truth.

## Truth guardrails

- Do not imply live Pixeltable writes or DuckDB query execution from this family.
- Keep `blocked_not_activated` and `planned_not_activated` states explicit until
  the persistence lane is proven.
- Keep the contract usable for workflow packaging, capability harvesting, and
  future runner proofs without widening into child-runtime activation.
