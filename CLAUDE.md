---
id: "parent-meta-claude"
slug: "parent-meta-claude"
doctype: "contract"
status: "active"
version: "1.1.0"
owner: "fre-meta-harness"
scope: "portable_parent_wrapper"
library_refs:
  - "library.yaml"
program_refs:
  - "program.md"
prompt_contract_refs:
  - "agent-heavy-run-prompt-index.md"
  - "agent-heavy-run-prompt-schema.md"
  - "agent-heavy-run-prompt.schema.json"
  - "agent-heavy-run-prompt.template.yaml"
  - "copilot-prompting-playbook.md"
comparison_refs:
  - "infranodus-phase-tool-map.json"
substrate_refs:
  - "pixeltable-operational-substrate.md"
governance_contract_refs:
  - "contracts/three-agent-topology.yaml"
  - "contracts/agent-extension-request.yaml"
upstream_local_refs:
  - "external/goal-md"
  - "external/meta-harness"
  - "external/autoresearch-mlx"
---

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working with this repository

This is the `fre-meta-harness` parent wrapper repo. It is a governance/contract scaffold plus a small inbox-protocol service — not a runtime body. Most files are validator-backed contract docs (YAML front matter + Markdown body + `---bottom-matter---`); the validator at `tests/validate_parent_wrapper_contract.py` enforces that scaffold.

### Common commands

Python (use `uv`; `pyproject.toml` targets Python ≥3.12):

```bash
# Run the parent-wrapper contract validator (must pass before claiming state)
uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py

# Score the parent wrapper and emit JSON (writes evaluation/metrics-latest.json on real runs)
uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json

# Scan the inbox/ directory, validate packets, and emit routing + delegation artifacts
uv run python scripts/watchers/inbox_router.py
# equivalent: bun run scan:inbox  (or  bun run check:inbox)
```

Inbox-protocol service + dashboard (two terminals):

```bash
# FastAPI service on :8787 (governs the inbox queue, scan, routing, delegations)
bun run dev:service
# Bun-served HTML dashboard on :3000 that proxies /api/* to the FastAPI service
bun run dev:app
# Health checks
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:3000/health
```

Refresh tool-health and the ratchet (most ratchet shell scripts hard-code the *original* macOS body path `/Volumes/PixelTable/VW_iTwin_Bridge/meta`; running them from a fresh clone requires editing `ROOT=` in `scripts/run-parent-ratchet.sh` and `scripts/run-copilot-parent-ratchet.sh`, or invoking the Python entry points directly).

### Mutable surface

A ratchet run may **only** edit these paths (see `program.md` and `scripts/score-parent-wrapper.py`):

- Root docs: `GOAL.md`, `domain_spec.md`, `program.md`, `library.yaml`, `agentics-library.md`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `MEMORY.md`, `GOLDENPATH.md`
- Trees: `source/`, `schemas/`, `examples/`, `expected-failures/`, `tests/`, `evaluation/`, `promotion/`, `prompts/`, `runs/`, `scripts/`

Everything under `external/` is a **read-only** git submodule (`goal-md`, `meta-harness`, `autoresearch-mlx`) — never edit those clones.

### Doc-shape rules enforced by the validator

- `README.md`, `AGENTS.md`, `CLAUDE.md`, `GOAL.md`, `GOLDENPATH.md`, `MEMORY.md` must all exist and carry YAML front matter, a body, and a `---bottom-matter---` block with `gate_progress` and `validation_status`-shaped fields.
- `AGENTS.md` and `CLAUDE.md` must explicitly mention the governance triad (markers: "triad" / "three-agent") and name all three triad role IDs (`orchestrator-validator`, `research`, `architect`).
- Every governed prompt and handoff in `prompts/` / `agent-heavy-run-prompt.*` / `architect-review-handoff-prompt.*` must validate against the matching schema in `schemas/`, with paired `*.valid.json` and `*.invalid.*.json` fixtures under `examples/` and `expected-failures/`.
- `runs/iterations.jsonl` is real JSONL (one compact object per line); doc-only edits do not count as ratchet improvement.

### Big-picture architecture

Two layers live side-by-side in this repo:

1. **Governance layer (contracts + doctrine, no live runtime).** The parent scaffold (`README.md`, `AGENTS.md`, `CLAUDE.md`, `GOAL.md`, `GOLDENPATH.md`, `MEMORY.md`, `program.md`, `library.yaml`) plus the `contracts/` family and matching `schemas/` define how parent governance works. The validator pairs every contract with a JSON Schema and `examples/*.valid.json` + `expected-failures/*.invalid.*.json` fixtures (this is the "seven-part proof package": `source/`, `schemas/`, `examples/`, `expected-failures/`, `tests/`, `evaluation/`, `promotion/`).

2. **Inbox-protocol service (the only running code).** Markdown packets land in `inbox/` (suffixes like `.handoff.md`, `.plan.md`, `.brainstorm.md`, `.checkpoint.md`, …). The flow is:

   ```
   inbox/*.{handoff,plan,brainstorm,…}.md
        │
        ▼   service/inbox_runtime.py: parse front+body+bottom, validate, eval gates
   scan_inbox_packets()  →  build_routing_artifacts()  →  write_router_outputs()
        │                          │                            │
        │                          │                            ▼
        │                          │                evaluation/tool-health/inbox-protocol/
        │                          │                  ├── latest-scan.json
        │                          │                  ├── gate-status.json
        │                          │                  ├── packets/<slug>.json
        │                          │                  ├── routing/all.json + <slug>.json
        │                          │                  └── delegations/all.json + <slug>.json
        │                          │
        │   service/main.py (FastAPI on :8787) exposes the same view as JSON:
        │       /health  /api/inbox/queue  /api/inbox/packets  /api/routing/results
        │       /api/delegations  /api/dashboard  POST /api/inbox/scan
        │
        ▼
   app/server.ts (Bun on :3000) serves a static HTML dashboard and proxies /api/* to FastAPI.
   scripts/watchers/inbox_router.py is the CLI form of the same scan+write pipeline.
   ```

   `ROLE_IDS` in `service/inbox_runtime.py` enumerates the only producer roles a packet may declare: the three triad roles plus the six front-door runtime roles (`user-facing-agent`, `spec-interpreter`, `filesystem-router`, `intake-mapper`, `semantic-cartographer`, `wrapper-synthesizer`). Routing status is `routed` / `needs_clarification` / `blocked`, derived from the gates inside `---bottom-matter---` plus front-matter validation errors.

3. **Ratchet loop (governance-evaluation).** `program.md` defines a keep-or-revert loop: read `runs/iterations.jsonl` → run the validator → run the scorer → propose one bounded change inside the mutable surface → revalidate → append a JSONL row → repeat until ≥2 real non-dry cycles plus 2 consecutive non-improving cycles, or an explicit blocker. Reports land in `evaluation/copilot-ratchet-report.json` and `evaluation/tool-health/status.json`. Dry runs are explicitly **not** proof.

### Things that look like bugs but aren't

- The hard-coded `/Volumes/PixelTable/VW_iTwin_Bridge/meta` paths in `scripts/run-parent-ratchet.sh`, `scripts/run-copilot-parent-ratchet.sh`, and `program.md` step 2 point at the *child body* on the original author's machine, not this repo. Use the Python entry points directly when working from a fresh clone.
- `package.json` has no `package-lock.json` / `bun.lockb`; the Bun app has zero npm dependencies (it only uses the Bun runtime + `fetch`). The Python side is the dependency surface.
- `meta-repomix.xml` (600 KB+) is a generated repo snapshot — not source to edit.

---

Parent wrapper operational note:

- start with the parent scaffold and the active body registry
- use the governed prompt schema for every heavy run
- use `program.md` for every real parent ratchet run
- use InfraNodus at every lifecycle gate
- treat Pixeltable as the durable substrate
- read the local imported upstream authority clones before modifying the ratchet
- read and write durable wrapper artifacts before claiming state
- keep governance triad roles separate from front-door runtime roles and from
  peer-mesh runtime roles
- send any self-extension proposal through
  `contracts/agent-extension-request.yaml` as a governed request only
- treat inbox packets as front-door governance artifacts until a structured
  routing decision and delegation bundle explicitly hand off to runtime
- do not claim child-runtime adoption or activation from parent artifacts alone

Governance triad:

- `orchestrator-validator` governs parent review, handoff readiness, and
  blocker truth
- `research` gathers bounded evidence and dependency truth for review
- `architect` shapes parent contracts, prompts, and handoff artifacts

Front-door runtime roles for the inbox-first slice are:

- `user-facing-agent`
- `spec-interpreter`
- `filesystem-router`
- `intake-mapper`
- `semantic-cartographer`
- `wrapper-synthesizer`

The older peer-mesh runtime roles remain defined in
`contracts/agent-role-contract.yaml` and are not overwritten by this slice.

Handoff rule:

- when execution is needed, the triad emits an inbox packet, routing decision,
  and delegation bundle instead of replacing runtime role definitions
- use the inbox/front-door contract family when that handoff begins:
  `contracts/inbox-packet.yaml`,
  `contracts/inbox-routing-decision.yaml`,
  `contracts/delegation-bundle.yaml`, and
  `contracts/front-door-runtime-topology.yaml`
- parent-only work stops at governed contracts, docs, prompts, handoffs,
  review outputs, extension requests, and promotion or blocker evidence unless
  a downstream runtime owner is explicitly named

---bottom-matter---
status_summary:
  completeness: 0.98
  confidence: high
  doc_state: active_contract

gate_progress:
  - gate_id: schema_gate
    status: green
    notes: "Parent execution rules and governed packet shape are explicit."
  - gate_id: scope_gate
    status: green
    notes: "Required authority references and parent-only scope remain explicit."
  - gate_id: consumer_gate
    status: green
    notes: "Front-door runtime consumers and triad separation are declared."
  - gate_id: evidence_gate
    status: green
    notes: "Contract validator checks packet, routing, and delegation surfaces while runtime adoption claims remain bounded."
  - gate_id: freshness_gate
    status: green
    notes: "State is backed by current parent artifacts rather than implied child-runtime integration."
  - gate_id: readiness_gate
    status: green
    notes: "No dangling parent execution references remain and inbox-first handoff rules are explicit."

open_questions: []

pending_validations:
  - "Rerun parent contract validator after governance topology and tool-health doctrine changes."

promotion_criteria:
  - "Operational rules survive transport into the standalone parent repo."
  - "Governance triad and runtime mesh roles remain explicitly separated."

blocked_by:
  - "Live InfraNodus MCP analysis remains optional; the bounded local parent-layer substitute is the default until runtime access is intentionally configured."

next_iteration:
  owner: "codex"
  objective: "Keep this parent operational note aligned with the published wrapper, its governance topology, and its tool-health evidence."
