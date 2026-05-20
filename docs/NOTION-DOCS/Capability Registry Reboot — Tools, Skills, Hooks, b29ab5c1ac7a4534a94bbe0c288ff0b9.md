# Capability Registry Reboot — Tools, Skills, Hooks, and InfraNodus

<aside>
🔁

**Status**: Focused reboot required — keep FRE, add the missing capability substrate.

</aside>

## Purpose

This handoff saves the current diagnosis and next-agent prompt for the FRE-AGENTIC Engineering project. It is intended for a fresh-context agent that needs to continue the work without re-deriving the whole conversation.

## Verdict

The FRE / Portable Harness organization is **structurally strong but incomplete**.

It does **not** need a total rebuild. It needs a targeted reboot around a missing layer:

> **Tools → Tool abilities → Skills / instructions → Single-file agents → Agents → Hooks → Runs → Graph memory**
> 

## What is already strong

- FRE has a canonical loop: onboarding → brainstorm → research → spec → tasks → build → test → evaluate → promote/repair.
- Portable Harness Package has an export root, folder map, sendable checklist, and definition of done.
- Schema Set already establishes that artifacts need schemas, examples, validators, and provenance.
- Artifact Registry already establishes that produced artifacts should be typed, owned, versioned, validated, and tracked.
- Spec Compiler already establishes markdown-first enforcement and missing-artifact checks.

## What is missing

- A formal `tools/` folder in the portable package.
- A capability manifest that says what tools the harness has access to.
- A tool ability registry that decomposes a tool into specific callable operations.
- A skill / instruction registry that explains how agents should use tools.
- A single-file-agent schema treating executable agents as governed tool-like artifacts.
- A hook manifest connecting events to required tools, skills, outputs, and validation gates.
- InfraNodus as an always-on graph intelligence layer, not merely an optional attached skill.
- A capability-harvest process for turning acquired repositories, archives, and skill libraries into governed harness capabilities.

## Core ontology

```
Capability
  = reusable governed ability the harness can invoke or assign.

Tool
  = executable or callable capability provider.

Tool Ability
  = named operation exposed by a tool.

Skill / Instruction
  = reusable instruction package that teaches an agent how and when to use tools.

Single-file Agent
  = tool-like executable agent artifact with description, inputs, outputs, skills, tools, hooks, and validation contract.

Agent
  = role with a description, scope, accessible skills, accessible tools, and lane ownership.

Hook
  = event-triggered linkage that invokes or requires a tool/skill/agent action.

Manifest
  = machine-readable index of tools, skills, abilities, hooks, and access relationships.

Capability Harvest
  = process for analyzing acquired repositories/libraries/skills and converting them into governed harness capabilities.
```

## Required package additions

```
tools/
  README.md
  manifest.yaml
  infranodus/
    README.md
    tool.yaml
    abilities/
      generate_knowledge_graph.yaml
      create_knowledge_graph.yaml
      generate_topical_clusters.yaml
      generate_content_gaps.yaml
      generate_research_questions.yaml
      generate_research_ideas.yaml
      generate_contextual_hint.yaml
      analyze_existing_graph_by_name.yaml
      analyze_text.yaml
      develop_latent_topics.yaml
      develop_conceptual_bridges.yaml
      develop_text_tool.yaml
      optimize_text_structure.yaml
      retrieve_from_knowledge_base.yaml
      list_graphs.yaml
      search.yaml
      fetch.yaml
      memory_add_relations.yaml
      memory_get_relations.yaml
      difference_between_texts.yaml
      overlap_between_texts.yaml
      merged_graph_from_texts.yaml
      analyze_google_search_results.yaml
      analyze_related_search_queries.yaml
      search_queries_vs_search_results.yaml
      generate_seo_report.yaml

skills/
  README.md
  manifest.yaml
  infranodus-cli/
    skill.yaml
  actionize/
    skill.yaml
  cognitive-variability/
    skill.yaml
  ontology-creator/
    skill.yaml
  llm-wiki/
    skill.yaml
  seo-analysis/
    skill.yaml
  shifting-perspective/
    skill.yaml

capabilities/
  README.md
  capability-matrix.yaml
  capability-harvest.schema.yaml
  capability-harvest.example.yaml

hooks/
  README.md
  hook-manifest.yaml
  infranodus-required-hooks.yaml
```

## Required schemas

```
schemas/
  tool.schema.json
  tool-ability.schema.json
  skill.schema.json
  agent.schema.json
  single-file-agent.schema.json
  hook.schema.json
  capability.schema.json
  capability-manifest.schema.json
  capability-matrix.schema.json
  capability-harvest.schema.json
  infranodus-tool.schema.json
```

Each schema must include:

- `schemaVersion`
- `artifactId`
- `name`
- `description`
- `purpose`
- `inputs`
- `outputs`
- `whenToUse`
- `whenNotToUse`
- `requiredContext`
- `dependencies`
- `sideEffects`
- `failureModes`
- `validation`
- `examples`
- `provenance`
- `docstrings`
- `comments`

## InfraNodus always-on requirement

InfraNodus is a core graph intelligence layer. Every meaningful harness action must either:

1. create/update a graph relation,
2. retrieve from a graph,
3. compare against a graph, or
4. explain why graph analysis was skipped.

This becomes the **InfraNodus graph gate**.

## InfraNodus stage mapping

```
Onboarding:
  - generate_contextual_hint
  - generate_knowledge_graph

Brainstorm:
  - generate_content_gaps
  - generate_research_questions
  - develop_text_tool
  - Cognitive Variability / Shifting Perspective skills

Research:
  - create_knowledge_graph
  - retrieve_from_knowledge_base
  - merged_graph_from_texts
  - generate_topical_clusters

Spec:
  - Ontology Creator skill
  - generate_knowledge_graph
  - develop_conceptual_bridges

Tasks:
  - generate_content_gaps
  - generate_research_questions
  - Actionize skill

Build:
  - retrieve_from_knowledge_base
  - memory_get_relations

Test:
  - difference_between_texts
  - overlap_between_texts
  - optimize_text_structure

Evaluate:
  - analyze_text
  - generate_knowledge_graph
  - graph diversity / focus / topical gap scoring

Promote / Repair:
  - memory_add_relations
  - create_knowledge_graph
  - develop_latent_topics
  - generate_research_ideas
```

## Capability harvest process

1. **Intake**
    - Identify repository/library/archive.
    - Record source and provenance.
    - Extract README, `SKILL.md`, tool docs, and examples.
2. **Parse**
    - Identify tools.
    - Identify abilities.
    - Identify skills/instructions.
    - Identify inputs/outputs.
    - Identify dependencies.
    - Identify examples.
3. **Classify**
    - Map into FRE stages.
    - Map into agent lanes.
    - Map into hooks.
    - Map into validation gates.
4. **Normalize**
    - Produce `tool.yaml`.
    - Produce ability YAML files.
    - Produce `skill.yaml`.
    - Produce capability matrix rows.
5. **Validate**
    - Schema validation.
    - Example exists.
    - At least one usage scenario.
    - At least one failure mode.
    - At least one hook or agent access path.
6. **Promote**
    - Add to manifest.
    - Add to artifact registry.
    - Add to compiler checks.
    - Add to golden path if required.

## Capability matrix columns

```
capability_id
name
type
provider
source_path
description
purpose
fre_stages
agent_lanes
skills_required
tools_required
hooks
inputs
outputs
schemas
examples
validators
failure_modes
side_effects
provenance
promotion_status
```

## First capability-harvest test case

Use the uploaded InfraNodus material as the first harvested capability package:

- `README.md`
- `SKILL.md`
- `tool-examples.md`
- `infranodus-tools.md`
- `infranodus-mcp-deploy-claude-code.txt`

The archive describes:

- InfraNodus CLI skill
- InfraNodus MCP tools
- text network analysis
- knowledge graphs
- content gap detection
- SEO / GEO optimization
- structured memory
- text comparison
- research questions
- latent topic development
- GraphRAG retrieval
- Google/search-intent analysis

Also account for the broader skill library:

- Actionize
- Cognitive Variability
- Critical Perspective
- Writing Assistant
- Ontology Creator
- SEO Analysis
- YouTube Viral Optimizer
- Shopping Assistant
- Rhetorical Analyst
- Shifting Perspective
- Perspective Reversal
- Embodied Navigation
- Vipassana for LLMs
- LLM Wiki
- InfraNodus CLI / Tool Use

## Definition of done

The reboot is complete when:

1. The Portable Harness Package has a visible `tools/` registry.
2. InfraNodus is represented as a governed always-on tool.
3. Every InfraNodus ability has a spec file.
4. Each ability spec explains what the tool is, what it is used for, when it should run, inputs, outputs, failure modes, examples, and schema reference.
5. Skills are represented as instruction artifacts, not vague prose.
6. Single-file agents are represented as tool-like executable artifacts.
7. Agent descriptions can declare accessible skills, accessible tools, accessible resources, and hooks.
8. Hooks can declare trigger event, required tool/skill, output artifact, and validation gate.
9. Capability harvest can ingest a new repo/archive and produce manifest entries, schema-bound capability records, matrix rows, examples, and validation checks.
10. The spec compiler can report missing tools, missing skill specs, missing ability docs, missing examples, missing validators, and missing InfraNodus stage coverage.

## Website / living docs direction

This project should be prepared as a public, living documentation website.

Documentation implications:

- Write pages as public-facing docs, not only private notes.
- Treat the Portable Harness Package as the source tree.
- Treat schemas, manifests, examples, and compiler outputs as publishable reference docs.
- Add contributor-facing explanations for:
    - how to understand the harness,
    - how to add a tool,
    - how to add a skill,
    - how to add an agent,
    - how to run capability harvest,
    - how to validate a contribution,
    - how InfraNodus participates in every stage.

## Next-agent prompt

```
You are the next FRE Harness Reboot Agent working in Jeromy’s Notion workspace.

Your task is to perform a focused reboot of the FRE / Portable Harness organization by adding the missing Capability + Tool Registry layer.

Do not restart the entire harness. Preserve the existing FRE structure, entrypoints, package root, schema set, artifact registry, and compiler model. Your job is to add the missing layer that makes tools, skills, hooks, single-file agents, and InfraNodus explicit, schema-governed, and exportable.

Start by updating the Portable Harness Package folder map, Schema Set, Artifact Registry, and Spec Compiler so they include tools, capabilities, skills, hooks, single-file agents, and InfraNodus always-on graph gates.

Then use the uploaded InfraNodus skill/docs as the first capability-harvest test case.

Keep the scope tight. Do not redesign FRE. Add the missing capability substrate.
```