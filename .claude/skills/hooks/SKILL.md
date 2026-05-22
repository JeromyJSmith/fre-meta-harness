---
name: hooks
description: Claude Code hooks patterns. Use when writing hook scripts (PreToolUse, PostToolUse, Stop, SessionStart, etc.) or configuring .claude/settings.json to wire hooks. Reference lib/claude-code-hooks-mastery/ for working examples.
---

# Claude Code Hooks

Hook scripts intercept Claude tool calls and lifecycle events. Source examples in `lib/claude-code-hooks-mastery/.claude/hooks/`.

## Location

`lib/claude-code-hooks-mastery/` — cloned (no install needed, hooks are Python scripts).

## Hook Types (settings.json keys)

| Hook | Trigger | Use For |
|------|---------|---------|
| `PreToolUse` | Before every tool call | Block dangerous commands, log, validate |
| `PostToolUse` | After every tool call | Log results, update observability |
| `Stop` | When Claude stops | Completion verification |
| `SessionStart` | Session begins | Bootstrap validation |
| `SessionEnd` | Session ends | Cleanup, final log |
| `Notification` | Claude sends notification | Alert routing |
| `UserPromptSubmit` | User submits prompt | Pre-processing, logging |
| `PreCompact` | Before context compaction | Save state |
| `PermissionRequest` | Permission prompt | Log or route |
| `SubagentStart` / `SubagentStop` | Subagent lifecycle | Multi-agent observability |

## Hook Script Shape

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///
import json, sys
def main():
    data = json.load(sys.stdin)
    # tool_name = data.get("tool_name", "")
    # tool_input = data.get("tool_input", {})
    # exit(2) to BLOCK the tool call with error message
    # exit(1) to log a warning without blocking
    # exit(0) to allow
    sys.exit(0)
if __name__ == "__main__":
    main()
```

## settings.json Pattern

```json
{
  "hooks": {
    "PreToolUse": [{"matcher": "", "hooks": [{"type": "command", "command": "uv run $CLAUDE_PROJECT_DIR/.claude/hooks/pre_tool_use.py"}]}],
    "PostToolUse": [{"matcher": "", "hooks": [{"type": "command", "command": "uv run $CLAUDE_PROJECT_DIR/.claude/hooks/post_tool_use.py"}]}]
  }
}
```

## This Workspace's Hooks

- `.claude/hooks/pre_tool_use.py` — blocks dangerous rm, .env access; logs to `logs/pre_tool_use.jsonl`
- `.claude/hooks/post_tool_use.py` — logs all tool results to `logs/post_tool_use.jsonl`
- `.claude/settings.json` — wires both hooks
