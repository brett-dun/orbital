
import pytest
import numpy as np

from coe import COE
from sv_from_coe import sv_from_coe


def test_sv_from_coe():

    mu = 398600

    coe = COE(
        h=80000,
        e=1.4,
        ra=np.deg2rad(40),
        incl=np.deg2rad(30),
        w=np.deg2rad(60),
        ta=np.deg2rad(30),
        a=0  # TODO: this shouldn't be in here
    )
    
    expected_r = np.array([-4039.9, 4814.56, 3628.62])
    expected_v = np.array([-10.386, -4.77192, 1.74388])

    r, v = sv_from_coe(mu, coe)
    
    assert r.shape == (3,)
    assert v.shape == (3,)

    np.testing.assert_almost_equal(r, expected_r, decimal=2)
    np.testing.assert_almost_equal(v, expected_v, decimal=2)
