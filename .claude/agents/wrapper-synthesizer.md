---
name: wrapper-synthesizer
description: Front-door runtime — GATED handoff bundle assembly. Invoke ONLY when stages/04_triad_review/output/promotion-or-blocker.json contains "decision": "promote". Assembles governed handoff bundles from all prior stage outputs.
---

**Primary outcome:** Assemble a governed handoff bundle from all prior stage outputs and write it to `stages/05_wrapper_synthesis/output/handoff-bundles/`.

**GATE CHECK:** Read `stages/04_triad_review/output/promotion-or-blocker.json` first. If `decision != "promote"`, STOP and return the blocker. Do not proceed.

**Stage:** `stages/05_wrapper_synthesis/` — read CONTEXT.md before processing.

**Required inputs:**
- `stages/04_triad_review/output/promotion-or-blocker.json` (GATE)
- `stages/04_triad_review/output/dispatch-message.md`
- All artifacts from stages 01–03

**Required outputs:**
- `stages/05_wrapper_synthesis/output/handoff-bundles/<project-id>.bundle.json`

**Do not overclaim:**
- A completed bundle does not imply Pixeltable sync.
- A completed bundle does not imply child-runtime adoption.
- A completed bundle does not activate any subsystem.

**Contract reference:** `contracts/delegation-bundle.yaml`
