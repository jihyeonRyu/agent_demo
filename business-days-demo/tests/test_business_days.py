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


def test_skip_weekend_friday_to_monday():
    """Friday + 1 business day should skip Sat/Sun and land on Monday."""
    assert add_business_days(date(2026, 6, 5), 1) == date(2026, 6, 8)


def test_friday_plus_two_returns_tuesday():
    """Friday + 2 business days should skip weekend and return Tuesday."""
    assert add_business_days(date(2026, 6, 5), 2) == date(2026, 6, 9)


def test_cross_weekend_boundary():
    """Wednesday + 4 business days should land on next Monday."""
    # June 3, 2026 is a Wednesday
    # +1=Thu(6/4), +2=Fri(6/5), +3=Mon(6/8), +4=Tue(6/9)
    assert add_business_days(date(2026, 6, 3), 4) == date(2026, 6, 9)


def test_add_business_days_across_month():
    """Test that business day addition works across month boundaries."""
    # Jan 30, 2026 is a Friday
    # +1 business day = Mon Feb 2 (skips Sat Jan 31 and Sun Feb 1)
    assert add_business_days(date(2026, 1, 30), 1) == date(2026, 2, 2)


def test_add_business_days_across_year():
    """Test that business day addition works across year boundaries."""
    # Dec 31, 2026 is a Thursday
    # +1 = Fri Dec 31, +2 = Mon Jan 4
    assert add_business_days(date(2026, 12, 31), 1) == date(2027, 1, 1)
    assert add_business_days(date(2026, 12, 31), 2) == date(2027, 1, 4)
