from __future__ import annotations

import json

from consume_source_quality_lib import build_operational_feature_matrix, write_json, OPERATIONAL_MATRIX_PATH


if __name__ == "__main__":
    payload = build_operational_feature_matrix()
    write_json(OPERATIONAL_MATRIX_PATH, payload)
    print(json.dumps(payload, indent=2))
