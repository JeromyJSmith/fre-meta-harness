from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from service.inbox_runtime import build_routing_artifacts, scan_inbox_packets, write_router_outputs


def main() -> int:
    results = scan_inbox_packets()
    artifacts = build_routing_artifacts(results)
    write_router_outputs(results, artifacts)
    print(
        json.dumps(
            {
                "packet_count": len(results),
                "routed_count": sum(result.status == "routed" for result in results),
                "blocked_count": sum(result.status == "blocked" for result in results),
                "clarification_count": sum(result.status == "needs_clarification" for result in results),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
