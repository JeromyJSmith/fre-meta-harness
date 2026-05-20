# finishing-touches.plan.explainer.md

## Plan file explainer (human readable)

A plan is a markdown document with:

- **Top YAML frontmatter** (name, status, owners, overview)
- **Narrative sections** (Inputs, Acceptance criteria, Steps, etc.)
- **Bottom-matter YAML config** in a fenced `yaml` block labeled `plan-config`

### Why bottom-matter exists

It holds execution knobs (budget/logging/scoring) without disrupting the plan narrative.