# Stage 01: Inbox Intake

Validate an incoming inbox packet, determine its routing lane, and emit a routing decision plus delegation bundle.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Inbox | `../../inbox/` | Dropped file (full) | The artifact to route |
| Reference | `references/inbox-packet.yaml` | Full file | Required front-matter schema for packets |
| Reference | `references/inbox-routing-decision.yaml` | Full file | Routing decision output schema |
| Reference | `references/delegation-bundle.yaml` | Full file | Delegation bundle output schema |
| Config | `../../_config/agent-roles.md` | Front-door runtime roles section | Who receives the routed packet |

## Process

1. Read the dropped file from `../../inbox/`
2. Validate front-matter against `references/inbox-packet.yaml` — record any missing required fields as blockers
3. Determine routing lane from packet contents:
   - `conversation_capture` → `user-facing-agent` or `spec-interpreter`
   - `governed_inbox` → `filesystem-router`
   - `triad_review` → `orchestrator-validator`, `research`, `architect`
4. Write `output/routing-decision.json` with lane, target roles, and any blockers
5. If lane is `governed_inbox`: write `output/delegation-bundle.json` pairing the packet with target runtime roles
6. Move processed file to `../../outbox/processed/`

## Audit

| Check | Pass Condition |
|-------|---------------|
| Schema valid | All required packet front-matter fields present |
| Lane assigned | Exactly one routing lane selected |
| Target roles named | At least one role from `_config/agent-roles.md` front-door list named |
| Blockers explicit | Missing fields recorded in routing-decision.json, not silently dropped |

## Outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Routing decision | `output/routing-decision.json` | Lane, target roles, blockers |
| Delegation bundle | `output/delegation-bundle.json` | Packet + role pairing (governed_inbox lane only) |
