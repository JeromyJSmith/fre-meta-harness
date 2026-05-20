# FS (do not read by default)

This page is a container for the harness filesystem tree (export structure). Open it only when you need to inspect or modify files.

<aside>
📎

**Purpose**: Container page that holds the **full filesystem tree** of the Portable Harness Package for export.

**Inputs**: All file/pages representing folders/files in the portable package.

**Outputs**: A complete, navigable tree that exports into directories/files.

**Validation tie-in**: Contract validation (tree completeness), Drift detection (unexpected additions/removals), Publish decision (sendable package).

**Failure modes**: Missing nodes silently remove required files from the export; unclear tree causes boot sequence drift.

**Update / upstream path**: Tree edits must be accompanied by an Update Artifact describing adds/moves/removals and validation results.

</aside>

```yaml
page_contract:
  purpose: "Portable package filesystem tree container."
  inputs: ["All package nodes (pages-as-files/folders)"]
  outputs: ["Exportable directory/file hierarchy"]
  validation_tie_in:
    gates: ["Contract validation", "Drift detection"]
    checks:
      - "Required nodes exist in expected locations"
  failure_modes:
    - "Missing required file pages"
    - "Broken boot order due to moved entrypoints"
  upstream:
    update_artifact: "Tree-change update artifact"
    proposal_path: "Record move/add/remove + rerun fresh export validation"
```

[schemas](schemas%20465c487604f483efadf4819aa439f492.md)

[.claude](claude%20091c487604f482ceade4813d6b684286.md)

[reports](reports%20b65c487604f48339a83e8156d1b7b992.md)

[[CLAUDE.md](http://CLAUDE.md)](CLAUDE%20md%2097fc487604f4832993ea8138033ec017.md)

[docs](docs%203e2c487604f48303a97281ba828ed8d1.md)

[compiler](compiler%2017ec487604f4827f959e81f1d8c60104.md)

[examples](examples%20dcac487604f482e8ab9281624b558d0c.md)

[runs](runs%205e6c487604f4831dab0c81ff61aa8648.md)

[backend](backend%205b6c487604f482fabc5b01a83a2bd3e8.md)

[databases](databases%20c48c487604f4832d90d2010c7c456050.md)

[[TASKS.md](http://TASKS.md)](TASKS%20md%20f4ec487604f4828bb8738128b1a72572.md)