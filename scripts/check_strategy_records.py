#!/usr/bin/env python3
"""Validate stable identifiers and row shape in the public Core roadmap."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROADMAP = ROOT / "docs" / "product" / "ROADMAP.md"
IDEA_ID = re.compile(r"SG-\d{4}")


def main() -> int:
    failures: list[str] = []
    rows: list[list[str]] = []
    for line in ROADMAP.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and IDEA_ID.fullmatch(cells[0]):
            rows.append(cells)

    identifiers: set[str] = set()
    for cells in rows:
        identifier = cells[0]
        if identifier in identifiers:
            failures.append(f"duplicate public roadmap identifier: {identifier}")
        identifiers.add(identifier)
        if len(cells) != 5:
            failures.append(
                f"{identifier}: public roadmap row must have 5 columns, found {len(cells)}"
            )

    if failures:
        print("Public roadmap validation failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(f"Public Core roadmap is valid: {len(rows)} active initiatives.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
