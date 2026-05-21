# Pixeltable Operational Substrate

Pixeltable is the durable substrate for the Meta-Harness and its child bodies.

At the parent wrapper layer this means:

- contract surfaces are shaped for later Pixeltable ingestion
- evaluation and promotion artifacts are substrate-oriented
- library entries, evidence, and bridge records are designed for durable table
  storage
- downstream analytics are expected to flow through Arrow or Parquet into
  DuckDB WASM

Parent-layer conceptual destinations only:

- governed prompt artifacts: a parent-scoped prompt artifact destination for
  approved heavy-run prompts and their governing metadata
- governed handoff artifacts: a parent-scoped handoff destination for explicit
  triad-to-runtime mapping notes, downstream owners, and execution boundaries
- triad review outputs: a parent-scoped review destination for
  orchestrator-validator, research, and architect conclusions plus cited
  evidence classes
- agent-extension requests: a parent-scoped request destination for governed
  self-extension proposals captured under
  `contracts/agent-extension-request.yaml`
- promotion and blocker evidence: a parent-scoped evidence destination for
  readiness, non-readiness, blocker precision, and promotion-state artifacts

These are conceptual parent-layer destinations, not a claim that live child
runtime tables, ingestion jobs, or end-to-end integrations already exist.
Parent docs may define the artifact families and intended substrate shape before
the child runtime adopts them.

Git remains the change surface. Pixeltable remains the intended durable
operational graph.
