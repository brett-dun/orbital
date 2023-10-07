import numpy as np

from gibbs import gibbs


def test_gibs():
    mu = 398600

    r1 = np.array([-294.32, 4265.1, 5986.7])
    r2 = np.array([-1365.4, 3637.6, 6346.8])
    r3 = np.array([-2940.3, 2473.7, 6555.8])

    v2 = gibbs(mu, r1, r2, r3)
    print(v2)

    expected_v2 = np.array([-6.2176, -4.01237, 1.59915])

    np.testing.assert_almost_equal(v2, expected_v2, decimal=5)
