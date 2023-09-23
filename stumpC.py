
from orbital_math import cos, cosh, sqrt


def stumpC(z: float) -> float:
    if z > 0.0:
        return (1.0 - cos(sqrt(z))) / z
    elif z < 0.0:
        return (cosh(sqrt(-z)) - 1) / (-z)
    return 1.0/2.0
