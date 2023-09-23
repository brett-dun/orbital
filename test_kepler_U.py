
import pytest

from kepler_U import kepler_U


def test_example_3_06():
    """
    Test that the implementation matches the expected result from example 3.5.
    """
    mu = 398600

    dt = 3600
    ro = 10000
    vro = 3.0752
    a = -19655

    expected = 128.511
    x = kepler_U(mu, dt, ro, vro, 1/a)

    assert x == pytest.approx(expected, rel=1e-3)
