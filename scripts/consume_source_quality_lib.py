from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPILED_DIR = ROOT / "evaluation" / "research" / "compiled"
OUTBOX_DIR = ROOT / "outbox"

SOURCE_INDEX_PATH = COMPILED_DIR / "source-index.json"
FEATURE_MATRIX_PATH = COMPILED_DIR / "feature-matrix.json"
CAPABILITY_HARVEST_PATH = COMPILED_DIR / "capability-harvest.json"
GAP_MAP_PATH = COMPILED_DIR / "gap-placement-map.json"
OPERATIONAL_MATRIX_PATH = COMPILED_DIR / "operational-feature-matrix.json"

EXTRACTION_MAP_PATH = OUTBOX_DIR / "2026-05-22-consume-folder-extraction-map.handoff.md"
EXTENSION_GUIDANCE_PATH = OUTBOX_DIR / "2026-05-22-capability-matrix-extension.handoff.md"
OPERATIONAL_MATRIX_HANDOFF_PATH = OUTBOX_DIR / "2026-05-22-operational-feature-matrix.handoff.md"
INGESTION_MAP_HANDOFF_PATH = OUTBOX_DIR / "2026-05-22-compiled-output-ingestion-map.handoff.md"

CONSUME_INPUTS = [
    {
        "path": "inbox/transcribe.consume/file-system-consume.md",
        "title": "file-system-consume",
        "family": "transcribe.consume",
        "extraction_posture": "extract_structure_only",
        "used_by_packets": ["consume_source_quality", "consume_extraction_map"],
        "notes": [
            "First-party consume packet for filesystem-oriented transcript intake.",
            "Useful for extraction posture and bounded source-quality guidance."
        ],
    },
    {
        "path": "inbox/transcribe.consume/prompt-candidate-consumption.md",
        "title": "prompt-candidate-consumption",
        "family": "transcribe.consume",
        "extraction_posture": "extract_and_label_transcript_claims",
        "used_by_packets": ["consume_source_quality", "evidence_strength"],
        "notes": [
            "Prompt candidate for transcript normalization and feature extraction.",
            "Transcript-derived workflow claims must stay blocked until stronger proof exists."
        ],
    },
    {
        "path": "inbox/prompting-tools.consume/Prompt Tools — Capability Harvesting Matrix 05fd146506d6472da0bd527086d6573e.md",
        "title": "capability-harvesting-matrix",
        "family": "prompting-tools.consume",
        "extraction_posture": "extract_capability_taxonomy",
        "used_by_packets": ["operational_feature_matrix", "capability_matrix_extension"],
        "notes": [
            "First-party consume packet that anchors capability harvesting doctrine.",
            "Used for bounded extension guidance without mutating canonical runtime truth."
        ],
    },
    {
        "path": "inbox/prompting-tools.consume/Prompt Tools — Tool Catalog (Prompt → Tool) 93e64081b83745deb9793ba0266585f8.md",
        "title": "tool-catalog",
        "family": "prompting-tools.consume",
        "extraction_posture": "extract_tool_contract_requirements",
        "used_by_packets": ["consume_source_quality", "compiled_output_ingestion"],
        "notes": [
            "Maps prompt-to-tool packaging requirements into bounded compiled outputs.",
            "Supports the ingestion map and operational compile behavior."
        ],
    },
    {
        "path": "inbox/prompting-tools.consume/Schema Set — Contracts for every artifact 49cc487604f482c7972b819cfcb5317b.md",
        "title": "schema-set",
        "family": "prompting-tools.consume",
        "extraction_posture": "extract_schema_requirements",
        "used_by_packets": ["consume_source_quality", "operational_feature_matrix"],
        "notes": [
            "Schema guidance packet used to keep the new source-quality outputs machine-validated.",
            "Supports the operational matrix schema and report schema."
        ],
    },
    {
        "path": "inbox/prompting-tools.consume/Prompt Tools — Pixeltable DuckDB Artifact Store f1f2f37e23014613b0326f67c634f87f.md",
        "title": "pixeltable-duckdb-artifact-store",
        "family": "prompting-tools.consume",
        "extraction_posture": "extract_future_persistence_boundaries",
        "used_by_packets": ["compiled_output_ingestion", "follow_up_decision_space"],
        "notes": [
            "Used only to preserve the exact blocked persistence dependencies.",
            "Does not activate Pixeltable or DuckDB in this slice."
        ],
    },
    {
        "path": "inbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md",
        "title": "operational-capability-matrix-handoff",
        "family": "handoff",
        "extraction_posture": "extract_operational_rows",
        "used_by_packets": ["operational_feature_matrix", "capability_matrix_extension"],
        "notes": [
            "Prior governed handoff used as bounded design input for the operational matrix.",
            "Remains advisory and does not mutate canonical compiled research truth by itself."
        ],
    },
]

OPERATIONAL_MATRIX_ROWS = [
    {
        "capability_id": "consume_packet_inventory",
        "feature_area": "source_intake",
        "parent_surface_type": "distribution_plane",
        "target_contract_surface": "contracts/research-packet-manifest.yaml",
        "runtime_trigger": "consume_refresh",
        "runtime_actor": "research",
        "validation_method": "Validate that every consume folder is mapped to extraction posture, evidence limits, and compiled destinations.",
        "evidence_artifact": "evaluation/research/compiled/source-index.json",
        "blocker_or_dependency": "Requires inbox consume packets to remain inside the parent repo and machine-readable enough for bounded mapping.",
        "parent_lane_classification": "core",
        "consume_inputs": [
            "inbox/transcribe.consume/file-system-consume.md",
            "inbox/transcribe.consume/prompt-candidate-consumption.md",
        ],
        "compiled_outputs": [
            "evaluation/research/compiled/operational-feature-matrix.json",
            "outbox/2026-05-22-consume-folder-extraction-map.handoff.md",
        ],
        "do_not_promote_notes": [
            "Inventory rows describe packet handling only and do not imply runtime activation.",
        ],
    },
    {
        "capability_id": "consume_packet_extraction_mapping",
        "feature_area": "source_intake",
        "parent_surface_type": "distribution_plane",
        "target_contract_surface": "contracts/research-packet-manifest.yaml",
        "runtime_trigger": "consume_refresh",
        "runtime_actor": "research",
        "validation_method": "Validate that extract vs enrich posture is explicit for every consume family and that transcript-heavy inputs stay bounded.",
        "evidence_artifact": "outbox/2026-05-22-consume-folder-extraction-map.handoff.md",
        "blocker_or_dependency": "Requires stable first-party consume packets and durable handoff artifacts.",
        "parent_lane_classification": "core",
        "consume_inputs": [
            item["path"] for item in CONSUME_INPUTS
        ],
        "compiled_outputs": [
            "outbox/2026-05-22-consume-folder-extraction-map.handoff.md",
        ],
        "do_not_promote_notes": [
            "Extraction mapping alone must not promote transcript-derived workflow claims.",
        ],
    },
    {
        "capability_id": "evidence_strength_normalization",
        "feature_area": "source_quality",
        "parent_surface_type": "policy_plane",
        "target_contract_surface": "schemas/evidence-strength.schema.json",
        "runtime_trigger": "source_index_refresh",
        "runtime_actor": "orchestrator-validator",
        "validation_method": "Validate that every source carries an explicit evidence-strength record and transcript-derived workflow claims stay blocked.",
        "evidence_artifact": "evaluation/research/compiled/source-index.json",
        "blocker_or_dependency": "Requires explicit evidence-strength vocabulary and schema validation before compiled outputs refresh.",
        "parent_lane_classification": "core",
        "consume_inputs": [
            "inbox/transcribe.consume/prompt-candidate-consumption.md",
            "inbox/transcribe.consume/file-system-consume.md",
        ],
        "compiled_outputs": [
            "evaluation/research/compiled/source-index.json",
        ],
        "do_not_promote_notes": [
            "Transcript-derived workflow claims stay blocked until frame or terminal proof exists.",
        ],
    },
    {
        "capability_id": "compiled_output_ingestion_mapping",
        "feature_area": "compiled_outputs",
        "parent_surface_type": "distribution_plane",
        "target_contract_surface": "contracts/research-packet-manifest.yaml",
        "runtime_trigger": "compiled_output_refresh",
        "runtime_actor": "research",
        "validation_method": "Validate that every compiled output names its consume inputs, merge rule, and policy gate before refresh.",
        "evidence_artifact": "evaluation/research/harvest-manifest.json",
        "blocker_or_dependency": "Requires stable compiled output paths and idempotent refresh scripts.",
        "parent_lane_classification": "core",
        "consume_inputs": [
            "inbox/prompting-tools.consume/Prompt Tools — Capability Harvesting Matrix 05fd146506d6472da0bd527086d6573e.md",
            "inbox/prompting-tools.consume/Prompt Tools — Tool Catalog (Prompt → Tool) 93e64081b83745deb9793ba0266585f8.md",
        ],
        "compiled_outputs": [
            "evaluation/research/compiled/capability-harvest.json",
            "evaluation/research/compiled/feature-matrix.json",
            "evaluation/research/compiled/gap-placement-map.json",
            "evaluation/research/compiled/source-index.json",
            "outbox/2026-05-22-compiled-output-ingestion-map.handoff.md",
        ],
        "do_not_promote_notes": [
            "Compiled derivatives inherit the strongest truthful limit from their sources.",
        ],
    },
    {
        "capability_id": "operational_feature_matrix_compile",
        "feature_area": "compiled_outputs",
        "parent_surface_type": "observability_plane",
        "target_contract_surface": "schemas/operational-feature-matrix.schema.json",
        "runtime_trigger": "source_quality_compile",
        "runtime_actor": "architect",
        "validation_method": "Validate the operational matrix against its schema and ensure each row names consume inputs, outputs, and non-promotion notes.",
        "evidence_artifact": "evaluation/research/compiled/operational-feature-matrix.json",
        "blocker_or_dependency": "Requires matrix rows to stay parent-owned and bounded to the consume-source-quality slice.",
        "parent_lane_classification": "core",
        "consume_inputs": [
            "inbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md",
            "inbox/prompting-tools.consume/Schema Set — Contracts for every artifact 49cc487604f482c7972b819cfcb5317b.md",
        ],
        "compiled_outputs": [
            "evaluation/research/compiled/operational-feature-matrix.json",
            "outbox/2026-05-22-operational-feature-matrix.handoff.md",
        ],
        "do_not_promote_notes": [
            "Operational rows describe compile behavior only, not active runtime lanes.",
        ],
    },
    {
        "capability_id": "capability_matrix_extension_guidance",
        "feature_area": "handoff_guidance",
        "parent_surface_type": "arbitration_lane",
        "target_contract_surface": "contracts/capability-matrix.yaml",
        "runtime_trigger": "governed_handoff_emit",
        "runtime_actor": "architect",
        "validation_method": "Validate that extension guidance references the canonical matrix rows and does not mutate bounded runtime truth.",
        "evidence_artifact": "outbox/2026-05-22-capability-matrix-extension.handoff.md",
        "blocker_or_dependency": "Requires the canonical capability matrix to remain the source of truth while the handoff stays advisory.",
        "parent_lane_classification": "gated",
        "consume_inputs": [
            "inbox/prompting-tools.consume/Prompt Tools — Capability Harvesting Matrix 05fd146506d6472da0bd527086d6573e.md",
            "inbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md",
        ],
        "compiled_outputs": [
            "outbox/2026-05-22-capability-matrix-extension.handoff.md",
        ],
        "do_not_promote_notes": [
            "Guidance does not rewrite the canonical capability matrix by itself.",
        ],
    },
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n")


def infer_evidence_strength(source: dict) -> dict:
    evidence_type = source["evidence_type"]
    ref = source["ref"]
    notes = list(source.get("notes", []))
    if evidence_type == "transcript_context_summary":
        return {
            "source_ref": ref,
            "evidence_type": evidence_type,
            "strength_class": "transcript_context_limited",
            "transcript_derived": True,
            "workflow_claim_promotion": "blocked",
            "required_artifacts": ["terminal capture", "frame capture"],
            "do_not_promote_reason": "Transcript-derived workflow claims need frame or terminal proof before promotion.",
            "notes": notes or ["Transcript-derived workflow claims remain bounded."],
        }
    if evidence_type == "task_capture":
        return {
            "source_ref": ref,
            "evidence_type": evidence_type,
            "strength_class": "task_capture_limited",
            "transcript_derived": True,
            "workflow_claim_promotion": "blocked",
            "required_artifacts": ["terminal capture", "frame capture"],
            "do_not_promote_reason": "Task captures without terminal or frame evidence stay below promotion strength.",
            "notes": notes or ["Task capture remains bounded without frame evidence."],
        }
    if evidence_type == "task_stub":
        return {
            "source_ref": ref,
            "evidence_type": evidence_type,
            "strength_class": "task_stub_limited",
            "transcript_derived": True,
            "workflow_claim_promotion": "blocked",
            "required_artifacts": ["terminal capture", "frame capture"],
            "do_not_promote_reason": "Task stubs do not preserve the proof needed for workflow promotion.",
            "notes": notes or ["Task stubs remain bounded placeholders."],
        }
    if evidence_type == "local_gap_placeholder":
        return {
            "source_ref": ref,
            "evidence_type": evidence_type,
            "strength_class": "structural_placeholder",
            "transcript_derived": False,
            "workflow_claim_promotion": "blocked",
            "do_not_promote_reason": "Placeholder sources preserve topic awareness only and must not drive workflow promotion.",
            "notes": notes or ["Placeholder source only."],
        }
    if evidence_type == "first_party_consume_packet":
        return {
            "source_ref": ref,
            "evidence_type": evidence_type,
            "strength_class": "first_party_packet",
            "transcript_derived": False,
            "workflow_claim_promotion": "allowed",
            "notes": notes or ["First-party consume packet."],
        }
    if evidence_type == "compiled_derivative":
        return {
            "source_ref": ref,
            "evidence_type": evidence_type,
            "strength_class": "compiled_derivative",
            "transcript_derived": False,
            "workflow_claim_promotion": "allowed",
            "notes": notes or ["Compiled derivative inherits upstream bounded limits."],
        }
    return {
        "source_ref": ref,
        "evidence_type": evidence_type,
        "strength_class": "documentary_support",
        "transcript_derived": False,
        "workflow_claim_promotion": "allowed",
        "notes": notes or ["Documentary support source."],
    }


def build_consume_packet_sources() -> list[dict]:
    sources = []
    for item in CONSUME_INPUTS:
        entry = {
            "kind": "consume_packet",
            "ref": item["path"],
            "evidence_type": "first_party_consume_packet",
            "used_by_packets": item["used_by_packets"],
            "notes": item["notes"],
        }
        entry["evidence_strength"] = infer_evidence_strength(entry)
        sources.append(entry)
    return sources


def refresh_source_index() -> dict:
    payload = load_json(SOURCE_INDEX_PATH)
    sources_by_ref = {source["ref"]: source for source in payload["sources"]}

    for source in sources_by_ref.values():
        source["evidence_strength"] = infer_evidence_strength(source)

    for source in build_consume_packet_sources():
        sources_by_ref[source["ref"]] = source

    payload["sources"] = sorted(sources_by_ref.values(), key=lambda item: item["ref"])
    return payload


def refresh_capability_harvest() -> dict:
    payload = load_json(CAPABILITY_HARVEST_PATH)
    note = (
        "Consume-source-quality refresh added bounded evidence-strength normalization and "
        "an operational feature matrix without changing active runtime-lane truth."
    )
    compiler_notes = payload.get("compiler_notes", [])
    if note not in compiler_notes:
        compiler_notes.append(note)
    payload["compiler_notes"] = compiler_notes
    return payload


def refresh_feature_matrix() -> dict:
    return load_json(FEATURE_MATRIX_PATH)


def refresh_gap_map() -> dict:
    return load_json(GAP_MAP_PATH)


def build_operational_feature_matrix() -> dict:
    return {
        "schema_version": "1.0.0",
        "packet_type": "operational_feature_matrix",
        "status": "refreshed",
        "rows": OPERATIONAL_MATRIX_ROWS,
    }


def extraction_map_rows() -> list[dict]:
    return [
        {
            "path": item["path"],
            "family": item["family"],
            "title": item["title"],
            "extraction_posture": item["extraction_posture"],
            "workflow_claim_rule": (
                "blocked pending stronger proof"
                if "transcribe.consume" in item["family"]
                else "allowed as bounded structural input"
            ),
            "compiled_targets": [
                "evaluation/research/compiled/source-index.json",
                "evaluation/research/compiled/operational-feature-matrix.json",
            ],
        }
        for item in CONSUME_INPUTS
    ]


def ingestion_map_rows() -> list[dict]:
    return [
        {
            "compiled_output": "evaluation/research/compiled/capability-harvest.json",
            "source_inputs": [
                "inbox/prompting-tools.consume/Prompt Tools — Capability Harvesting Matrix 05fd146506d6472da0bd527086d6573e.md",
                "inbox/prompting-tools.consume/Prompt Tools — Tool Catalog (Prompt → Tool) 93e64081b83745deb9793ba0266585f8.md",
            ],
            "ingestion_rule": "Keep canonical capability rows aligned while appending a consume-source-quality compiler note.",
            "policy_gate": "Do not promote new runtime lanes from compile-only artifact strengthening.",
        },
        {
            "compiled_output": "evaluation/research/compiled/feature-matrix.json",
            "source_inputs": [
                "inbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md",
            ],
            "ingestion_rule": "Preserve canonical feature rows and use outbox guidance for any future extension.",
            "policy_gate": "Extension guidance stays advisory until a later governed slice approves canonical edits.",
        },
        {
            "compiled_output": "evaluation/research/compiled/gap-placement-map.json",
            "source_inputs": [
                "evaluation/gap-map-strength-report.json",
            ],
            "ingestion_rule": "Retain consume_source_quality as the bounded strengthening lane while related blocked lanes stay explicit.",
            "policy_gate": "Do not collapse live InfraNodus or persistence blockers into this slice.",
        },
        {
            "compiled_output": "evaluation/research/compiled/source-index.json",
            "source_inputs": [item["path"] for item in CONSUME_INPUTS],
            "ingestion_rule": "Attach evidence-strength records to every source and add first-party consume packets into the governed index.",
            "policy_gate": "Transcript-derived workflow claims remain blocked until frame or terminal proof exists.",
        },
    ]


def write_markdown(path: Path, front_matter: dict, body_lines: list[str], bottom_matter: dict) -> None:
    lines = ["---"]
    for key, value in front_matter.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {json.dumps(value) if isinstance(value, bool) else value}")
    lines.extend(["---", ""])
    lines.extend(body_lines)
    lines.extend(["", "---bottom-matter---"])
    for key, value in bottom_matter.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")
    path.write_text("\n".join(lines) + "\n")


def write_handoffs() -> None:
    extraction_rows = extraction_map_rows()
    ingestion_rows = ingestion_map_rows()

    write_markdown(
        OPERATIONAL_MATRIX_HANDOFF_PATH,
        {
            "artifact_type": ".handoff.md",
            "handoff_id": "HANDOFF-20260522-OPMATRIX",
            "owner": "architect",
            "parent_only": True,
        },
        [
            "# Operational feature matrix handoff",
            "",
            f"- Structured artifact: `evaluation/research/compiled/operational-feature-matrix.json`",
            f"- Row count: `{len(OPERATIONAL_MATRIX_ROWS)}`",
            "- Runtime truth stays bounded to same-host peer mesh and inbox protocol.",
            "- Operational rows describe compile behavior and non-promotion rules only.",
        ],
        {
            "validation_status": "draft",
            "structured_artifact_ref": "evaluation/research/compiled/operational-feature-matrix.json",
            "open_questions": "[]",
        },
    )

    write_markdown(
        EXTENSION_GUIDANCE_PATH,
        {
            "artifact_type": ".handoff.md",
            "handoff_id": "HANDOFF-20260522-CAPEXT",
            "owner": "architect",
            "parent_only": True,
        },
        [
            "# Capability matrix extension guidance",
            "",
            "- Canonical authority remains `contracts/capability-matrix.yaml` plus `evaluation/research/compiled/feature-matrix.json`.",
            "- Advisory extension candidates come from `evaluation/research/compiled/operational-feature-matrix.json`.",
            "- Do not merge operational rows into the canonical matrix until a later governed slice explicitly approves it.",
            "",
            "## Candidate extension surfaces",
            "",
            "- `consume_packet_inventory`",
            "- `consume_packet_extraction_mapping`",
            "- `evidence_strength_normalization`",
            "- `compiled_output_ingestion_mapping`",
            "- `operational_feature_matrix_compile`",
            "- `capability_matrix_extension_guidance`",
        ],
        {
            "validation_status": "draft",
            "structured_artifact_ref": "evaluation/research/compiled/operational-feature-matrix.json",
            "open_questions": "[]",
        },
    )

    write_markdown(
        EXTRACTION_MAP_PATH,
        {
            "artifact_type": ".handoff.md",
            "handoff_id": "HANDOFF-20260522-EXTRACTMAP",
            "owner": "research",
            "parent_only": True,
        },
        [
            "# Consume-folder extraction map",
            "",
            "| Source path | Family | Extraction posture | Workflow claim rule |",
            "| --- | --- | --- | --- |",
            *[
                f"| `{row['path']}` | `{row['family']}` | `{row['extraction_posture']}` | {row['workflow_claim_rule']} |"
                for row in extraction_rows
            ],
            "",
            "Transcript-derived workflow claims remain blocked until frame or terminal proof exists.",
        ],
        {
            "validation_status": "draft",
            "structured_artifact_ref": "evaluation/research/compiled/source-index.json",
            "open_questions": "[]",
        },
    )

    write_markdown(
        INGESTION_MAP_HANDOFF_PATH,
        {
            "artifact_type": ".handoff.md",
            "handoff_id": "HANDOFF-20260522-INGESTMAP",
            "owner": "research",
            "parent_only": True,
        },
        [
            "# Compiled-output ingestion map",
            "",
            "| Compiled output | Ingestion rule | Policy gate |",
            "| --- | --- | --- |",
            *[
                f"| `{row['compiled_output']}` | {row['ingestion_rule']} | {row['policy_gate']} |"
                for row in ingestion_rows
            ],
        ],
        {
            "validation_status": "draft",
            "structured_artifact_ref": "evaluation/research/harvest-manifest.json",
            "open_questions": "[]",
        },
    )


def refresh_all() -> dict:
    OUTBOX_DIR.mkdir(exist_ok=True)
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)

    source_index = refresh_source_index()
    capability_harvest = refresh_capability_harvest()
    feature_matrix = refresh_feature_matrix()
    gap_map = refresh_gap_map()
    operational_matrix = build_operational_feature_matrix()

    write_json(SOURCE_INDEX_PATH, source_index)
    write_json(CAPABILITY_HARVEST_PATH, capability_harvest)
    write_json(FEATURE_MATRIX_PATH, feature_matrix)
    write_json(GAP_MAP_PATH, gap_map)
    write_json(OPERATIONAL_MATRIX_PATH, operational_matrix)
    write_handoffs()

    return {
        "source_index": str(SOURCE_INDEX_PATH.relative_to(ROOT)),
        "capability_harvest": str(CAPABILITY_HARVEST_PATH.relative_to(ROOT)),
        "feature_matrix": str(FEATURE_MATRIX_PATH.relative_to(ROOT)),
        "gap_map": str(GAP_MAP_PATH.relative_to(ROOT)),
        "operational_matrix": str(OPERATIONAL_MATRIX_PATH.relative_to(ROOT)),
        "handoffs": [
            str(OPERATIONAL_MATRIX_HANDOFF_PATH.relative_to(ROOT)),
            str(EXTENSION_GUIDANCE_PATH.relative_to(ROOT)),
            str(EXTRACTION_MAP_PATH.relative_to(ROOT)),
            str(INGESTION_MAP_HANDOFF_PATH.relative_to(ROOT)),
        ],
    }
