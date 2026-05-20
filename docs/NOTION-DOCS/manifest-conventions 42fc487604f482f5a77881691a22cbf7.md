# manifest-conventions

# Manifest Conventions

The living-document manifest is written as YAML front matter and validated conceptually against `schemas/living-document-manifest.schema.json`.

## Front matter

Front matter must be the first block in every Markdown artifact:

```yaml
---
manifest_version:1.0.0
artifact:
id: example-artifact
title: Example Artifact
type: architecture_spec
owners:
- owner-name
created_at: 2026-01-01
updated_at: 2026-01-01
lifecycle:
state: Draft
promotion_readiness: needs_research
canonicality:
is_canonical:false
provenance:
sources:[]
decisions:[]
rdd:
inputs:[]
requirements:[]
acceptance_criteria:[]
validation:
schema_valid:false
evidence:[]
gates:[]
spatial_system:
domain: vectorworks_to_itwin
source_systems:
- Vectorworks
target_systems:
- iTwin
---
```

## Bottom matter

Bottom matter should be the final block in every Markdown artifact:

```yaml
---
bottom_matter:
change_log:
-date: 2026-01-01
summary: Initial draft.
author: owner-name
open_questions:[]
next_actions:[]
---
```

## Promotion-state source of truth

The `lifecycle.state` field is the source of truth for artifact promotion. Do not infer canonical status from file paths, branch names, or prose headings.

## Spatial metadata

Use `spatial_system` to make spatial assumptions machine-discoverable. Include source systems, target systems, formats, CRS references, semantic layers, and fidelity targets whenever known.