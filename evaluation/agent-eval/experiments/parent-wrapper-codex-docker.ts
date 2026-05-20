import type { ExperimentConfig } from '@vercel/agent-eval';

const config: ExperimentConfig = {
  agent: 'codex',
  runs: 1,
  earlyExit: true,
  timeout: 300,
  evals: ['parent-wrapper-agent-eval-boundary'],
  validation: 'vitest',
  sandbox: 'docker',
  copyFiles: 'all',
};

export default config;
