"""
Orbital Mechanics for Egineering Students (Curtis) - Appendix D.3
Alogirthm 3.2: Solution of Kepler's Equation for the Hyperbola Using Newton's Method
"""
from orbital_math import cosh, sinh


def kepler_H(e: float, M: float, error: float = 1e-8) -> float:
    """
    Solution of Kepler's Equation for the Hyperbola Using Newton's Method

    This equation uses Newton's method to solve Kepler's equation for the hyperbola
    e*sinh(F) - F = M for the hyperbolic eccentricity and the hyperbolic mean anomaly.

    :param e: eccentricity
    :param M: hyperbolic mean anomaly (dimensionless)
    :param error: error tolerance (unitless), defaults to 1e-8

    :return: hyperbolic eccentric anomaly (dimensionless)
    """
    # Starting value for F.
    F = M

    # Iterate on equation 3.42 until F is determined to within the error tolerance.
    ratio = 1
    while abs(ratio) > error:
        ratio = (e*sinh(F) - F - M)/(e*cosh(F) - 1)
        F = F - ratio
    
    return F
