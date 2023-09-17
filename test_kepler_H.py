
import pytest

from kepler_H import kepler_H


def test_example_3_05():
    """
    Test that the implementation matches the expected result from example 3.5.
    """
    e = 2.7696
    M = 40.69

    expected = 3.46309
    F = kepler_H(e, M)

    assert F == pytest.approx(expected, rel=1e-6)
