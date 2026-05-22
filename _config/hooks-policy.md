# Hooks Policy

Condensed from `contracts/hook-manifest.yaml`.

## Global Policy

| Setting | Value |
|---------|-------|
| Fail mode | `fail_loud` — hooks that fail block the operation and emit an error |
| Evidence artifact required | Yes — every hook must point to an `evidence_artifact` file |
| Verification boundary required | Yes — every hook must specify completion_token behavior |

## Hook Inventory

| Hook ID | Event | Runtime Actor | Required Capabilities |
|---------|-------|--------------|----------------------|
| `peer-session-start` | session_start | peer_mesh_host | pi-vs-claude-code, the-library |
| `peer-membership-refresh` | peer_join | peer_mesh_host | pi-vs-claude-code, the-library |
| `peer-prompt-guard` | before_send_prompt | prod_gatekeeper | pi-vs-claude-code, claude-code-hooks-mastery |
| `completion-verification` | after_tool_use | mesh_verifier | the-library |
| `inbox-packet-validation` | before_inbox_drop | filesystem-router | the-library |
| `triad-dispatch-guard` | before_triad_dispatch | orchestrator-validator | the-library |

## Claude Code Hook Wiring

Hook scripts are in `.claude/hooks/`. Wired in `.claude/settings.json` under:
- `PreToolUse` → `pre-tool-use.sh`
- `PostToolUse` → `post-tool-use.sh`
- `Stop` → completion verification

## Policy Contracts Referenced

- `contracts/policy-decision.yaml`
- `contracts/observability-event.yaml`
