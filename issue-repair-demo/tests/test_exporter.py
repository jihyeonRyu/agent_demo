from csv_guard import Person, export_people_summary, parse_people_csv


SAMPLE_CSV = "name,role,region\nAda Lovelace,Engineer,UK\nGrace Hopper,Computer Scientist,US\n"

CSV_NO_TRAILING_NEWLINE = (
    "name,role,region\n"
    "Ada Lovelace,Engineer,UK\n"
    "Grace Hopper,Computer Scientist,US"
)


def test_parse_people_csv_returns_people() -> None:
    assert parse_people_csv(SAMPLE_CSV) == [
        Person(name="Ada Lovelace", role="Engineer", region="UK"),
        Person(name="Grace Hopper", role="Computer Scientist", region="US"),
    ]


def test_export_people_summary_formats_labels() -> None:
    assert export_people_summary(SAMPLE_CSV) == (
        "name,label\n"
        "Ada Lovelace,Engineer - UK\n"
        "Grace Hopper,Computer Scientist - US\n"
    )


# ── Regression tests for missing trailing newline ──────────────────

def test_parse_people_csv_missing_trailing_newline() -> None:
    """parse_people_csv must not drop the last row when there is no trailing newline."""
    people = parse_people_csv(CSV_NO_TRAILING_NEWLINE)
    assert people == [
        Person(name="Ada Lovelace", role="Engineer", region="UK"),
        Person(name="Grace Hopper", role="Computer Scientist", region="US"),
    ]


def test_export_people_summary_missing_trailing_newline() -> None:
    """export_people_summary must include the last row in the output when
    the input CSV does not end with a newline character."""
    result = export_people_summary(CSV_NO_TRAILING_NEWLINE)
    assert result == (
        "name,label\n"
        "Ada Lovelace,Engineer - UK\n"
        "Grace Hopper,Computer Scientist - US\n"
    )
