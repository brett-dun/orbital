
from typing import Tuple

from orbital_math import sqrt
from stumpC import stumpC
from stumpS import stumpS


def f_and_g(mu: float, x: float, t: float, ro: float, a: float) -> Tuple[float, float]:
    
    z = a * x**2

    # Equation 3.66a
    f = 1 - x**2 / ro * stumpC(z)

    # Equation 3.66b
    g = t - 1/sqrt(mu) * x**3 * stumpS(z)

    return f, g
