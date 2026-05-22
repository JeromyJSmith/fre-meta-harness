---
name: env-scanner
description: Scan the current environment for installed tools, CLI versions, env vars, and Python packages. Invoke before capability harvesting. Writes evaluation/env-audit.json. Read-only except for writing the audit artifact.
---

# env-scanner

Audit what is actually installed and reachable in the current shell environment.

## Scope

READ: nothing (all checks are shell commands)
WRITE: `evaluation/env-audit.json`
FORBIDDEN: everything else

## Job

Run each check via Bash. Record version or "not_found". Write the artifact.

### CLI Tools to Check

| Tool | Command |
|------|---------|
| bun | `bun --version` |
| uv | `uv --version` |
| pi (Pi Coding Agent) | `pi --version` |
| just | `just --version` |
| codegraph | `~/.bun/bin/codegraph --version` or `bun x codegraph --version` |
| git | `git --version` |
| node | `node --version` |
| python3 | `python3 --version` |

### Env Vars to Check (present/absent, NOT value)

- `PI_COMS_NET_AUTH_TOKEN` — present or absent
- `ANTHROPIC_API_KEY` — present or absent
- `OPENAI_API_KEY` — present or absent

### Lib Repo Install Status

For each dir in `lib/`:
- Check `package.json` exists → check `node_modules/` or `bun.lockb` exists
- Check `pyproject.toml` exists → check `.venv/` or `uv.lock` exists
- Report: installed / needs_install / no_install_needed

## Output Schema

```json
{
  "schema_version": "1.0.0",
  "executed_at": "<iso>",
  "cli_tools": {
    "bun": {"found": true, "version": "1.3.x"},
    "uv": {"found": true, "version": "0.x.x"},
    "pi": {"found": false, "version": null},
    "just": {"found": false, "version": null},
    "codegraph": {"found": true, "version": "1.0.0"},
    "git": {"found": true, "version": "2.x.x"},
    "node": {"found": true, "version": "22.x.x"},
    "python3": {"found": true, "version": "3.12.x"}
  },
  "env_vars": {
    "PI_COMS_NET_AUTH_TOKEN": "present",
    "ANTHROPIC_API_KEY": "absent",
    "OPENAI_API_KEY": "absent"
  },
  "lib_repos": [
    {
      "name": "<repo-name>",
      "path": "lib/<repo-name>",
      "install_status": "installed|needs_install|no_install_needed",
      "has_package_json": true/false,
      "has_pyproject": true/false
    }
  ]
}
```

## Hard Rules

- Never print env var values — only "present" or "absent"
- Do not install anything — this is a READ-ONLY audit
- If a tool is not found, record `"found": false` — do not abort
