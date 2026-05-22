# Prompt Tools — Policy + Gates (Trust Plane)

<aside>
🛡️

**Purpose**: Encode enforceable trust boundaries so tools are safe, debuggable, and promotable.

</aside>

## 0) Before → After

- **Before**: “be careful” guidance.
- **After**: explicit policies + deterministic gates:
    - allow/block/ask decisions
    - message-boundary policies (peer mesh)
    - PII boundaries (prod ↔ dev)
    - completion criteria + loop budgets
    - promotion rules (what must pass to ship)

## 1) Required policy bundles

### POL-ALLOW-BLOCK-ASK

- allow
- block (severity)
- ask (question + rationale)

### POL-MESSAGE-BOUNDARY

- allowed payload types
- redaction requirements
- correlation and audit logging

### POL-TOOL-BOUNDARY

- file access rules
- shell command rules
- network call rules

### POL-COMPLETION

- explicit done token / state
- max turns
- max outbound calls

## 2) Gate sequence (tool promotion)

1) Schema present + valid

2) OpenAPI present

3) Golden tests pass

4) Policy violation tests pass

5) Observability events emitted

6) Pixeltable persistence confirmed

7) DuckDB queries return expected summaries

8) Doc parity (human-readable spec matches machine contract)

## 3) Pixeltable tables

- policies
- gate_results
- violations

## 4) Tasklist

- [ ]  Define PolicySpec JSON Schema
- [ ]  Define GateResult JSON Schema
- [ ]  Implement “allow/block/ask” evaluator as middleware
- [ ]  Implement message-boundary redaction checks
- [ ]  Add loop budget enforcement
- [ ]  Store gate results + violations in Pixeltable