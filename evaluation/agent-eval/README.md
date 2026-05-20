# Parent agent-eval lane

This directory is the parent-scoped `@vercel/agent-eval` project for the
standalone `fre-meta-harness` wrapper.

## Current truthful boundary

- default parent baseline: CLI-first local runner harvest plus dry agent-eval
- strongest honest local evidence today: `dry`
- optional remote-backed escalation: `smoke`
- why smoke is not yet green in this repo: Docker is available locally, but no
  supported provider credential is configured for the direct Codex experiment

## Fixture shape

- experiment: `experiments/parent-wrapper-codex-docker.ts`
- eval: `evals/parent-wrapper-agent-eval-boundary/`
- subject: parent-wrapper evaluation doctrine, not child-repo implementation

## Commands

```bash
scripts/run-parent-agent-eval.sh dry
scripts/run-parent-agent-eval.sh smoke
```

`dry` proves the fixture is discoverable with no API calls.

`smoke` is an exact exception lane, not the normal parent path. It requires
`OPENAI_API_KEY`, because the experiment is pinned to `sandbox: 'docker'`.

## Expected durable artifacts

- `evaluation/tool-health/agent-eval-dry.log`
- `evaluation/tool-health/agent-eval-smoke.log`
- `contracts/agent-eval-parent-lane.yaml`
