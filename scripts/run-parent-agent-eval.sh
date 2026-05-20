#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_DIR="$ROOT/evaluation/agent-eval"
EXPERIMENT_ID="parent-wrapper-codex-docker"
MODE="${1:-dry}"

cd "$PROJECT_DIR"

case "$MODE" in
  dry)
    exec npx --yes @vercel/agent-eval "$EXPERIMENT_ID" --dry
    ;;
  smoke)
    if ! command -v docker >/dev/null 2>&1; then
      echo "blocked: docker is required for the bounded local smoke sandbox." >&2
      exit 3
    fi
    if [[ -z "${OPENAI_API_KEY:-}" ]]; then
      echo "blocked: OPENAI_API_KEY is required for the direct codex smoke experiment; docker is available so no VERCEL_TOKEN is needed." >&2
      exit 2
    fi
    exec npx --yes @vercel/agent-eval "$EXPERIMENT_ID" --smoke
    ;;
  *)
    echo "usage: scripts/run-parent-agent-eval.sh [dry|smoke]" >&2
    exit 64
    ;;
esac
