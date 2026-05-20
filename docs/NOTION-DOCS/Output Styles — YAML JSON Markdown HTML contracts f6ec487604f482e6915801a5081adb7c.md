# Output Styles — YAML / JSON / Markdown / HTML contracts

## Purpose

Define how the harness formats outputs so they are **predictable, parseable, and cheap**.

## Output style registry

Each output style gets:

- `styleId`
- target format (yaml/json/markdown/html)
- intended consumer (human/agent/tool)
- schema (if applicable)
- examples

## Baseline styles (seed)

### 1) `yaml:frontmatter`

- For skills, subagents, rules, and plan files.
- Rule: keep critical fields on a **single line** when parsers are brittle.

### 2) `json:scorecard`

- For evaluation results and metrics.

### 3) `markdown:spec`

- For human-readable contracts, with stable headings.

### 4) `html:interactive-report`

- For drilldown reports (links, filters, collapsible sections).

## Style contracts (recommended)

- Every tool-consumed output must declare its **schema**.
- Every human-consumed output must declare its **purpose + how to verify**.

## Hardening rules (portable)

- Every non-trivial output style must have:
    - a JSON Schema (even for Markdown/HTML, schema describes required sections/keys)
    - at least one valid example + at least one invalid example
    - an expected-failures entry when a failure mode is known and recurring