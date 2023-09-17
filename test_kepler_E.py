
import pytest

from kepler_E import kepler_E


def test_example_3_02():
    """
    Test that the implementation matches the expected result from example 3.2.
    """
    e = 0.37255
    M = 3.6029

    expected = 3.47942
    E = kepler_E(e, M)

    assert E == pytest.approx(expected, rel=1e-6)
