from __future__ import annotations

import json
import math
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evaluation"
TOOL_HEALTH_DIR = EVAL_DIR / "tool-health"

STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "that",
    "this",
    "from",
    "into",
    "over",
    "only",
    "when",
    "will",
    "must",
    "does",
    "like",
    "than",
    "they",
    "them",
    "their",
    "there",
    "were",
    "have",
    "has",
    "had",
    "not",
    "but",
    "are",
    "was",
    "its",
    "can",
    "use",
    "using",
    "used",
    "each",
    "every",
    "keep",
    "kept",
    "runs",
    "run",
    "real",
    "local",
    "parent",
    "wrapper",
    "portable",
    "meta",
    "layer",
    "layers",
    "current",
    "next",
    "today",
    "root",
    "file",
    "files",
    "path",
    "paths",
    "json",
    "yaml",
    "md",
}

LAYER_SOURCES = {
    "prompt_contracts": {
        "label": "prompt_contracts",
        "sources": [
            "agent-heavy-run-prompt.schema.json",
            "architect-review-handoff-prompt.schema.json",
            "contracts/three-agent-topology.yaml",
        ],
    },
    "inbox_doctrine": {
        "label": "inbox_doctrine",
        "sources": [
            "inbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md",
            "inbox/2026-05-21-pipeline-ideas-and-implementation.handoff.md",
            "inbox/consuming-layer.plan.md",
        ],
    },
    "subsystem_harness": {
        "label": "subsystem_harness",
        "sources": [
            "contracts/subsystem-harness-topology.yaml",
            "contracts/subsystem-registry.yaml",
            "source/subsystems/registry.json",
            "source/subsystems/intake-etl.md",
            "source/subsystems/research-harvest.md",
            "source/subsystems/semantic-cartography.md",
            "source/subsystems/wrapper-synthesizer.md",
        ],
    },
    "compiled_research": {
        "label": "compiled_research",
        "sources": [
            "evaluation/research/compiled/capability-harvest.json",
            "evaluation/research/compiled/feature-matrix.json",
            "evaluation/research/compiled/gap-placement-map.json",
            "evaluation/research/compiled/source-index.json",
        ],
    },
    "tool_catalog_inputs": {
        "label": "tool_catalog_inputs",
        "sources": [
            "inbox/prompting-tools.consume/Prompt Tools — Tool Catalog (Prompt → Tool) 93e64081b83745deb9793ba0266585f8.md",
            "inbox/prompting-tools.consume/Prompt Tools — Capability Harvesting Matrix 05fd146506d6472da0bd527086d6573e.md",
            "inbox/prompting-tools.consume/Prompt Tools — Observability + Evaluation (Measure 43aec88ea68041cc8bfcf8e8b4b04fc8.md",
            "inbox/transcribe.consume/file-system-consume.md",
            "inbox/transcribe.consume/prompt-candidate-consumption.md",
        ],
    },
    "tool_health": {
        "label": "tool_health",
        "sources": [
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/local-runners.json",
            "evaluation/tool-health/peer-mesh-local.json",
        ],
    },
}

NAMED_IMPROVEMENT_LAYERS = [
    "prompt_contracts",
    "inbox_doctrine",
    "subsystem_harness",
    "compiled_research",
    "tool_catalog_inputs",
]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text()


def normalize_token(token: str) -> str:
    token = token.lower().strip("_-")
    token = token.replace("agent-eval", "agent_eval")
    token = token.replace("meta-harness", "meta_harness")
    token = token.replace("tool-health", "tool_health")
    token = token.replace("goal-md", "goal_md")
    token = token.replace("cli-first", "cli_first")
    token = token.replace("openai_api_key", "provider_key")
    return token


def tokenize(text: str) -> list[str]:
    raw_tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", text)
    tokens = [normalize_token(token) for token in raw_tokens]
    return [token for token in tokens if token not in STOPWORDS]


def load_layer_text(relative_paths: list[str]) -> str:
    sections = []
    for rel in relative_paths:
        path = ROOT / rel
        sections.append(f"FILE: {rel}\n")
        sections.append(read_text(path))
        sections.append("\n")
    return "\n".join(sections)


def top_terms(counter: Counter[str], limit: int = 8) -> list[str]:
    return [term for term, _ in counter.most_common(limit)]


def jaccard(left: set[str], right: set[str]) -> float:
    union = left | right
    if not union:
        return 0.0
    return len(left & right) / len(union)


def build_corpus(layer_texts: dict[str, str]) -> str:
    blocks = []
    for layer_id, text in layer_texts.items():
        blocks.append(f"## LAYER: {layer_id}\n{text.strip()}\n")
    return "\n".join(blocks).strip() + "\n"


def main() -> int:
    layer_texts = {
        layer_id: load_layer_text(config["sources"]) for layer_id, config in LAYER_SOURCES.items()
    }
    layer_tokens = {layer_id: tokenize(text) for layer_id, text in layer_texts.items()}
    layer_counters = {layer_id: Counter(tokens) for layer_id, tokens in layer_tokens.items()}
    layer_term_sets = {layer_id: set(top_terms(counter, 12)) for layer_id, counter in layer_counters.items()}

    corpus = build_corpus(layer_texts)
    (EVAL_DIR / "infranodus-parent-corpus.txt").write_text(corpus)

    all_terms = Counter()
    for tokens in layer_tokens.values():
        all_terms.update(tokens)

    gateway_terms = [
        term
        for term, count in all_terms.most_common()
        if count >= 3 and term not in {"portable_parent_wrapper", "provider_key"}
    ]
    main_concepts = [term for term, _ in all_terms.most_common(12)]

    pair_rows = []
    named_pairs = []
    layer_ids = list(LAYER_SOURCES.keys())
    for index, left in enumerate(layer_ids):
        for right in layer_ids[index + 1 :]:
            overlap = round(jaccard(layer_term_sets[left], layer_term_sets[right]), 3)
            shared_terms = sorted(layer_term_sets[left] & layer_term_sets[right])[:6]
            row = {
                "from_layer": left,
                "to_layer": right,
                "overlap": overlap,
                "shared_terms": shared_terms,
            }
            pair_rows.append(row)
            if left in NAMED_IMPROVEMENT_LAYERS and right in NAMED_IMPROVEMENT_LAYERS:
                named_pairs.append(row)

    content_gaps = [
        f"{row['from_layer']} -> {row['to_layer']}"
        for row in sorted(named_pairs, key=lambda item: (item["overlap"], item["from_layer"], item["to_layer"]))[:3]
    ]

    adjacent_candidates = []
    for layer_id in layer_ids:
        if layer_id in NAMED_IMPROVEMENT_LAYERS:
            continue
        overlaps = [
            row["overlap"]
            for row in pair_rows
            if layer_id in {row["from_layer"], row["to_layer"]}
            and (row["from_layer"] in NAMED_IMPROVEMENT_LAYERS or row["to_layer"] in NAMED_IMPROVEMENT_LAYERS)
        ]
        mean_overlap = round(sum(overlaps) / len(overlaps), 3) if overlaps else 0.0
        adjacent_candidates.append((mean_overlap, layer_id))
    adjacent_candidates.sort(reverse=True)
    missing_adjacent_layer = adjacent_candidates[0][1] if adjacent_candidates else None

    bridges = []
    for row in sorted(named_pairs, key=lambda item: (item["overlap"], item["from_layer"], item["to_layer"]))[:3]:
        bridge_terms = row["shared_terms"] or gateway_terms[:3]
        bridges.append(
            {
                "bridge_id": f"{row['from_layer']}-to-{row['to_layer']}",
                "from_layer": row["from_layer"],
                "to_layer": row["to_layer"],
                "through_layer": missing_adjacent_layer,
                "bridge_terms": bridge_terms[:3],
                "reason": "Low-overlap layers need a shared operational vocabulary to stay comparable.",
                "evidence": [
                    "evaluation/tool-health/status.json",
                    "evaluation/tool-health/local-runners.json",
                    "contracts/parent-capability-metrics.yaml",
                ],
            }
        )

    research_topics = []
    for index, row in enumerate(sorted(named_pairs, key=lambda item: (item["overlap"], item["from_layer"], item["to_layer"]))[:4], start=1):
        terms = row["shared_terms"] or gateway_terms[:4]
        research_topics.append(
            {
                "topic_id": f"topic-{index}",
                "title": f"Bridge {row['from_layer']} and {row['to_layer']} through observable local evidence",
                "priority": index,
                "driven_by_gaps": [f"{row['from_layer']} -> {row['to_layer']}"],
                "bridge_terms": terms[:4],
                "questions": [
                    f"Which bounded commands connect {row['from_layer']} outputs to {row['to_layer']} decisions?",
                    f"Which artifact should become the canonical bridge between {row['from_layer']} and {row['to_layer']}?"
                ],
                "recommended_artifacts": [
                    "contracts/parent-capability-metrics.yaml",
                    "evaluation/tool-health/status.json",
                    "evaluation/infranodus-gap-analysis.json",
                ],
            }
        )

    live_probe = {
        "probe_id": "PARENT-INFRANODUS-LIVE-PROBE-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "status": "blocked",
        "mode": "live_mcp_runtime",
        "blocker": "Live InfraNodus MCP analysis remains API/OAuth-bound and no local runtime credential or session configuration was present in this run.",
        "bounded_fallback": "scripts/build-parent-infranodus-artifacts.py",
        "evidence": [
            "infranodus-phase-tool-map.json",
            "evaluation/tool-health/infranodus-package.log",
            "evaluation/infranodus-gap-analysis.json",
        ],
    }
    (TOOL_HEALTH_DIR / "infranodus-live-probe.json").write_text(json.dumps(live_probe, indent=2) + "\n")

    gap_analysis = {
        "analysis_id": "PARENT-META-INFRANODUS-GAP-0002",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "method": {
            "mode": "bounded_local_cli_substitute",
            "summary": "Used the governed parent corpus, layer token overlap, and gateway terms as the strongest honest local substitute while live MCP analysis stayed blocked.",
            "limitation": live_probe["blocker"],
        },
        "analyzed_layers": [
            {
                "id": layer_id,
                "label": config["label"],
                "source_files": config["sources"],
                "top_terms": top_terms(layer_counters[layer_id]),
            }
            for layer_id, config in LAYER_SOURCES.items()
        ],
        "likely_missing_adjacent_layer": {
            "id": missing_adjacent_layer,
            "label": missing_adjacent_layer,
            "reason": "This layer is present in parent doctrine and evidence, overlaps multiple named layers, and should stay explicit in the improvement map.",
            "evidence": LAYER_SOURCES[missing_adjacent_layer]["sources"] if missing_adjacent_layer else [],
        },
        "topical_clusters": [config["label"] for config in LAYER_SOURCES.values()],
        "content_gaps": content_gaps,
        "resolved_by": [
            "contracts/parent-capability-metrics.yaml",
            "evaluation/tool-health/local-runners.json",
            "evaluation/tool-health/status.json",
            "scripts/build-parent-infranodus-artifacts.py",
        ],
        "limitations": [
            live_probe["blocker"],
            "This bounded substitute reports graph structure honestly but does not claim live InfraNodus MCP output."
        ],
    }
    (EVAL_DIR / "infranodus-gap-analysis.json").write_text(json.dumps(gap_analysis, indent=2) + "\n")

    bridges_payload = {
        "analysis_id": "PARENT-META-INFRANODUS-BRIDGES-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "mode": "bounded_local_cli_substitute",
        "bridges": bridges,
        "limitations": gap_analysis["limitations"],
    }
    (EVAL_DIR / "infranodus-conceptual-bridges.json").write_text(json.dumps(bridges_payload, indent=2) + "\n")

    research_payload = {
        "analysis_id": "PARENT-META-INFRANODUS-RESEARCH-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "mode": "bounded_local_cli_substitute",
        "topics": research_topics,
        "limitations": gap_analysis["limitations"],
    }
    (EVAL_DIR / "infranodus-research-topics.json").write_text(json.dumps(research_payload, indent=2) + "\n")

    cluster_rows = []
    total_terms = sum(all_terms.values()) or 1
    for index, layer_id in enumerate(layer_ids, start=1):
        layer_total = sum(layer_counters[layer_id].values()) or 1
        influence = min(99, int(math.ceil(100 * len(layer_term_sets[layer_id]) / max(1, len(main_concepts)))))
        share = int(round(100 * layer_total / total_terms))
        cluster_rows.append(
            f"{index}. {layer_id}: {' '.join(top_terms(layer_counters[layer_id], 6))} ({index} | {share}% | {influence}%)"
        )

    top_relations = [
        f"{index}) {row['from_layer']} <-> {row['to_layer']}"
        for index, row in enumerate(sorted(pair_rows, key=lambda item: (-item["overlap"], item["from_layer"], item["to_layer"]))[:10], start=1)
    ]
    influential = []
    for term in gateway_terms[:8]:
        degree = sum(1 for terms in layer_term_sets.values() if term in terms)
        influential.append(
            {
                "node": term,
                "bc": round(degree / max(1, len(layer_ids)), 3),
                "degree": degree,
            }
        )

    live_summary = {
        "generated_at": date.today().isoformat(),
        "source": "bounded_local_cli_substitute",
        "scope": "portable_parent_wrapper",
        "statistics": {
            "clusterCount": len(layer_ids),
            "nodeCount": len(set(main_concepts + gateway_terms)),
            "edgeCount": len(pair_rows),
            "diversity_score": "bounded_local",
            "modularity_score": "approximate",
        },
        "contentGaps": [f"Gap {index}: {gap}" for index, gap in enumerate(content_gaps, start=1)],
        "mainTopicalClusters": cluster_rows,
        "mainConcepts": main_concepts[:12],
        "conceptualGateways": gateway_terms[:8],
        "topRelations": top_relations,
        "topInfluentialNodes": influential,
        "limitations": gap_analysis["limitations"],
    }
    (EVAL_DIR / "infranodus-live-summary.json").write_text(json.dumps(live_summary, indent=2) + "\n")

    print(
        json.dumps(
            {
                "status": "ok",
                "artifacts": [
                    "evaluation/infranodus-parent-corpus.txt",
                    "evaluation/infranodus-gap-analysis.json",
                    "evaluation/infranodus-conceptual-bridges.json",
                    "evaluation/infranodus-research-topics.json",
                    "evaluation/infranodus-live-summary.json",
                    "evaluation/tool-health/infranodus-live-probe.json",
                ],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
