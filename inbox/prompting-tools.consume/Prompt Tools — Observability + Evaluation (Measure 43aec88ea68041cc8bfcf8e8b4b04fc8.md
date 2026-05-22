# Prompt Tools — Observability + Evaluation (Measure Plane)

<aside>
📡

**Purpose**: Make tool behavior visible, comparable, and regressible. No hidden work.

</aside>

## 0) Before → After

- **Before**: logs/transcripts only.
- **After**: structured event stream + benchmarks + baselines stored in Pixeltable (queryable via DuckDB).

## 1) Required schemas

- EventEnvelope.schema.json
- BenchmarkPoint.schema.json
- Scorecard.schema.json

## 2) Event envelope (minimum fields)

- eventId, timestamp
- runId/sessionId
- toolId
- agentId/peerName
- eventType
- correlationId + parentEventId
- status
- payload (typed sub-objects)

## 3) Benchmarks (minimum)

- mesh latency
- tool latency
- success rate
- policy blocks/asks
- token/cost accounting
- artifact counts + sizes

## 4) Pixeltable tables

- events
- benchmarks
- scorecards
- baselines

## 5) DuckDB query recipes (examples)

- “latest run summary by toolId”
- “regression deltas vs baseline”
- “top causes of block/ask”

## 6) Tasklist

- [ ]  Freeze EventEnvelope schema
- [ ]  Implement correlation rules
- [ ]  Define benchmark groups + metrics
- [ ]  Persist events + benchmarks to Pixeltable
- [ ]  Add baseline comparison report artifact