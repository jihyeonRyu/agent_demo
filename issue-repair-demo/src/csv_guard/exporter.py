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
    """Yield newline-terminated records from a CSV payload.

    Also yields the final unterminated line if the input does not
    end with a trailing newline, so that no data row is silently dropped.
    """
    lines = text.splitlines(keepends=True)
    for line in lines:
        if line.endswith("\n"):
            yield line.rstrip("\n")
        elif line:  # unterminated final line – keep it
            yield line


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
