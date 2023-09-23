"""
Orbital Mechanics for Egineering Students (Curtis) - Appendix D.4
"""
from orbital_math import cos, cosh, sqrt


def stumpC(z: float) -> float:
    """
    This function evaluates the Stumpff function C(z) according to equation 3.50.

    :param z:

    :return:
    """
    if z > 0.0:
        return (1.0 - cos(sqrt(z))) / z
    elif z < 0.0:
        return (cosh(sqrt(-z)) - 1) / (-z)
    return 1.0/2.0
