# FRE Schema Evaluation Plan for LATTICE Meta-Harness

<aside>
🧪

**Evaluation status**: FRE is being evaluated as a **candidate proof kernel**, not adopted as doctrine and not treated as a replacement framework.

</aside>

## Core hypothesis under test

```
source → schema → examples → validation → metrics → repair task → promotion decision
```

This loop must prove, amend, or reject whether FRE can serve as the smallest repeatable proof kernel for future LATTICE and non-LATTICE projects.

## Current branch context

- **Date**: 2026-05-16
- **Branch**: `feat/fre-meta-harness-eval`
- **Worktree**: `/Volumes/PixelTable/VW_iTWIN_Bridge/lattice-worktrees/feat-fre-meta-harness-eval`
- **Source packet**: `/Volumes/PixelTable/VW_iTWIN_Bridge/fre-test-eval-improvement 76019c48ec2441c0a42a1ac7a3f9b49b.md`
- **Base commit**: `d02328e` from `origin/main`

## Production safety boundary

<aside>
🚫

**Allowed write scope**: `meta/harness/fre/**` only.

**Bootstrap exception**: `meta/harness/docs/specs/fre-method-evaluation-plan-2026-05-16.md`.

Any change outside `meta/harness/fre/**` requires explicit justification in the session report and adoption memo.

</aside>

### Forbidden write scope

```
pixeltable/**
src/**
public/**
scripts/**
meta/SCHEMA.md
meta/ARCHITECTURE.md
meta/API.md
pixeltable/migrations/**
deployment config
production runtime config
production data
```

## Success criteria

1. The FRE packet is translated into repo-local executable artifacts.
2. The loop runs end to end with deterministic `uv` commands.
3. Valid examples pass.
4. Invalid examples fail for expected reasons.
5. Failures produce repair tasks and promotion decisions.
6. Results map cleanly or explicitly conflict with LATTICE concepts: proof evidence, ratchet decisions, capability promotion, and restart-ready docs.
7. At least two real LATTICE fixtures are evaluated.
8. The final decision memo recommends exactly one of: `ADOPT`, `ADOPT WITH AMENDMENTS`, or `REJECT`.

## Rejection criteria

Reject FRE as a future base framework if any are true:

1. Same inputs do not produce repeatable outputs.
2. Invalid examples pass or fail for accidental reasons.
3. Repair tasks are vague or non-actionable.
4. FRE vocabulary conflicts with existing LATTICE proof language without adding clarity.
5. Real LATTICE fixtures require major schema expansion before the loop is useful.
6. The experiment requires migrations, UI, or runtime integration before proving the contract.
7. The adoption memo cannot state what FRE adds beyond existing Meta-Harness practice.
8. The schema cannot represent existing LATTICE proof, evidence, or promotion concepts without major distortion.

## Required repository shape

```
meta/harness/fre/
  README.md
  CLAUDE.md
  docs/
    goal.md
    sources.md
    source-normalization.md
    evaluation-questions.md
    fre-to-lattice-map.md
    adoption-rubric.md
    gaps.md
    decisions/
    sessions/
  schemas/
    fre-loop.schema.json
    gate-result.schema.json
    repair-task.schema.json
    promotion-decision.schema.json
  examples/
    fre-loop.valid.json
    fre-loop.invalid.missing-promotion.json
    fre-loop.invalid.green-terminology.json
    expected-failures.yaml
    gate-result.valid.json
    repair-task.valid.json
    promotion-decision.valid.json
  tests/
    test_schema_validity.py
    test_examples_validate.py
    test_failure_examples_fail.py
    test_no_green_terminology.py
    test_required_metrics.py
    test_repair_tasks.py
    test_lattice_mapping.py
  harness/
    validate_schema.py
    validate_examples.py
    evaluate.py
    report.py
    propose_repairs.py
  runs/
    README.md
```

## Validation checks

- [ ]  Every schema has at least one valid example.
- [ ]  Every invalid example has an expected failure contract.
- [ ]  Every expected failure contract has an expected failure class and expected field.
- [ ]  Every harness script has a command and expected output.
- [ ]  Every run has an immutable run directory.
- [ ]  Every run has an input manifest.
- [ ]  Every failed gate creates a repair task.
- [ ]  Every promotion decision has evidence.
- [ ]  No artifact outside allowed write scope is modified without a scope exception.
- [ ]  FRE terminology does not overwrite LATTICE terminology unless the mapping status is `clean`.

## First 30-minute setup checklist

- [ ]  Create the main evaluation page.
- [ ]  Create the databases listed below.
- [ ]  Add the repository shape as a checklist.
- [ ]  Add the production safety constraints as a pinned warning.
- [ ]  Add Phase 0 artifacts as tasks.
- [ ]  Add Phase 1 schemas/examples/tests as pending records.
- [ ]  Add expected-failure contracts for green terminology and missing promotion decision.
- [ ]  Add FRE-to-LATTICE mapping rows for `repair_task`, `promotion_decision`, `scorecard`, `validation_pass_criteria`, `source_record`, and `artifact`.
- [ ]  Add adoption rubric rows.
- [ ]  Add a P0 view showing anything that blocks deterministic execution.

## Standard

The standard is not whether FRE is elegant. The standard is whether FRE produces better proof artifacts, better repair tasks, and better promotion decisions than LATTICE already has.

[Evaluation Boundary](Evaluation%20Boundary%20d6911f08552b423390a9ca468c318227.md)

[Production Safety Constraints](Production%20Safety%20Constraints%201840c76e8e1d45be81fc2a57338b3e1b.md)

[Rejection Criteria](Rejection%20Criteria%20ad1b72c2e786425bae2ecc4b03fd3267.md)

[Repository Shape](Repository%20Shape%204d9532b343b343fb853acba15ea0730f.md)

[Ground Rules](Ground%20Rules%204ce70dd509354ec383fad5f9f0f57a31.md)

[Expected Failure Contracts](Expected%20Failure%20Contracts%20e69fd15f602c4ebe88d9a76d64211c72.md)

[Success Criteria](Success%20Criteria%200674bbbd699846aeb005b1b3ea62b56d.md)

[FRE-to-LATTICE Translation Map](FRE-to-LATTICE%20Translation%20Map%2084b5ec31f8624486b8287187f7b4f0ae.md)

[Evaluation Hypothesis](Evaluation%20Hypothesis%20442f9575f22b4766a13cbd81e708a35b.md)

[Phase 0 Artifacts](Phase%200%20Artifacts%2060478fea3cee47f2afcc07acd9b6ef45.md)

[Source Packet Normalization](Source%20Packet%20Normalization%203e85303f1a904c7286fde7b6da94159a.md)

[Phase 1 Executable Loop](Phase%201%20Executable%20Loop%200e2fb263b5df4ba29677c965fbc94e32.md)

[Immediate Next Tasks](Immediate%20Next%20Tasks%2095f44d8966bf424fa6b314f6f16838b5.md)

[Risks and Controls](Risks%20and%20Controls%202076482f2a684403be44ca68377d24c1.md)

[Run Manifests](Run%20Manifests%20d3937ce847844723948403a24728e0ed.md)

[Adoption Rubric](Adoption%20Rubric%201b353945166a4dd685cad6bdc98373bc.md)

[FRE Evaluation Artifacts](FRE%20Evaluation%20Artifacts%205d807ea8501d433e8e729060c5815cec.csv)

[Harness Scripts](Harness%20Scripts%2069d24fc68d374d6ea57ea234af8a8763.csv)

[Expected Failures](Expected%20Failures%20f1911808b65a496c8e37741efda7f42f.csv)

[Immutable Runs](Immutable%20Runs%2084b0c6f0a9c94df59d5c8db4fb9b7cac.csv)

[FRE Tests](FRE%20Tests%20b1e979ce33a24a3db798978284953b43.csv)

[FRE Examples](FRE%20Examples%20f03b1ca756ea4d5094b844cedbf397ac.csv)

[FRE Schemas](FRE%20Schemas%20d2955e8824824c7a95b0d6fa1f9aaced.csv)

[FRE-to-LATTICE Mappings](FRE-to-LATTICE%20Mappings%20d6409c74d8834430a96aaef7fdc9f38d.csv)

[Promotion Decisions](Promotion%20Decisions%20e29f522ea59a46f09c54b6254e2c5c3b.csv)

[Scope Exceptions](Scope%20Exceptions%20946418b06cd444449c0d7d08ebbde011.csv)

[Repair Tasks](Repair%20Tasks%2049ffe2fa5a2c476ebb3157f6e19d9881.csv)

[Adoption Rubric Scores](Adoption%20Rubric%20Scores%20ad0cf28063564eadbcde708e89e6c3ed.csv)