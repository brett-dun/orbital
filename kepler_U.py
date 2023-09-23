"""
Orbital Mechanics for Egineering Students (Curtis) - Appendix D.5
Alogirthm 3.3: Solution of the Universal Kepler's Equation Using Newton's Method
"""
from orbital_math import sqrt
from stumpC import stumpC
from stumpS import stumpS


def kepler_U(dt: float, ro: float, vro: float, a: float, error: float = 1e-8, nMax: int = 1000) -> float:
    mu = 398600

    x = sqrt(mu) * abs(a) * dt

    n = 0
    ratio = 1
    while abs(ratio) > error and n < nMax:
        n += 1
        C = stumpC(a * x**2)
        S = stumpS(a * x**2)
        F = ro * vro / sqrt(mu) * x**2 * C + (1 - a*ro) * x**3 * S + ro * x - sqrt(mu) * dt
        dFdx = ro*vro/sqrt(mu)*x*(1.0 - a * x**2 * S) + (1 - a*ro) * x**2 * C + ro

        ratio = F/dFdx
        x = x - ratio

    return x
