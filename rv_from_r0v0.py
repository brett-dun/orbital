"""
Orbital Mechanics for Egineering Students (Curtis) - Appendix D.7
Alogirthm 3.4: Calculation of the state vector (r, v) given the intial state vector (r0, v0) and time lapse dt.
"""
from typing import Tuple
import numpy as np

from f_and_g import f_and_g
from fDot_and_gDot import fDot_and_gDot
from kepler_U import kepler_U


def rv_from_r0v0(mu: float, R0: np.ndarray, V0: np.ndarray, t: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculation of the state vector (r, v) given the intial state vector (r0, v0) and time lapse dt.

    This function computes the state vector (R, V) from the initial state vector (R0, V0) and the elapsed time.

    :param mu: gravitational parameter (km^3/s^3)
    :param R0: initial position vector (km)
    :param V0: initial velocity vector (km/s)

    :return: tuple of final position vector (km) and final velocity vector (km/s)
    """
    assert R0.shape == (3,)
    assert R0.shape == (3,)

    # Magnitudes of R0 and V0.
    r0 = np.linalg.norm(R0)
    v0 = np.linalg.norm(V0)

    # Initial radial velocity.
    vr0 = np.dot(R0, V0)/r0

    # Reciprocal of the semi-major axis. (Calculated from the energy equation.)
    alpha = 2/r0 - v0**2/mu

    # Compute the universal anomaly.
    x = kepler_U(mu, t, r0, vr0, alpha)

    # Compute the f and g functions.
    f, g = f_and_g(mu, x, t, r0, alpha)

    # Compute the final position vector.
    R = f*R0 + g*V0

    # Compute the magnitude of R.
    r = np.linalg.norm(R)

    # Compute the derivatives of f and g.
    fdot, gdot = fDot_and_gDot(mu, x, r, r0, alpha)

    # Compute the final velocity.
    V = fdot*R0 + gdot*V0

    return R, V
