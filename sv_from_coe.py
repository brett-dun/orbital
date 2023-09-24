
from typing import Tuple
import numpy as np
from numpy import cos, sin

from coe import COE


def sv_from_coe(mu: float, coe: COE) -> Tuple[np.array, np.array]:
    """
    Compute the state vector (r, v) from th e classical orbital elements (coe).
    The MATLAB implementation of this algorithm is given by D.9 in Orbital Mechanics for Engineering Students by Howard Curtis.

    :param coe: Classical orbital elements object.
    :param mu: Gravitational parameter (km^3/s^2)

    :return: state vector as a tuple
    """

    # equations 4.45 and 4.46 (rp and vp are column vectors)
    # rp - position vector in the perifocal frame (km)
    # vp - velocity vector in the perifocal frame (km/s)
    rp = (coe.h**2 / mu) * (1 / (1 + coe.e * cos(coe.ta))) * (cos(coe.ta) * np.array([1, 0, 0]) + sin(coe.ta) * np.array([0, 1, 0]))
    assert rp.shape == (3,)
    vp = (mu / coe.h) * (-sin(coe.ta) * np.array([1, 0, 0]) + (coe.e + cos(coe.ta)) * np.array([0, 1, 0]))
    assert vp.shape == (3,)

    # equation 4.34 (rotation matrix about the z-axis through the angle RA)
    R3_W = np.array([[cos(coe.ra), sin(coe.ra), 0.0],
                     [-sin(coe.ra), cos(coe.ra), 0.0],
                     [0.0, 0.0, 1.0]])
    assert R3_W.shape == (3,3)
    
    # equation 4.32
    R1_i = np.array([[1.0, 0.0, 0.0],
                     [0.0, cos(coe.incl), sin(coe.incl)],
                     [0.0, -sin(coe.incl), cos(coe.incl)]])
    assert R1_i.shape == (3,3)

    # equation 4.34
    R3_w = np.array([[cos(coe.w), sin(coe.w), 0.0],
                     [-sin(coe.w), cos(coe.w), 0.0],
                     [0.0, 0.0, 1.0]])
    assert R3_w.shape == (3,3)

    # equation 4.49
    Q_pX = (R3_W.transpose() @ R1_i.transpose() @ R3_w.transpose())
    assert Q_pX.shape == (3,3)

    # equation 4.51
    r = Q_pX @ rp
    v = Q_pX @ vp

    # convert to row vectors
    r = r.transpose()
    v = v.transpose()
    
    return r, v
