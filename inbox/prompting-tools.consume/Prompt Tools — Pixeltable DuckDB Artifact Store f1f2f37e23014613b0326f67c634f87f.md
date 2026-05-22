# Prompt Tools — Pixeltable/DuckDB Artifact Store

<aside>
🗄️

**Purpose**: Canonical storage + query substrate for tools, tasks, artifacts, events, tests, and metrics.

</aside>

## 0) Before → After

- **Before**: artifacts scattered across filesystem + ad hoc JSON.
- **After**: every artifact is stored with:
    - schemaRef
    - runId + correlation
    - provenance (source refs)
    - evaluability (score hooks)

## 1) Required Pixeltable tables (v0)

1) tool_specs

2) agent_cards

3) tasks

4) artifacts

5) events

6) policies

7) tests

8) scorecards

9) baselines

## 2) DuckDB requirements

- Every table must be queryable with stable column names.
- Provide "starter queries" for:
    - run summaries
    - artifact inventories
    - policy violation aggregation
    - regression comparisons

## 3) Ingestion contract

- every tool invocation writes:
    - task row
    - artifact rows
    - event rows
    - benchmark rows

## 4) Export contract

- export pack contains:
    - ToolSpec
    - AgentCard
    - OpenAPI
    - schemas
    - artifacts
    - run summary

## 5) Tasklist

- [ ]  Define table schemas + migrations
- [ ]  Define ingestion adapters (filesystem → Pixeltable)
- [ ]  Define runId/correlationId semantics
- [ ]  Implement DuckDB query layer + report artifacts