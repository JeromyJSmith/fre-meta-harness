# Stage 03: Semantic Cartography

Index code structure with codegraph, analyze research text with InfraNodus, and map semantic gaps and candidate placements.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../02_research_harvest/output/source-index.json` | Full file | Code roots and lib repos to index |
| Previous stage | `../02_research_harvest/output/feature-matrix.json` | Full file | Text to send to InfraNodus for cluster analysis |
| Reference | `references/subsystem-harness-topology.yaml` | Full file | Subsystem boundaries and runner map |
| Config | `../../_config/proof-vocabulary.md` | Proof states | Vocabulary for tagging outputs |

## Process

1. Load `source-index.json` from `../02_research_harvest/output/`
2. Run `codegraph` on the key source roots listed in source-index (scripts/, contracts/, stages/)
3. Extract cluster summaries: top nodes, cross-stage connections, orphaned files
4. Send feature-matrix text to InfraNodus (`mcp__infranodus__generate_knowledge_graph`) for topical cluster + gap analysis
5. Call `mcp__infranodus__generate_content_gaps` to identify underdeveloped areas
6. Call `mcp__infranodus__develop_conceptual_bridges` for cross-cluster connection opportunities
7. Map candidate placements: which lib tools fill which semantic gaps
8. Emit all artifacts to `output/`

## Audit

| Check | Pass Condition |
|-------|---------------|
| codegraph ran | source-index roots were passed; output shows node counts |
| Cluster count ≥ 3 | InfraNodus returned at least 3 topical clusters |
| Gaps identified | At least 1 gap recorded in infranodus-gap-analysis.json |
| Candidate placements | Each gap has at least one candidate tool from lib/ |

## Outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Semantic graph summary | `output/semantic-graph-summary.json` | codegraph node counts, top connections |
| Candidate placements | `output/candidate-placements.json` | Gap → lib tool mapping |
| InfraNodus gap analysis | `output/infranodus-gap-analysis.json` | Topical gaps from knowledge graph |
| InfraNodus conceptual bridges | `output/infranodus-conceptual-bridges.json` | Cross-cluster bridge concepts |
| InfraNodus live summary | `output/infranodus-live-summary.json` | Cluster overview for routing context |
| InfraNodus research topics | `output/infranodus-research-topics.json` | Generated research questions per gap |
