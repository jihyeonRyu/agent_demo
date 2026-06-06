from __future__ import annotations

import argparse
from pathlib import Path

from .exporter import export_people_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Export a compact people summary from CSV.")
    parser.add_argument("csv_path", type=Path, help="Path to a CSV file with name, role, region columns")
    args = parser.parse_args()

    print(export_people_summary(args.csv_path.read_text(encoding="utf-8")), end="")


if __name__ == "__main__":
    main()
