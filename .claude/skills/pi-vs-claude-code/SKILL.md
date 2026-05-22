---
name: pi-vs-claude-code
description: Pi Coding Agent extension playground. Use when writing, running, or debugging Pi extensions for peer-to-peer communication (coms-net, coms, pi-pi) or multi-agent workflows (agent-team, agent-chain). Bun only — never pnpm/npm.
---

# Pi Coding Agent Extensions

Pi is a coding agent by @mariozechner. This workspace extends it with TypeScript extensions for peer-to-peer communication and multi-agent coordination.

**Not Raspberry Pi.** Pi = Pi Coding Agent CLI.

## Location

`lib/pi-vs-claude-code/` — cloned and installed (`bun install` complete).

## Running Extensions

```bash
cd lib/pi-vs-claude-code
pi -e extensions/<name>.ts
```

## Key Extensions

| Extension | File | Purpose |
|-----------|------|---------|
| coms-net | `extensions/coms-net.ts` (56KB) | HTTP/SSE Pi-to-Pi communication hub |
| coms | `extensions/coms.ts` (51KB) | Peer communication layer |
| pi-pi | `extensions/pi-pi.ts` (22KB) | Direct Pi-to-Pi messaging |
| agent-team | `extensions/agent-team.ts` (22KB) | Multi-agent team coordination |
| agent-chain | `extensions/agent-chain.ts` (24KB) | Sequential agent chaining |

## Environment Variables

Copy `lib/pi-vs-claude-code/.env.sample` → `.env` and fill in:

| Variable | Purpose |
|----------|---------|
| `PI_COMS_NET_AUTH_TOKEN` | Shared secret for coms-net hub (auto-generates for localhost) |
| `PI_COMS_NET_PORT` | Pin server port (optional — leave blank for auto) |
| `PI_COMS_NET_SERVER_URL` | Hub URL for clients (optional — auto-discovers via server.json) |
| `ANTHROPIC_API_KEY` | Required for Claude-backed extensions |
| `OPENAI_API_KEY` | Required for OpenAI-backed extensions |

## Conventions

- Extensions are standalone `.ts` files loaded by Pi's jiti runtime
- Available imports: `@mariozechner/pi-coding-agent`, `@mariozechner/pi-tui`, `@mariozechner/pi-ai`, `@sinclair/typebox`
- Register tools at the top level of the extension function (not inside event handlers)
- Use `isToolCallEventType()` for type-safe `tool_call` event narrowing

## Package Manager

`bun` only. Never npm, yarn, or pnpm.

## Smoke Test (same-host)

```bash
cd lib/pi-vs-claude-code
PI_COMS_NET_AUTH_TOKEN=$(openssl rand -hex 32) pi -e extensions/coms-net.ts
```
