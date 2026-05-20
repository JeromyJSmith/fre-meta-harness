#!/usr/bin/env bash
set -euo pipefail

ROOT="/Volumes/PixelTable/VW_iTwin_Bridge/meta"
PROMPT_FILE="$ROOT/prompts/parent-wrapper-copilot-ratchet.prompt.md"
SHARE_FILE="$ROOT/runs/copilot-parent-wrapper-ratchet-session.md"

gh copilot \
  -C /Volumes/PixelTable/VW_iTWIN_Bridge \
  --add-dir /Volumes/PixelTable/VW_iTwin_Bridge/meta \
  --allow-all \
  --no-ask-user \
  --share "$SHARE_FILE" \
  -p "$(cat "$PROMPT_FILE")"
