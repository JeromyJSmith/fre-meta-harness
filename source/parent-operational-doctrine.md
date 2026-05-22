# Parent operational doctrine

This file is the canonical source of truth for parent-wrapper operational
claims. `README.md`, `GOAL.md`, `program.md`, and `library.yaml` should point
here instead of restating runtime and tool-health doctrine in full.

## Runtime truth

| Lane | State | Proof rule | Evidence |
|---|---|---|---|
| `peer_mesh_local.same_host` | active | Claim only after a fresh bounded same-host run | `evaluation/tool-health/peer-mesh-local.json` |
| `inbox_protocol.same_host` | active | Claim only after a fresh watcher scan and routing emission | `evaluation/tool-health/inbox-protocol/latest-scan.json` |
| `peer_mesh_local.cross_device` | blocked | Keep blocked until authenticated transport is actually configured and proven | `evaluation/tool-health/status.json` |
| `inbox_protocol.cross_device` | blocked | Keep blocked until authenticated remote routing exists | `evaluation/tool-health/status.json` |

Do not treat fixture-only checks, dry evals, or file presence alone as proof of
live runtime activation.

## Launcher truth

- Root `.mcp.json`: **absent in this repo unless a real file exists**
- Honest launcher surfaces today:
  - `app/server.ts`
  - `service/main.py`
  - `scripts/watchers/inbox_router.py`
  - `scripts/run-parent-peer-mesh-local.sh`
  - `package.json` scripts

When `.mcp.json` is absent, say so explicitly and point to these entrypoints
instead of inventing an MCP launcher path.

## Local-first default path

Run these from the repo root:

```bash
uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py
uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json
uv run --isolated --with jsonschema --with pyyaml python scripts/refresh-parent-tool-health.py
uv run python -m unittest discover -s tests -p 'test_*.py'
uv run python scripts/watchers/inbox_router.py
```

These are the default parent commands because they stay local and produce durable
artifacts under `evaluation/`, `promotion/`, and `runs/`.

## Optional and credential-required paths

| Lane | Default truth | Upgrade requirement | Notes |
|---|---|---|---|
| GitNexus | bounded fixture probe | fresh full-repo probe without external warnings | Full-repo warnings stay weaker than the bounded fixture truth |
| Graphify | bounded fixture probe | broader verified coverage if intentionally added | Bounded fixture output is not full-repo activation |
| InfraNodus live MCP | blocked | authenticated live MCP session and provider config | Use the bounded local substitute when live is not proven |
| Agent-eval smoke/live | blocked unless configured | required provider credentials and sandbox prerequisites | `dry` remains the strongest default local evidence |

## Artifact refresh rule

Whenever runtime truth, launcher truth, or optional-lane status changes, refresh:

- `evaluation/tool-health/status.json`
- `evaluation/validation-report.json`
- `promotion/readiness.json`

If the change affects docs or runbooks, update this file first and then point the
summary docs back here.
