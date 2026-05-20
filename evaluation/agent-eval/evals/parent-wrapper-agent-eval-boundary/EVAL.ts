import { existsSync, readFileSync } from 'fs';
import { test, expect } from 'vitest';

test('writes the parent agent-eval summary file', () => {
  expect(existsSync('out/agent-eval-summary.json')).toBe(true);
});

test('summary preserves the truthful parent boundary', () => {
  const summary = JSON.parse(readFileSync('out/agent-eval-summary.json', 'utf-8'));

  expect(summary).toMatchObject({
    scope: 'portable_parent_wrapper',
    current_evidence: 'dry',
    dry_command: 'scripts/run-parent-agent-eval.sh dry',
    next_smoke_command: 'scripts/run-parent-agent-eval.sh smoke',
    smoke_requires: ['OPENAI_API_KEY'],
    sandbox: 'docker',
    docs_only_is_evidence: false,
    tool_health_is_improvement_proof: false,
    live_ready: false,
  });
});

test('agent read the parent doctrine files first', () => {
  const results = JSON.parse(readFileSync('__agent_eval__/results.json', 'utf-8'));
  const filesRead = new Set(results.o11y?.filesRead ?? []);

  expect(filesRead.has('README.md')).toBe(true);
  expect(filesRead.has('GOAL.md')).toBe(true);
  expect(filesRead.has('program.md')).toBe(true);
  expect(filesRead.has('library.yaml')).toBe(true);
  expect(filesRead.has('agentics-library.md')).toBe(true);
});
