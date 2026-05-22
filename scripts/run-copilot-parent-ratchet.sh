#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKSPACE_ROOT="${FRE_META_WORKSPACE_ROOT:-$(cd "$ROOT/.." && pwd)}"
PROMPT_FILE="$ROOT/prompts/parent-wrapper-copilot-ratchet.prompt.md"
SHARE_FILE="$ROOT/runs/copilot-parent-wrapper-ratchet-session.md"

gh copilot \
  -C "$WORKSPACE_ROOT" \
  --add-dir "$ROOT" \
  --allow-all \
  --no-ask-user \
  --share "$SHARE_FILE" \
  -p "$(cat "$PROMPT_FILE")"
