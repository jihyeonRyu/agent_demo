from __future__ import annotations

import csv
from dataclasses import dataclass
from io import StringIO


@dataclass(frozen=True)
class Person:
    name: str
    role: str
    region: str


def _complete_lines(text: str):
    """Yield newline-terminated records from a CSV payload."""
    for line in text.splitlines(keepends=True):
        if not line.endswith("\n"):
            continue
        yield line.rstrip("\n")


def parse_people_csv(text: str) -> list[Person]:
    reader = csv.DictReader(_complete_lines(text))
    people: list[Person] = []

    for row in reader:
        people.append(
            Person(
                name=row["name"].strip(),
                role=row["role"].strip(),
                region=row["region"].strip(),
            )
        )

    return people


def export_people_summary(text: str) -> str:
    people = parse_people_csv(text)
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")

    writer.writerow(["name", "label"])
    for person in people:
        writer.writerow([person.name, f"{person.role} - {person.region}"])

    return output.getvalue()
