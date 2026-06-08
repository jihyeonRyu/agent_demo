from __future__ import annotations

import argparse
from datetime import date, timedelta


def add_business_days(start: date, days: int) -> date:
    """Return the date after adding business days, skipping Saturdays and Sundays."""
    if days < 0:
        raise ValueError("days must be non-negative")

    current = start
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Mon=0 .. Fri=4
            added += 1
    return current


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add business days to a date.")
    parser.add_argument("start", help="Start date in YYYY-MM-DD format")
    parser.add_argument("days", type=int, help="Number of business days to add")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    start = date.fromisoformat(args.start)
    print(add_business_days(start, args.days).isoformat())


if __name__ == "__main__":
    main()

