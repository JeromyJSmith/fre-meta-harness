---
name: observability
description: Multi-agent observability patterns. Use when adding logging, tracing, or monitoring across agent interactions. Reference lib/claude-code-hooks-multi-agent-observability/ for working examples including agent session tracking, damage control, and multi-agent event streams.
---

# Multi-Agent Observability

Patterns for logging, tracing, and monitoring across Claude Code agent interactions.

## Location

`lib/claude-code-hooks-multi-agent-observability/` — cloned.

Structure:
```
.claude/
  agents/       ← agent definitions with observability roles
  skills/       ← skill files
  themes/       ← output themes
  damage-control-rules.yaml
  settings.json
```

## Key Patterns

### Per-Tool Logging

Log every tool call to a JSONL file for replay and analysis:

```python
# pre_tool_use.py / post_tool_use.py
with log_path.open("a") as f:
    f.write(json.dumps(input_data) + "\n")
```

### Damage Control Rules

`lib/claude-code-hooks-multi-agent-observability/.claude/damage-control-rules.yaml` defines conditions under which an agent should pause and escalate instead of proceeding autonomously.

### Agent Session Tracking

Each agent session writes events to `logs/` — enables post-hoc replay of exactly what each agent did and in what order.

## This Workspace's Observability

- `logs/pre_tool_use.jsonl` — all tool calls before execution
- `logs/post_tool_use.jsonl` — all tool results after execution
- `evaluation/subsystem-runner-probes/` — per-subsystem proof artifacts (events.jsonl, benchmarks.json, probe-status.json)
- `evaluation/tool-health/status.json` — tool health state

## Proof Artifact Emission

Every subsystem probe emits three artifacts to `evaluation/subsystem-runner-probes/<id>/`:
1. `probe-status.json` — proof state, blockers, gate IDs
2. `events.jsonl` — timestamped event stream
3. `benchmarks.json` — duration and key metrics
