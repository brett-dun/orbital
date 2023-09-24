
import numpy as np

from coe import COE


def coe_from_sv(mu: float, R: np.ndarray, V: np.ndarray, eps: float = 1e-10) -> COE:
    
    r = np.linalg.norm(R)
    v = np.linalg.norm(V)

    vr = np.dot(R, V) / r

    H = np.cross(R, V)
    h = np.linalg.norm(H)

    # Equation 4.7
    incl = np.arccos(H[2]/h)

    # Equation 4.8
    N = np.cross(np.array([0, 0, 1]), H)
    n = np.linalg.norm(N)

    # Equation 4.9
    if n == 0.0:
        RA = 0.0
    else:
        RA = np.arccos(N[0]/n)
        if N[1] < 0:
            RA = 2 * np.pi - RA
    
    # Equation 4.10
    E = 1/mu * ((v**2 - mu/r) * R - r*vr*V)
    e = np.linalg.norm(E)

    # Equation 4.12
    if e == 0.0:
        w = 0.0
    elif e > eps:
        w = np.arccos(np.dot(N, E)/n/e)
        if E[2] < 0:
            w = 2.0 * np.pi - w
    else:
        w = 0.0

    # Equation 4.13a
    if e > eps:
        TA = np.arccos(np.dot(E, R)/e/r)
        if r < 0:
            TA = 2.0 * np.pi - TA
    else:
        cp = np.cross(N, R)
        if cp[2] >= 0.0:
            TA = 2.0 * np.pi - np.arccos(np.dot(N, R)/n/r)

    # Equation 2.61 (a < 0 for a parabola)
    a = h**2 / mu / (1 - e**2)

    return COE(
        h=h,
        e=e,
        ra=RA,
        incl=incl,
        w=w,
        ta=TA,
        a=a
    )
