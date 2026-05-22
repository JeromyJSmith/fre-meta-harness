from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from consume_source_quality_lib import ROOT, OPERATIONAL_MATRIX_PATH, SOURCE_INDEX_PATH


def load_schema(rel_path: str) -> dict:
    return json.loads((ROOT / rel_path).read_text())


if __name__ == "__main__":
    evidence_schema = load_schema("schemas/evidence-strength.schema.json")
    operational_schema = load_schema("schemas/operational-feature-matrix.schema.json")
    source_index_schema = load_schema("schemas/source-index.schema.json")

    source_index = json.loads(Path(SOURCE_INDEX_PATH).read_text())
    operational_matrix = json.loads(Path(OPERATIONAL_MATRIX_PATH).read_text())

    Draft202012Validator(source_index_schema).validate(source_index)
    Draft202012Validator(operational_schema).validate(operational_matrix)

    consume_sources = 0
    for source in source_index["sources"]:
        Draft202012Validator(evidence_schema).validate(source["evidence_strength"])
        if source["kind"] == "consume_packet":
            consume_sources += 1
        if source["evidence_strength"]["transcript_derived"]:
            if source["evidence_strength"]["workflow_claim_promotion"] != "blocked":
                raise SystemExit("Transcript-derived workflow claim was incorrectly promotable.")
            if source["evidence_strength"]["strength_class"] == "terminal_or_frame_verified":
                raise SystemExit("Transcript-derived workflow claim was incorrectly upgraded to terminal_or_frame_verified.")
    if consume_sources < 4:
        raise SystemExit("Expected at least four first-party consume packet sources.")

    print(
        json.dumps(
            {
                "status": "pass",
                "consume_source_count": consume_sources,
                "source_index": str(SOURCE_INDEX_PATH.relative_to(ROOT)),
                "operational_matrix": str(OPERATIONAL_MATRIX_PATH.relative_to(ROOT)),
            },
            indent=2,
        )
    )
