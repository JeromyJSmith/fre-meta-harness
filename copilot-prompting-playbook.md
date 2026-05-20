# GitHub Copilot Prompting Playbook

This parent wrapper uses the same governed heavy-run prompting doctrine as the
child Meta-Harness.

Rules:

- start from verified local truth
- keep scope bounded
- use `uv` for Python execution
- require durable proof and validation artifacts
- keep blocked states honest
- map every heavy prompt back to the governed prompt schema

Prompt shape:

1. mission
2. current verified state
3. hard rules
4. bounded tasks
5. validation loop
6. report contract
