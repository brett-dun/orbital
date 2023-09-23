"""
Orbital Mechanics for Egineering Students (Curtis) - Appendix D.4
"""
from orbital_math import sin, sinh, sqrt


def stumpS(z: float) -> float:
    """
    This function evaluates the Stumpff function S(z) according to equation 3.49.

    :param z:

    :return:
    """
    if z > 0.0:
        return (sqrt(z) - sin(sqrt(z))) / (sqrt(z)**3)
    elif z < 0.0:
        return (sinh(sqrt(-z)) - sqrt(-z)) / (sqrt(-z)**3)
    else:
        return 1.0/6.0
