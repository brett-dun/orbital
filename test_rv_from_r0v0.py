
import numpy as np
import pytest

from rv_from_r0v0 import rv_from_r0v0


def test_rv_from_r0v0():
    """
    Test that the implementation matches the expected result from example 3.7.
    """
    mu = 398600

    R0 = np.array([7000.0, -12124.0, 0.0])
    V0 = np.array([2.6679, 4.6210, 0.0])
    t = 3600

    # Algorithm 3.4
    R, V = rv_from_r0v0(mu, R0, V0, t)

    expected_R = np.array([-3297.77, 7413.4, 0])
    expected_V = np.array([-8.2976, -0.964045, -0])

    print(R)
    print(V)

    np.testing.assert_almost_equal(R, expected_R, decimal=2)
    np.testing.assert_almost_equal(V, expected_V, decimal=2)
