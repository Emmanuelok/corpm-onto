from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from corruptpm.validate import validate_project


def main() -> None:
    result = validate_project(root=ROOT)
    print(result.report_text.strip())
    raise SystemExit(0 if result.conforms else 1)


if __name__ == "__main__":
    main()
