You are evaluating the standalone `fre-meta-harness` parent wrapper.

Read these local authority files before writing anything:

- `README.md`
- `GOAL.md`
- `program.md`
- `library.yaml`
- `agentics-library.md`

Then create `out/agent-eval-summary.json` with exactly these keys:

- `scope`
- `current_evidence`
- `dry_command`
- `next_smoke_command`
- `smoke_requires`
- `sandbox`
- `docs_only_is_evidence`
- `tool_health_is_improvement_proof`
- `live_ready`

Use the parent-wrapper truth in this fixture.

Rules:

- Do not claim smoke or live success.
- Do not invent credentials.
- Keep `scope` equal to `portable_parent_wrapper`.
- Set `current_evidence` to the strongest honest local evidence in this fixture.
- Set `dry_command` to `scripts/run-parent-agent-eval.sh dry`.
- Set `next_smoke_command` to `scripts/run-parent-agent-eval.sh smoke`.
- Set `smoke_requires` to a JSON array containing only `OPENAI_API_KEY`.
- Set `sandbox` to `docker`.
- Set `docs_only_is_evidence` to `false`.
- Set `tool_health_is_improvement_proof` to `false`.
- Set `live_ready` to `false`.
