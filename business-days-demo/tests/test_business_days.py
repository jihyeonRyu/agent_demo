from datetime import date

import pytest

from business_days import add_business_days


def test_zero_days_returns_start_date():
    assert add_business_days(date(2026, 6, 1), 0) == date(2026, 6, 1)


def test_adds_weekday_business_days():
    assert add_business_days(date(2026, 6, 1), 2) == date(2026, 6, 3)


def test_rejects_negative_days():
    with pytest.raises(ValueError, match="non-negative"):
        add_business_days(date(2026, 6, 1), -1)

