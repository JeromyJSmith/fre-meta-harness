---
name: just-prompt
description: just-prompt MCP server for model-agnostic prompt routing. Use when you need to send the same prompt to multiple LLM providers, compare outputs, or route prompts based on provider/model selection. Installed via uv sync.
---

# just-prompt

Python MCP server for multi-provider LLM prompt routing by Sam Disler.

## Location

`lib/just-prompt/` — cloned and `uv sync` complete (19 packages installed).

## Running

```bash
cd lib/just-prompt
uv run just-prompt --help
```

Or as an MCP server (add to `.mcp.json`):
```json
{
  "mcpServers": {
    "just-prompt": {
      "command": "uv",
      "args": ["run", "--directory", "lib/just-prompt", "just-prompt"],
      "env": {
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}",
        "OPENAI_API_KEY": "${OPENAI_API_KEY}"
      }
    }
  }
}
```

## Capabilities

- Send prompts to multiple providers in one call
- Compare outputs across Claude, GPT, Gemini
- Model selection routing
- Batch prompt execution

## Required Environment Variables

- `ANTHROPIC_API_KEY` — for Claude models
- `OPENAI_API_KEY` — for OpenAI models
- `GEMINI_API_KEY` — for Gemini models (optional)

## Integration with This Workspace

Use just-prompt when the triad review stage (04_triad_review) needs to compare outputs from different models before making a govern-or-block decision.
