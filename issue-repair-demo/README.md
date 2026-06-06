# Issue Repair Demo

A small Python CSV utility for demonstrating an agent-driven GitHub issue workflow.

The app reads a CSV of people and exports a compact summary CSV.

## Setup

```bash
cd issue-repair-demo
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Run Tests

```bash
python -m pytest
```

## Run The CLI

```bash
python -m csv_guard examples/team.csv
```

Expected output:

```csv
name,label
Ada Lovelace,Engineer - UK
Grace Hopper,Computer Scientist - US
```

## Demo Flow

Use this project with a GitHub issue that describes a CSV edge case. The intended demo path is:

1. Read the GitHub issue.
2. Add a regression test that reproduces the bug.
3. Run the test and observe failure.
4. Patch the parser.
5. Run the full test suite.
6. Write a PR title and summary.
