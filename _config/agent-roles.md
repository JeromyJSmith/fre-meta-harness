# Agent Roles

Condensed from `contracts/agent-role-contract.yaml`, `contracts/three-agent-topology.yaml`, and `contracts/front-door-runtime-topology.yaml`.

---

## Governance Triad

These roles govern review, dispatch, and contract authoring. They do **not** originate conversational packets or self-promote to runtime.

| Role | Purpose | Can Dispatch To |
|------|---------|----------------|
| `orchestrator-validator` | Select next bounded slice; keep validation and blocker truth; refuse fake-green outcomes | research, architect |
| `research` | Tighten bounded evidence; verify claims; never upgrade blocked lanes without proof | orchestrator-validator, architect |
| `architect` | Convert reviewed evidence into contracts, schemas, prompts, or governance updates | orchestrator-validator, research |

---

## Front-Door Runtime Roles

These roles operate the inbox-first slice. They receive governed handoffs from the triad; they do **not** self-promote governance.

| Role | Purpose | Routing Lane |
|------|---------|-------------|
| `user-facing-agent` | Handle conversational entry; translate intent into packet | conversation_capture |
| `spec-interpreter` | Parse and validate spec or packet front-matter | conversation_capture |
| `filesystem-router` | Route governed inbox packets to the right runtime role | governed_inbox |
| `intake-mapper` | Map validated packets to stage inputs | governed_inbox |
| `semantic-cartographer` | Index code and map research to semantic graph | governed_inbox |
| `wrapper-synthesizer` | Assemble governed handoff bundles (GATED) | routed_delegation |

---

## Peer Mesh Runtime Roles

These roles operate the same-host peer mesh. Defined in `contracts/agent-role-contract.yaml`.

| Role | Purpose |
|------|---------|
| `peer_mesh_host` | Bootstrap mesh, publish membership |
| `prod_gatekeeper` | Own production-facing exchange, enforce PII stripping |
| `dev_driver` | Drive bounded development tasks within the mesh |
| `mesh_verifier` | Verify mesh state and completion tokens |

---

## Separation Rules

- Governance triad roles cannot originate conversational packets.
- Runtime roles cannot self-promote governance.
- Router cannot invent missing evidence.
- Triad bypass is forbidden.
- Role aliasing is forbidden.
