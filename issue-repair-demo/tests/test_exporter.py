from csv_guard import Person, export_people_summary, parse_people_csv


SAMPLE_CSV = "name,role,region\nAda Lovelace,Engineer,UK\nGrace Hopper,Computer Scientist,US\n"


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
