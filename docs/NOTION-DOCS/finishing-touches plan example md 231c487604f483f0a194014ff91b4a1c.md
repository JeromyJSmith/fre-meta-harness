# finishing-touches.plan.example.md

---

name: Finishing Touches — Portable Harness Package

status: example

owners:

- planning-agent

version: 0.1.0

lastUpdated: 2026-05-15

overview: Example plan file showing required sections and bottom-matter config.

---

# Inputs

- project-name: example-project
- green-definition: export succeeds + required files exist

# Acceptance criteria

- compiler/[compliance.md](http://compliance.md) exists
- compiler/[missing.md](http://missing.md) exists

# Steps

1. Copy template into projects/example-project/
2. Customize nucleus docs
3. Seed backend/data/*.csv
4. Record runs/[0001.md](http://0001.md)

```yaml
# plan-config (bottom matter)
run:
  iteration_budget:
    wall_clock_minutes: 20
    max_turns: 80
  logging:
    run_log_dir: "runs/"
  scoring:
    primary_metric: "goal_pass_rate"
```