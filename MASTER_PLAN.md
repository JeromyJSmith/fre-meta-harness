---
id: "parent-meta-master-plan"
slug: "parent-meta-master-plan"
doctype: "master_plan"
status: "active"
version: "1.0.0"
owner: "fre-meta-harness"
scope: "portable_parent_wrapper"
generated_at: "2026-05-22"
infranodus_analysis: "live_mcp"
git_state: "clean — commit 589f6b8 pushed to main"
---

# MASTER PLAN — fre-meta-harness

> **Objective:** Get the system fully organized and build-ready so that when a
> project is dropped into `inbox/`, it flows through the complete pipeline
> from intake to governed promotion — no manual intervention required.

---

## 1. Git State

**Status: CLEAN ✓**

- Branch: `main`
- Remote: `git@github.com:JeromyJSmith/fre-meta-harness.git`
- Last commit: `589f6b8` — 132 files changed, 18 549 insertions
- All surfaces committed and pushed.

---

## 2. InfraNodus Live Analysis (2026-05-22)

Graph: 10 clusters · 150 nodes · 392 edges · modularity 0.554 · **diversified**

### Topical Clusters (by influence)

| Rank | Cluster | Key Terms | BC% |
|------|---------|-----------|-----|
| 1 | **Source Quality** | consume source ready quality pipeline index folder scorer | 15% |
| 2 | **Contract Handoff** | wrapper prompt contract handoff synthesizer bundle wrap triad | 14% |
| 3 | **Build Tool** | parent py tool artifact kb build infranodus health | 12% |
| 4 | **Harvest Capability** | harvest subsystem research emit map capability matrix placement | 12% |
| 5 | **ETL Clean** | runtime etl door intake reusable front project clean | 11% |
| 6 | **Require Blocked** | blocked explicit pi coms require required net fail | 11% |
| 7 | **Meta Library** | file meta harness bridge red library md untracked | 8% |
| 8 | **Mesh Device** | mesh peer host role bounded device active cross | 8% |
| 9 | **Routing Inbox** | inbox packet routing extract decision delegation protocol normalize | 7% |
| 10 | **Semantic Graph** | semantic cartography graph produce | **2% ← WEAKEST** |

### Top Influential Nodes (hub concepts)

`consume` (0.19) → `harvest` (0.12) → `parent` (0.11) → `source` (0.11) →
`inbox` (0.10) → `wrapper` (0.10) → `py` (0.08)

### Content Gaps to Bridge

| Gap | From | To | Implication |
|-----|------|----|-------------|
| G1 | ETL Clean | Require Blocked | Intake/ETL has no bridge to blocked-dep resolution layer |
| G2 | Require Blocked | Meta Library | Blocked state not wired into file/library organization layer |
| G3 | ETL Clean | Mesh Device | Intake pipeline not connected to peer mesh runtime |
| G4 | Project Ingestion | Semantic Mapping | Ingestion flow has no bridge to semantic cartography (2% cluster) |
| G5 | Project Ingestion | Mesh Operations | Ingestion pipeline not wired to peer mesh operations |
| G6 | System Placement | Project Ingestion | Subsystem placements not feeding the ingestion flow |

**Root cause:** Semantic cartography is the most underdeveloped surface. Closing
G4 and G6 first will cascade through G3 and G5.

---

## 3. Subsystem Harness — Wrapping Map

Four subsystems defined in `source/subsystems/registry.json`.
All are `defined_not_activated`. Activation order is sequential.

### Subsystem 1: `intake_etl`
**State:** `defined_not_activated`
**Wraps:** Governed inbox drops + consume-folder assets → normalized packets +
provenance records + source-index

```
inbox/ (front door)
  └─ intake-mapper routes packet
       └─ intake_etl normalizes
            ├─ evaluation/research/harvest-manifest.json
            └─ evaluation/research/compiled/source-index.json
```

**Consumes:**
- `contracts/inbox-packet.yaml`
- `contracts/inbox-routing-decision.yaml`
- `contracts/delegation-bundle.yaml`

**Emits:**
- `evaluation/research/harvest-manifest.json`
- `evaluation/research/compiled/source-index.json`

**Reusable infra (ready now):**
- `colbymchenry/codegraph` — semantic index of code
- `oxc-project/oxc` — JS/TS AST parse + transform
- `oven-sh/bun` — runtime + package manager

**Activation runner needed:** `scripts/run-intake-etl.sh` or
`scripts/watchers/inbox_router.py` extended with extract logic.

**Current blocker:** No runner connects `inbox_router.py` output → `intake_etl`
normalize → `source-index` emit. The watcher scans but doesn't invoke ETL.

---

### Subsystem 2: `research_harvest`
**State:** `defined_not_activated`
**Wraps:** Normalized evidence → capability-harvest + feature-matrix + gap-placement-map

```
evaluation/research/harvest-manifest.json
  └─ research_harvest compiles
       ├─ evaluation/research/compiled/capability-harvest.json
       ├─ evaluation/research/compiled/feature-matrix.json
       └─ evaluation/research/compiled/gap-placement-map.json
```

**Consumes:**
- `evaluation/research/harvest-manifest.json`
- `contracts/research-packet-manifest.yaml`
- `source/subsystems/registry.json`

**Emits:**
- `evaluation/research/compiled/capability-harvest.json`
- `evaluation/research/compiled/feature-matrix.json`
- `evaluation/research/compiled/gap-placement-map.json`

**Reusable infra (gated):**
- `VectifyAI/OpenKB` — document compilation + persistent knowledge base
- `sandeco/reversa` — legacy-to-spec multi-agent framework

**Activation runner needed:** Connect `consume_source_quality_lib.py` →
`build_operational_feature_matrix()` → research compiled outputs.

**Current blocker:** `consume_source_quality_lib.py` exists and is READY but no
runner calls it as the harvest step. The thin CLI scripts are wired but not
orchestrated into the subsystem flow.

---

### Subsystem 3: `semantic_cartography`
**State:** `defined_not_activated` · **WEAKEST CLUSTER (2%)**
**Wraps:** Code + docs + compiled research → semantic graphs + entity maps +
subsystem candidate placements

```
evaluation/research/compiled/source-index.json
evaluation/research/compiled/feature-matrix.json
  └─ semantic_cartography produces
       ├─ subsystem candidate placements
       ├─ semantic graph-ready summaries
       └─ wrapper binding inputs (→ subsystem 4)
```

**Consumes:**
- `evaluation/research/compiled/source-index.json`
- `evaluation/research/compiled/feature-matrix.json`
- `contracts/subsystem-harness-topology.yaml`

**Emits:**
- Subsystem candidate placements
- Semantic graph summaries
- Wrapper binding inputs

**Reusable infra (ready now):**
- `colbymchenry/codegraph` — pre-indexed knowledge graph
- `facebook/pyrefly` — Python type checker + language server
- `oxc-project/oxc` — JS/TS semantic extraction

**Activation runner needed:** `scripts/run-semantic-cartography.sh` — invoke
`codegraph` + `pyrefly` on source-index, emit semantic summaries.

**This is the highest-priority gap to close** (G4, G6). Closing it unlocks
wrapper synthesis and completes the pipeline.

---

### Subsystem 4: `wrapper_synthesizer` ← GATED
**State:** `late_bound_not_activated`
**Gate:** Explicit triad review required before activation.
**Wraps:** Approved subsystem outputs → wrapper contracts + prompts + handoff bundles

**Activation criterion:**
- Subsystems 1–3 must produce their emitted artifacts
- Triad orchestrator-validator must issue a delegation-bundle
- Then wrapper synthesis runs and emits governed handoff bundles

---

## 4. Inbox Pipeline — Clean State Design

### Rule: Inbox is the front door only

The inbox must be clean (empty of processed material) when no project is loaded.
A project enters the system by being dropped into `inbox/`.

### Current Inbox Contents → Disposition

| Item | Type | Action |
|------|------|--------|
| `prompting-tools.consume/` | Research material | Move → `external/prompting-tools/` |
| `transcribe.consume/` | Transcribed source | Move → `external/transcribed/` |
| `file-system-structure-research.consume/` | Research | Move → `external/filesystem-research/` |
| `claude-code-portable-peer-mesh-schema/` | Schema research | Move → `external/peer-mesh-schema/` |
| `2026-05-21-operational-capability-matrix-and-schemas.handoff.md` | Processed handoff | Archive → `outbox/processed/` |
| `2026-05-21-pipeline-ideas-and-implementation.handoff.md` | Processed handoff | Archive → `outbox/processed/` |
| `consuming-layer.plan.*` | Consumed plan | Archive → `outbox/processed/` |
| `FRE-META-HARNESS_PLAN.plan.*` | Consumed plan | Archive → `outbox/processed/` |
| `fre-meta-harness_plus_inbox.plan.*` | Consumed plan | Archive → `outbox/processed/` |
| `MetaHarness possible improvement blog.md` | Reference material | Move → `external/reference/` |
| `prompt-candidate-Preflight-Step-0.*` | Governed prompt | Move → `prompts/` |

**After cleanup:** `inbox/` contains only `.gitkeep`. Ready for project drop.

### Inbox → Pipeline Flow (when a project is dropped)

```
inbox/
  └─[project files dropped here]
       │
       ▼
  scripts/watchers/inbox_router.py
  (bun run scan:inbox  OR  uv run python scripts/watchers/inbox_router.py)
       │
       ├─ validates against contracts/inbox-packet.yaml
       ├─ emits contracts/inbox-routing-decision.yaml
       └─ emits contracts/delegation-bundle.yaml
            │
            ▼
       SUBSYSTEM 1: intake_etl
       ├─ normalizes source material
       ├─ emits harvest-manifest.json
       └─ emits source-index.json
            │
            ▼
       SUBSYSTEM 2: research_harvest
       ├─ compile_source_quality_lib.build_operational_feature_matrix()
       ├─ emits capability-harvest.json
       ├─ emits feature-matrix.json
       └─ emits gap-placement-map.json
            │
            ▼
       SUBSYSTEM 3: semantic_cartography
       ├─ codegraph index on source-index
       ├─ pyrefly type analysis (Python sources)
       ├─ emits semantic graph summaries
       └─ emits subsystem candidate placements
            │
            ▼
       InfraNodus live analysis
       (scripts/build-parent-infranodus-artifacts.py)
       ├─ generates knowledge graph
       ├─ identifies content gaps
       └─ emits gap-map-strength report
            │
            ▼
       TRIAD REVIEW (orchestrator-validator)
       ├─ reviews capability-harvest + gap-map + semantic placements
       ├─ issues promotion or blocker decision
       └─ on PROMOTE → delegates to wrapper_synthesizer
            │
            ▼
       SUBSYSTEM 4: wrapper_synthesizer (GATED)
       ├─ assembles governed handoff bundles
       ├─ emits wrapper binding candidates
       └─ emits governed prompts for child runtime
            │
            ▼
       outbox/ — handoff bundles ready for child body cell
```

---

## 5. RED → GREEN Pipeline

### RED Items (must fix before ingestion)

| ID | Item | Owner | Blocker |
|----|------|-------|---------|
| R1 | ~~Git uncommitted~~ | done | ✓ Fixed — 589f6b8 pushed |
| R2 | Inbox not clean | intake-mapper | Processed items still in inbox/ |
| R3 | `intake_etl` has no activation runner | dev_driver | No script wires inbox_router → ETL normalize |
| R4 | `research_harvest` not orchestrated | dev_driver | consume_source_quality_lib not called as subsystem step |
| R5 | `semantic_cartography` not activated | dev_driver | Weakest cluster (2%), no runner exists |
| R6 | Cross-device peer mesh blocked | peer_mesh_host | Needs PI_COMS_NET_AUTH_TOKEN + hub URL |
| R7 | No validator coverage for 14 new schemas | mesh_verifier | tests/ has slices but no CI run |

### YELLOW Items (scaffolded, need wiring)

| ID | Item | Notes |
|----|------|-------|
| Y1 | `inbox_router.py` scans but doesn't invoke ETL | Needs consume pipeline integration |
| Y2 | `consume_source_quality_lib.py` ready but not orchestrated | Wire as research_harvest runner |
| Y3 | `codegraph` identified as best fit | Not yet installed or invoked |
| Y4 | InfraNodus live MCP now unblocked | Was blocked_pass, now LIVE |
| Y5 | `scripts/tool_health_probe_lib.py` exists | Wire into CI / scheduled runs |

### GREEN Items (operational, harvest-ready)

| ID | Item | Evidence |
|----|------|---------|
| G1 | Git main clean + pushed | 589f6b8 |
| G2 | Same-host peer mesh (4 roles) | evaluation/tool-health/peer-mesh-local.json |
| G3 | Parent validator + scorer | tests/validate_parent_wrapper_contract.py |
| G4 | InfraNodus corpus build | scripts/build-parent-infranodus-artifacts.py |
| G5 | Tool health refresh cycle | scripts/refresh-parent-tool-health.py |
| G6 | Governance contracts complete (5 new) | contracts/ |
| G7 | 14 new schemas with valid/invalid examples | schemas/ + examples/ |
| G8 | 10 governed prompts landed | prompts/ |
| G9 | Inbox protocol gate-status + scan | evaluation/tool-health/inbox-protocol/ |
| G10 | consume_source_quality_lib.py (27KB) ready | scripts/ |
| G11 | GitNexus bounded_pass | evaluation/tool-health/status.json |
| G12 | Graphify bounded_pass | evaluation/tool-health/status.json |
| G13 | Local runners harvested | evaluation/tool-health/local-runners.json |

---

## 6. Next Session Activation Sequence

Run in order. Each step produces evidence the next step consumes.

```bash
# Step 0 — Verify clean state
git status  # should be clean
uv run --isolated --with jsonschema --with pyyaml \
  python tests/validate_parent_wrapper_contract.py

# Step 1 — Clean inbox
# Move processed consume folders to external/
# Archive processed handoffs to outbox/processed/
# See Section 4 disposition table above

# Step 2 — Activate intake_etl
# Drop project into inbox/
bun run scan:inbox
# OR
uv run python scripts/watchers/inbox_router.py

# Step 3 — Run research harvest
uv run python scripts/ingest-consume-sources.py
uv run python scripts/compile-operational-feature-matrix.py
uv run python scripts/extract-consume-source-quality.py

# Step 4 — Refresh InfraNodus analysis
uv run python scripts/build-parent-infranodus-artifacts.py

# Step 5 — Score the wrapper
uv run --isolated --with jsonschema --with pyyaml \
  python scripts/score-parent-wrapper.py --json

# Step 6 — Refresh all tool health
uv run python scripts/refresh-parent-tool-health.py

# Step 7 — Run full ratchet
bash scripts/run-parent-ratchet.sh
```

---

## 7. Pi-to-Pi Communication State

**Same-host peer mesh: ACTIVE**
- All 4 roles registered: peer_mesh_host, prod_gatekeeper, dev_driver, mesh_verifier
- Operations wired: list_agents, send_command, send_prompt, await_response
- Completion tokens enforced: done, failed, needs-human
- Evidence: `evaluation/tool-health/peer-mesh-local.json`
- Run: `bash scripts/run-parent-peer-mesh-local.sh`

**Cross-device (Pi-to-Pi) peer mesh: BLOCKED**
- Blocker: `PI_COMS_NET_AUTH_TOKEN` env var not set
- Blocker: Hub URL not declared
- Implementation: `scripts/parent_peer_mesh_runtime.py` (43KB) — runtime is READY
- To unlock: Set `PI_COMS_NET_AUTH_TOKEN` + declare hub URL in environment

**claude-peers MCP: LIVE**
- Available in this session
- Can be used for same-machine peer coordination immediately

---

## 8. Capability Harvest — What Can Be Harvested Now

These capabilities are ready to be used, packaged, or composed today:

| Capability | Entry Point | Output |
|-----------|-------------|--------|
| Same-host peer mesh | `scripts/run-parent-peer-mesh-local.sh` | Governed peer exchange log |
| Parent validator | `tests/validate_parent_wrapper_contract.py` | Pass/fail JSON |
| Wrapper scorer | `scripts/score-parent-wrapper.py --json` | Score JSON |
| InfraNodus corpus | `scripts/build-parent-infranodus-artifacts.py` | Gap analysis + live graph |
| Tool health probe | `scripts/refresh-parent-tool-health.py` | status.json |
| Source quality | `scripts/consume_source_quality_lib.py` | Feature matrix + quality report |
| Inbox protocol | `scripts/watchers/inbox_router.py` | Routing + delegation artifacts |
| Full ratchet | `scripts/run-parent-ratchet.sh` | Copilot ratchet report |
| Visualization | `scripts/build-visualization-artifacts.py` | dashboard-data.js |

---
bottom-matter:
  status_summary:
    completeness: 1.0
    confidence: high
    doc_state: active_master_plan
  infranodus_session: live_mcp_2026-05-22
  git_commit: 589f6b8
  next_action: clean inbox, then activate intake_etl subsystem runner
