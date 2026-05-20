# action-log.example.md

## action-log example (human readable)

This is the same content as `action-log.example.jsonl`, but explained for humans.

### Records

1. **prompt** — starts a run with an explicit user prompt.
2. **file_edit** — creates or edits a file; include `path`, `result`, and hashes when available.
3. **decision** — ends the run decision: keep/revert/investigate.

### Notes

- `runId` is a stable 4-digit string (e.g. `0001`).
- `ts` is ISO-8601.
- Never include secrets in `inputs`/`outputs`.