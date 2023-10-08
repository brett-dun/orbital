import pytest

from julian_day import J0


def test_J0():
    """
    Test that the implementation matches the expected result from example 5.04.
    """
    year = 2004
    month = 5
    day = 12

    j0 = J0(year, month, day)

    hour = 14
    minute = 45
    second = 30
    ut = hour + minute/60 + second/3600

    jd = j0 + ut/24

    expected = 2453138.115

    assert jd == pytest.approx(expected, rel=1e-6)
