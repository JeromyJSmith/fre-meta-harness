from __future__ import annotations

import json

from consume_source_quality_lib import refresh_all


if __name__ == "__main__":
    print(json.dumps(refresh_all(), indent=2))
