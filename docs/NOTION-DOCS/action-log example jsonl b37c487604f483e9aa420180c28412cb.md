# action-log.example.jsonl

```
{"ts":"2026-05-15T17:55:00Z","runId":"0001","actionType":"prompt","inputs":{"text":"Bootstrap new project"},"claudeCodeVersion":"2.x"}
{"ts":"2026-05-15T17:55:05Z","runId":"0001","actionType":"file_edit","inputs":{"path":"projects/example/CLAUDE.md"},"outputs":{"result":"created"},"hashes":{"sha256":"<placeholder>"},"claudeCodeVersion":"2.x"}
{"ts":"2026-05-15T17:55:10Z","runId":"0001","actionType":"decision","outputs":{"decision":"keep","reason":"meets goal_pass_rate"},"claudeCodeVersion":"2.x"}
```