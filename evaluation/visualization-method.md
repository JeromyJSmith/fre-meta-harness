# Visualization Method

This dashboard is intentionally built from verified, public visualization
systems instead of an improvised one-off stack.

## Chosen Sources

1. **3D network graph**
   - Repo: `vasturiano/3d-force-graph`
   - Why: proven interactive WebGL graph renderer with documented examples for
     focus-on-node, directional arrows, dynamic graph data, DAG layouts, and
     scene interaction.
   - Source:
     - https://github.com/vasturiano/3d-force-graph
     - Repo example family used:
       - dynamic data changes
       - force-directed tree (DAG mode)
       - pause / resume animation

2. **Charts and dashboard panels**
   - Repo: `apache/echarts`
   - Docs: `apache/echarts-doc`
   - Why: proven browser charting stack with official line-chart examples,
     dynamic update guidance, relationship chart support, mobile-ready
     interactions, and multi-series dashboard composition.
   - Sources:
     - https://github.com/apache/echarts
     - https://github.com/apache/echarts-examples
     - https://github.com/apache/echarts-doc
     - https://echarts.apache.org/handbook/en/how-to/chart-types/line/basic-line/
     - https://echarts.apache.org/handbook/en/how-to/chart-types/line/area-line/
     - https://echarts.apache.org/handbook/en/how-to/data/dynamic-data/
     - https://echarts.apache.org/en/feature.html

3. **Entity/relationship semantics and gap-analysis framing**
   - Product: InfraNodus
   - Why: the parent wrapper already uses InfraNodus as the graph-intelligence
     layer, so node/edge meaning should follow its text-to-graph, knowledge-gap,
     and cluster logic instead of an arbitrary network schema.
   - Sources:
     - https://infranodus.com/docs
     - https://infranodus.com/mcp/tools
     - https://infranodus.com/videos/text-analysis-ai
     - https://infranodus.com/extension

## Applied Combination

- **ECharts** renders the improvement loop, component breakdown, and lifecycle
  tool coverage, and the live InfraNodus cluster strength view.
- **3d-force-graph** renders the interactive entity/relationship network with
  click-to-focus and directional particle emphasis for blockers and gaps.
- **InfraNodus semantics** define the graph contents:
  - topical clusters
  - content gaps
  - gate-to-tool mappings
  - proof-package-to-tool mappings
  - promotion blockers
  - live main concepts
  - live conceptual gateways
  - live influential nodes

## Verified Technique Mapping

- `3d-force-graph`:
  - camera focus on node click
  - directional arrows
  - directional particles for stressed relations
- `Apache ECharts`:
  - multi-series line chart for loop improvement
  - horizontal bars for component scoring
  - grouped bars for gate coverage and cluster strength
- `InfraNodus`:
  - actual MCP-generated graph statistics
  - actual topical clusters
  - actual content gaps
  - actual main concepts and gateways

## Why This Is Better Than A Single Tutorial Clone

- It separates the jobs correctly:
  - charting for quantitative series
  - force graph for exploratory relationships
  - InfraNodus for structural meaning
- It stays honest when the ratchet has not yet produced real non-dry cycles.
- It can update from generated local artifacts instead of hand-edited mock
  data.
