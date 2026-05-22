---
name: lib-cloner
description: Clone missing capability repos from github.com/disler into lib/. Invoke when capability-matrix.yaml lists repos not present in lib/. Reads the matrix, clones each missing repo, runs the appropriate install (bun install or uv sync), writes evaluation/lib-clone-status.json. Never touches anything outside lib/ and evaluation/.
---

# lib-cloner

Clone missing disler repos into `lib/` and install them.

## Scope

READ: `contracts/capability-matrix.yaml` (for upstream_repo URLs and install method)
WRITE: `lib/<repo-name>/` (cloned repos), `evaluation/lib-clone-status.json`
FORBIDDEN: everything else — no contracts/, no stages/, no .claude/

## Job

1. Read `contracts/capability-matrix.yaml` — extract all `upstream_repo` URLs
2. For each URL, derive the repo name (last path segment)
3. Check if `lib/<repo-name>/` exists
4. If missing: `git clone <url> lib/<repo-name>`
5. Determine install method:
   - Has `package.json` → `bun install`
   - Has `pyproject.toml` → `uv sync`
   - Neither → no install needed
6. Write `evaluation/lib-clone-status.json`

## Output Schema

```json
{
  "schema_version": "1.0.0",
  "executed_at": "<iso>",
  "capabilities": [
    {
      "capability_id": "<id>",
      "upstream_repo": "<url>",
      "lib_path": "lib/<name>",
      "was_present": true/false,
      "cloned": true/false,
      "installed": true/false,
      "install_method": "bun_install|uv_sync|none",
      "error": null
    }
  ],
  "summary": {
    "total": 10,
    "already_present": 5,
    "cloned": 5,
    "install_failures": 0
  }
}
```

## Hard Rules

- `bun` ONLY for JS/TS installs — never npm or pnpm
- `uv sync` ONLY for Python installs — never pip
- Do NOT clone into any path other than `lib/`
- Do NOT edit any file outside `lib/` and `evaluation/`
- If a clone fails, record the error and continue — do not abort
