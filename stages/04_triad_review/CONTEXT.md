# Stage 04: Triad Review

Review all prior stage outputs, formulate ≥3 decision options, and emit a promote-or-block decision with a dispatch message.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Stage 01 | `../01_inbox_intake/output/` | routing-decision.json | Original routing intent |
| Stage 02 | `../02_research_harvest/output/` | All artifacts | Capability evidence baseline |
| Stage 03 | `../03_semantic_cartography/output/` | All artifacts | Semantic gaps and candidate placements |
| Reference | `references/three-agent-topology.yaml` | agent_profiles section | Role responsibilities for each triad member |
| Reference | `references/gap-map-strength.yaml` | Full file | Gap strength taxonomy for decision weighting |
| Config | `../../_config/proof-vocabulary.md` | Full file | Proof states to cite in decision |

## Process

1. Load all prior stage outputs — record any missing artifacts as blockers
2. Identify open questions: missing evidence, unresolved gaps, blocked lanes
3. Formulate at least 3 distinct decision options ranked by risk and evidence strength:
   - Option A (recommended): proceed to wrapper synthesis
   - Option B: return to research harvest with specific gap target
   - Option C: escalate to architect for contract revision
4. Select recommended path with explicit rationale
5. Write `output/promotion-or-blocker.json` with decision, rationale, and blockers
6. Write `output/gap-map-strength-assessment.json` scoring each identified gap
7. Write `output/dispatch-message.md` as the human-readable triad dispatch message

## Audit

| Check | Pass Condition |
|-------|---------------|
| ≥3 options | Decision space contains at least 3 options |
| Recommended path named | Exactly one option marked recommended with rationale |
| Blockers explicit | Any blocked lanes named with exact missing artifact |
| Machine truth preserved | promotion-or-blocker.json is structured JSON, not free text |

## Outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Promotion or blocker | `output/promotion-or-blocker.json` | promote / block decision + rationale |
| Gap map strength assessment | `output/gap-map-strength-assessment.json` | Per-gap strength score |
| Dispatch message | `output/dispatch-message.md` | Human-readable triad decision message |
