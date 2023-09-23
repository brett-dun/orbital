
from orbital_math import sin, sinh, sqrt


def stumpS(z: float) -> float:
    if z > 0.0:
        return (sqrt(z) - sin(sqrt(z))) / (sqrt(z)**3)
    elif z < 0.0:
        return (sinh(sqrt(-z)) - sqrt(-z)) / (sqrt(-z)**3)
    else:
        return 1.0/6.0
