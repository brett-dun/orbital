"""
Orbital Mechanics for Egineering Students (Curtis) - Appendix D.2
Alogirthm 3.1: Solution of Kepler's Equation by Newton's Method
"""
from orbital_math import cos, sin, pi


def kepler_E(e: float, M: float, error: float = 1e-8) -> float:
    """
    Solution of Kepler's Equation by Newton's Method

    This function uses Newton's method to solve Kepler's equation E - e*sin(E) = M
    for the eccentric anomaly, given the eccentricity and the mean anomaly.

    
    :param e: eccentricity (unitless)
    :param M: mean anomaly (radians)
    :param error: error tolerance (unitless), defaults to 1e-8

    :return: E the eccentric anomaly (radians)
    """
    # Select a starting value for E.
    if M < pi:
        E = M + e/2
    else:
        E = M - e/2

    # Iterate on equation 3.14 until E is determined to within the error tolerance.
    ratio = 1
    while abs(ratio) > error:
        ratio = (E - e*sin(E) - M)/(1 - e*cos(E))
        E = E - ratio
    
    return E
