from __future__ import annotations

import json

from consume_source_quality_lib import extraction_map_rows, write_handoffs


if __name__ == "__main__":
    write_handoffs()
    print(json.dumps({"extraction_rows": extraction_map_rows()}, indent=2))
