
from typing import Tuple

from orbital_math import sqrt
from stumpC import stumpC
from stumpS import stumpS


def fDot_and_gDot(mu: float, x: float, r: float, ro: float, a: float) -> Tuple[float, float]:

    z = a * x**2

    # Equation 3.66c
    fdot = sqrt(mu)/r/ro * (z*stumpS(z) - 1.0) * x

    # Equation 3.66d
    gdot = 1.0 - x**2/r * stumpC(z)

    return fdot, gdot
