# Pixeltable Operational Substrate

Pixeltable is the durable substrate for the Meta-Harness and its child bodies.

At the parent wrapper layer this means:

- contract surfaces are shaped for later Pixeltable ingestion
- evaluation and promotion artifacts are substrate-oriented
- library entries, evidence, and bridge records are designed for durable table
  storage
- downstream analytics are expected to flow through Arrow or Parquet into
  DuckDB WASM

Git remains the change surface. Pixeltable remains the intended durable
operational graph.
