from __future__ import annotations

import json

from consume_source_quality_lib import build_consume_packet_sources


if __name__ == "__main__":
    print(json.dumps({"sources": build_consume_packet_sources()}, indent=2))
