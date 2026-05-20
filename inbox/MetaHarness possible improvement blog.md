Title: Meta-Harness: A Self-Optimizing Harness Around Coding Agents

URL Source: http://shashikantjagtap.net/meta-harness-a-self-optimizing-harness-around-coding-agents/

Markdown Content:
Stanford AI lab just released the [Meta Harness paper](https://arxiv.org/pdf/2603.28052) which covers the meta harness strategy that self-optimise. Most conversations about coding agents focus on the model. People compare model quality, context windows, tool use, and reasoning ability. Those things matter, but after working with coding agents on real repositories, a different pattern becomes hard to ignore. The model is often not the whole story.

Two systems can use very similar models and still behave very differently. One feels sharp, grounded, and reliable. The other feels noisy, brittle, and hard to trust. One gets into a repository, understands the job, follows the rules, runs the right checks, and makes focused edits. The other drifts, misses setup assumptions, changes the wrong files, or keeps repeating the same mistakes. Very often, the difference is not just the model. It is the harness around the model.

That is why we built `metaharness`. It’s an open source [Python](https://github.com/SuperagenticAI/metaharness) library for optimizing coding agent harnesses. It is inspired by the [Meta Harness paper](https://arxiv.org/pdf/2603.28052) and is an unofficial implementation of the core ideas in that work. This post explains what the harness is, why it matters so much, what `metaharness` does, how to use it, what is included in the first public release, and how to think about applying it to real coding agent systems.

## What is the harness around a coding agent?

When people say “agent,” they often collapse many things into one idea. In practice, the agent is not just a model call. It is a whole working environment around the model. That environment usually includes files like:

*   `AGENTS.md`
*   `GEMINI.md`
*   `CLAUDE.md`
*   `bootstrap.sh`
*   `validate.sh`
*   `test.sh`

It also includes any surrounding glue that shapes the agent’s behavior. Repository instructions, setup logic, evaluation rules, retrieval helpers, routing rules, safety checks, acceptance criteria, and the small operational details that decide what the model sees and what it is allowed to do are all part of the harness.

If the harness is weak, the model starts from a bad position. It may not understand the repository. It may not know what success means. It may not have enough validation feedback. It may be missing critical setup context. It may be allowed to edit far more than it should. It may look like a model problem when it is really a harness problem.

## The practical problem

Harness work is usually done in a very manual way. A team notices that the agent keeps making the same mistake. Someone updates the instruction file. Then they tweak the setup script. Then they add one more validation step. Then they adjust the test command. Then they rewrite a prompt fragment. Then someone else makes another change a few days later. Some of those changes help. Some do nothing. Some make the system worse in subtle ways. After a while, the team no longer has a clean answer to a basic question.

**Which harness changes actually improved the system?**

That question is surprisingly hard to answer if you do not keep a disciplined record of candidates, diffs, validation output, and evaluation results. This is the problem `metaharness` tries to solve.

## The central idea behind metaharness

The main idea is simple. Treat the harness itself as the optimization target. Instead of only optimizing a prompt string, optimize the executable environment around the coding agent. That means the optimizer is allowed to improve things like repository instructions, bootstrap scripts, validation scripts, test scripts, and other small harness artifacts that affect agent behavior. Then evaluate those changes with deterministic checks, keep the evidence on disk, and repeat. This is a much more realistic view of how coding agents succeed or fail in actual repositories.

## Why a filesystem first design matters

One of the strongest design choices in `metaharness` is that it is filesystem first. That sounds simple, but it matters a lot. Many optimization systems collapse the world down to a compact textual summary. That can be useful, but coding agent behavior often depends on details that live in real files and real run artifacts. For example, the exact wording of the repository instructions, the exact shell command used for validation, whether a bootstrap script exits early, whether the test runner actually checks the real task, and whether the agent was allowed to edit files outside its intended scope are all easier to reason about when they are preserved as real files and real diffs.

`metaharness` stores the candidate workspace, proposal result, validation result, evaluation result, manifest, and diff on disk. That makes every run inspectable after the fact. This is one of the biggest differences between casual agent tweaking and disciplined harness optimization.

## How metaharness works

At a high level, `metaharness` runs an outer loop over a baseline harness.

1.   Start from a baseline workspace.
2.   Prepare a candidate workspace.
3.   Capture a compact environment bootstrap.
4.   Ask a coding agent backend to improve the harness.
5.   Validate the candidate.
6.   Evaluate the candidate against a deterministic objective.
7.   Store all artifacts on disk.
8.   Keep the best candidate and continue within budget.

That outer loop is the core product.

The provider backend is swappable. The benchmark target is swappable. The harness is swappable.

This is important because the library should not be tied to one exact provider or one exact paper setup. It should be reusable across coding agent environments.

## What gets stored during a run

Every run is designed to leave a useful paper trail. A typical run stores the candidate workspace, a candidate manifest, proposal stdout and stderr, proposal metadata, validation output, evaluation output, workspace diffs, run summaries, and ledgers.

This is not just nice to have. It is what makes it possible to debug a failed optimization run, compare candidates, and understand whether a change really helped.

## Features in the current release

The current release already includes a substantial amount of functionality. At the core of the package, it includes a minimal optimization engine, a filesystem backed run store, a public CLI, a coding tool integration layer, experiment matrix execution, candidate ledgers, and run summaries. It also includes safety and structure features that turned out to matter a lot in practice. One is an environment bootstrap snapshot. Before proposal begins, `metaharness` captures a compact description of the workspace, the detected tools, package files, git state, and environment. This gives the proposer a better starting point and avoids wasting turns on trivial discovery.

Another is write scope enforcement. A project can declare exactly which paths are allowed to change. If a candidate edits files outside that scope, the system can reject it automatically as a scope violation. This matters because a harness optimizer should not quietly win by changing arbitrary files that were never meant to be part of the optimization target.

## Candidate outcomes

Every candidate gets an explicit outcome classification. The current system uses outcomes such as `baseline`, `keep`, `discard`, `crash`, `timeout`, `no-change`, and `scope-violation`. This is useful because not all failures are the same. A provider crash, a timeout, a harmless no-op, and an off-target edit are very different situations. Treating them as different outcomes makes the experiment record much more useful.

## Benchmarks included in the repository

The repository includes built-in examples and benchmark targets. The most important ones are `examples/python_fixture_benchmark`, `examples/python_cli_benchmark`, and `examples/ticket_router`.

The two Python benchmarks are the main release quality examples. They are not just toy prompt demos. They use real shell scripts, deterministic checks, and a real fixture repository layout.

The smaller ticket router example is useful for understanding the loop quickly.

## Provider strategy in this release: Codex

A key product decision in this release is that the project is positioned as **Codex first**. It would be easy to say that many providers are supported equally, but that would not be honest. The strongest benchmark evidence in the repository is on the Codex path. That includes hosted Codex and Codex over local Ollama models. Other integrations exist, but they are not being presented as equally validated. In the current release, Codex is the primary and validated backend. Gemini CLI is experimental. Pi is experimental. OpenCode is experimental. This is a better release shape because it gives users one strong path to trust while still keeping room for future provider work.

## Why Codex is the primary validated path

Codex earned that position because it is the provider path with the clearest and strongest benchmark evidence in this repository. Real documented runs showed that hosted Codex solved both real benchmark targets. Local Codex over Ollama with `gpt-oss:120b` also solved one of the real benchmarks. Local `gpt-oss:20b` was useful for smoke checks but timed out on the current real benchmarks. That gives the project a credible release story. There is one provider path that is clearly working well, is benchmarked, and is ready to recommend.

## What happened with Gemini, Pi, and OpenCode

Those backends are implemented, and the integration work is real. They are not placeholders. But implementation alone is not the same as validation.

When running live smoke tests, each of them exposed a different type of real world integration issue. Gemini CLI launched, but failed because the environment did not have `GEMINI_API_KEY` configured. Pi launched, but failed because no models were configured. It asked for provider API keys or a models configuration file in the Pi user directory. OpenCode launched. One run failed because it tried to write under its own user state directory in a sandboxed environment. A second run outside the sandbox completed successfully, but produced a no-change candidate and hit its own permission behavior.

These results are valuable because they show that the backends exist and can be exercised through `metaharness`. But they also confirm that Codex is the only provider path that should be considered release quality in the current version.

## Installing metaharness

The package is published on PyPI as `superagentic-metaharness`. The installed command is still `metaharness`. If you want the released CLI, install it with `uv`:

```
uv tool install superagentic-metaharness
metaharness --help
```

If you want to work from source, clone the repository and set up the environment with:

```
uv sync
uv run metaharness --help
```

If you also want the docs toolchain, use:

```
uv sync --group dev
```

## Your first useful run

The easiest way to understand the system is to run the fake backend on a real benchmark target. This is a very good newcomer path because it exercises the full optimization loop without requiring provider authentication, model access, or external network calls.

```
uv run metaharness run \
  examples/python_fixture_benchmark \
  --backend fake \
  --budget 1 \
  --run-name first-run
```

Then inspect the results:

```
uv run metaharness inspect \
  examples/python_fixture_benchmark/runs/first-run
```

And export the candidate ledger:

```
uv run metaharness ledger \
  examples/python_fixture_benchmark/runs/first-run \
  --tsv
```

This alone gives a clear view of how the package works.

## Running a real Codex benchmark

Once you are comfortable with the fake backend flow, move to the Codex path. If you want to use hosted Codex:

```
uv run metaharness run \
  examples/python_fixture_benchmark \
  --backend codex \
  --hosted \
  --budget 1 \
  --run-name hosted-codex
```

If you want to use local Codex over Ollama:

```
uv run metaharness smoke codex \
  examples/python_fixture_benchmark \
  --probe-only \
  --oss \
  --local-provider ollama \
  --model gpt-oss:20b
```

Then run the benchmark:

```
uv run metaharness run \
  examples/python_fixture_benchmark \
  --backend codex \
  --oss \
  --local-provider ollama \
  --model gpt-oss:20b \
  --proposal-timeout 240 \
  --budget 1
```

For a stronger local model:

```
uv run metaharness run \
  examples/python_fixture_benchmark \
  --backend codex \
  --oss \
  --local-provider ollama \
  --model gpt-oss:120b \
  --proposal-timeout 240 \
  --budget 1
```

## Inspecting results after a run

After any run, the first thing to do is inspect the run summary.

```
uv run metaharness inspect \
  examples/python_fixture_benchmark/runs/hosted-codex
```

Then use the ledger view:

```
uv run metaharness ledger \
  examples/python_fixture_benchmark/runs/hosted-codex
```

If you want tabular output for analysis:

```
uv run metaharness ledger \
  examples/python_fixture_benchmark/runs/hosted-codex \
  --tsv
```

If you have several runs, summarize them:

```
uv run metaharness summarize \
  examples/python_fixture_benchmark
```

Or compare specific run directories:

```
uv run metaharness compare \
  examples/python_fixture_benchmark/runs/hosted-codex-20260401 \
  examples/python_fixture_benchmark/runs/ollama-120b-20260401
```

## Running experiment matrices

The experiment runner is one of the most useful parts of the package. It lets you run repeated trial matrices and save aggregate outputs as JSON and TSV.

A simple example:

```
uv run metaharness experiment \
  examples/python_fixture_benchmark \
  --backend fake \
  --trials 3
```

You can also use a saved config:

```
uv run metaharness experiment \
  --config examples/experiment_configs/fake-benchmarks.json
```

This is the right way to turn one off local experiments into repeatable benchmark records.

## Why write scope enforcement matters

It is worth pausing on this feature because it is easy to underestimate. Imagine you want to optimize the harness for a coding agent. You intend to improve instruction files, bootstrap scripts, validation scripts, and test scripts. But if the optimizer is allowed to change anything in the repository, it may accidentally win by editing unrelated files. That would muddy the result. You would no longer know whether the harness got better or whether the optimizer just escaped the intended problem.

With `allowed_write_paths`, you can constrain exactly what is in scope. That makes results much easier to trust.

## Why environment bootstrap snapshots matter

Another feature that looks small but matters a lot is the environment bootstrap. Before the proposer starts editing, `metaharness` captures a compact summary of the environment. That summary can include the working directory, top level workspace entries, detected tools, package and build files, git state, and platform and Python details.This gives the proposer a faster start and reduces wasteful early exploration.In coding agent systems, the first few turns are often consumed by basic recon. A compact bootstrap improves that starting point significantly.

## What the current benchmark evidence says

At the moment, the benchmark story is clear.Hosted Codex is the strongest path on the real benchmarks in this repository. Local Codex over Ollama with `gpt-oss:120b` is capable, but slower. Local `gpt-oss:20b` is useful for smoke checks but timed out on the current real benchmarks. The experimental providers are implemented and documented, but they are not yet part of the main validated story. This is a good place to be for an early release. The package has one clear validated provider path and several future paths that can be improved later.

## Who should use metaharness right now

`metaharness` is already useful for a few specific audiences. It is useful for teams building coding agent systems who want to optimize the real environment around the model instead of endlessly tweaking prompts in isolation. It is useful for practitioners who already rely on coding tools in repositories and want to improve the instruction files, setup flow, validation logic, and test flow around those tools. It is also useful for people doing careful evaluation work on coding agent harnesses who want durable experiment records rather than one off intuition.

## What this first release is and is not

This is an alpha release, and it is important to be clear about what that means.

What it is:

*   a real open source package
*   a usable CLI
*   a filesystem first optimization framework
*   a Codex first harness optimization tool with benchmark evidence
*   a strong base for future provider and benchmark work

What it is not:

*   a full reproduction of every result in the Meta Harness paper
*   a claim that all providers are equally validated
*   a finished benchmark platform with every major coding agent integrated

This is exactly the right scope for an early public release.

## Why release now

It is often tempting to wait until everything feels complete. In practice, that can slow down the stage where outside feedback becomes most valuable.The core loop works. The package is published. The docs exist. The benchmark story is credible. The provider story is honestly scoped. That is enough to put the project in front of real users. And for a tool like this, real usage matters more than endless internal polish.

## Where metaharness can go next

The next steps are straightforward.The most important one is probably not more framework expansion. It is stronger evidence around the existing system.That can include more Codex benchmark studies, deeper benchmark targets, careful selective work on one experimental provider at a time, and more project templates and benchmark profiles.But even without those future steps, the current release already delivers something useful and concrete.

## Try it

Project links:

GitHub:

[https://github.com/SuperagenticAI/metaharness](https://github.com/SuperagenticAI/metaharness)

Documentation:

[https://superagenticai.github.io/metaharness/](https://superagenticai.github.io/metaharness/)

PyPI:

[https://pypi.org/project/superagentic-metaharness/](https://pypi.org/project/superagentic-metaharness/)

If you work on coding agents, coding agent infrastructure, or benchmark driven improvement of agent workflows, `metaharness` is meant for exactly that layer of work.

The model matters. But the harness around the model often matters just as much. In real systems, that is usually where a surprising amount of quality lives.
