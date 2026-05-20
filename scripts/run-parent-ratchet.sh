#!/usr/bin/env bash
set -euo pipefail

ROOT="/Volumes/PixelTable/VW_iTwin_Bridge/meta"
LOG="$ROOT/runs/iterations.jsonl"
REPORT="$ROOT/evaluation/copilot-ratchet-report.json"

mkdir -p "$ROOT/runs"
touch "$LOG"

before_json="$(mktemp)"
after_json="$(mktemp)"

uv run --isolated --with jsonschema --with pyyaml python "$ROOT/scripts/score-parent-wrapper.py" --json > "$before_json"
bash "$ROOT/scripts/run-copilot-parent-ratchet.sh"
uv run --isolated --with jsonschema --with pyyaml python "$ROOT/tests/validate_parent_wrapper_contract.py" >/dev/null
uv run --isolated --with jsonschema --with pyyaml python "$ROOT/scripts/score-parent-wrapper.py" --json > "$after_json"

if [[ ! -f "$REPORT" ]]; then
  echo "missing $REPORT" >&2
  exit 1
fi

cycles="$(jq -r '.real_non_dry_cycles_executed // 0' "$REPORT")"

if [[ "$cycles" -lt 2 ]]; then
  echo "copilot report did not execute at least 2 real non-dry cycles" >&2
  exit 1
fi

jq -cn \
  --argjson before "$(cat "$before_json")" \
  --argjson after "$(cat "$after_json")" \
  --argjson report "$(cat "$REPORT")" \
  '{
    iteration: (now | floor),
    cycle_kind: "real_non_dry",
    before_score: $before.total_score,
    after_score: $after.total_score,
    before_outcome_score: $before.outcome_score,
    after_outcome_score: $after.outcome_score,
    before_instrument_score: $before.instrument_score,
    after_instrument_score: $after.instrument_score,
    weakest_component_before: $before.weakest_component,
    weakest_component_after: $after.weakest_component,
    action: "copilot-parent-ratchet-cycle",
    result: (if $after.total_score >= $before.total_score then "kept" else "reverted" end),
    note: $report.stop_reason,
    kept: ($after.total_score >= $before.total_score),
    copilot_status: $report.status,
    real_non_dry_cycles_executed: $report.real_non_dry_cycles_executed
  }' >> "$LOG"

cat "$after_json"
