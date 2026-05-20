# living-document-framework

# Living-Document Framework

The living-document framework treats architectural artifacts as versioned, reviewable system objects rather than static prose. Each document contains machine-readable front matter for identity, lifecycle state, provenance, RDD traceability, validation gates, and spatial-system metadata.

## Document anatomy

Each Markdown artifact should contain:

- A YAML front matter block at the top of the file.
- Human-readable content in the body.
- A YAML bottom matter block at the end of the file.

The front matter describes the current artifact state. The bottom matter captures change history, open questions, and next actions that should not pollute the main specification body.

## Promotion expectations

- `Draft` artifacts can be incomplete but must have an artifact ID and owner.
- `Research` artifacts must cite RDD inputs, research sources, hypotheses, or experiment evidence.
- `Validated` artifacts must pass schema validation and at least one meaningful domain validation gate.
- `Canonical` artifacts must have reviewer approval, implementation traceability, and supersession rules.

## Spatial-system requirements

For Vectorworks-to-iTwin systems, living documents should preserve:

- Source authoring assumptions from Vectorworks files, layers, classes, symbols, stories, and site models.
- Exchange assumptions for IFC, glTF, 3D Tiles, GeoJSON, and iModel intermediates.
- Coordinate reference system, georeferencing, origin, unit, and transform rules.
- Semantic mappings from design objects to iTwin elements, models, categories, and aspects.
- Fidelity targets for geometry, metadata completeness, topology, and round-trip drift.