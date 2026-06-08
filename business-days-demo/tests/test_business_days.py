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


def test_friday_plus_one_skips_weekend():
    """Friday + 1 business day should return Monday (skip Sat/Sun)."""
    # 2026-06-05 is a Friday
    assert add_business_days(date(2026, 6, 5), 1) == date(2026, 6, 8)


def test_friday_plus_two_gives_tuesday():
    """Friday + 2 business days should return Tuesday."""
    # 2026-06-05 is a Friday
    assert add_business_days(date(2026, 6, 5), 2) == date(2026, 6, 9)


def test_crossing_weekend_boundary():
    """Wed + 4 business days should land on next Tuesday."""
    # 2026-06-03 is a Wednesday
    # +1 Thu, +2 Fri, +3 Mon, +4 Tue => 2026-06-09
    assert add_business_days(date(2026, 6, 3), 4) == date(2026, 6, 9)

