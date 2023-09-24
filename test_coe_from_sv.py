
import pytest
import numpy as np

from coe import COE
from coe_from_sv import coe_from_sv


def test_coe_from_sv():
    mu = 398600

    r = np.array([-6045.0, -3490.0, 2500.0])
    v = np.array([-3.457, 6.618, 2.533])

    expected_coe = COE(
        h=58311.7,
        e=0.171212,
        ra=np.deg2rad(255.279),
        incl=np.deg2rad(153.249),
        w=np.deg2rad(20.0683),
        ta=np.deg2rad(28.4456),
        a=8788.1
    )

    coe = coe_from_sv(mu, r, v)

    assert coe.h == pytest.approx(expected_coe.h, rel=1e-3)
    assert coe.e == pytest.approx(expected_coe.e, rel=1e-3)
    assert coe.ra == pytest.approx(expected_coe.ra, rel=1e-3)
    assert coe.incl == pytest.approx(expected_coe.incl, rel=1e-3)
    assert coe.w == pytest.approx(expected_coe.w, rel=1e-3)
    assert coe.ta == pytest.approx(expected_coe.ta, rel=1e-3)
    assert coe.a == pytest.approx(expected_coe.a, rel=1e-3)
