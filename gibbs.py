from typing import Optional
import numpy as np


def gibbs(mu: float, R1: np.ndarray, R2: np.ndarray, R3: np.ndarray, tol: float = 1e-4) -> Optional[np.ndarray]:
    """
    ...

    :param mu:
    :param R1:
    :param R2:
    :param R3:
    :param tol:
    
    :return:
    """

    # Magnitudes of R1, R2, R3.
    r1 = np.linalg.norm(R1)
    r2 = np.linalg.norm(R2)
    r3 = np.linalg.norm(R3)

    # Cross products.
    c12 = np.cross(R1, R2)
    assert c12.shape == (3,)
    c23 = np.cross(R2, R3)
    assert c23.shape == (3,)
    c31 = np.cross(R3, R1)
    assert c31.shape == (3,)

    # Check that R1, R2, and R3 are coplanar.
    val = abs(np.dot(R1, c23)/r1/np.linalg.norm(c23))
    print(val)
    if val > tol:
        return None
    
    # Equation 5.13
    N = r1*c23 + r2*c31 + r3*c12
    assert N.shape == (3,)

    # Equation 5.14
    D = c12 + c23 + c31
    assert D.shape == (3,)

    # Equation 5.21
    S = R1*(r2 - r3) + R2*(r3 - r1) + R3*(r1 - r2)
    assert S.shape == (3,)

    # Equation 5.22
    return np.sqrt(mu/np.linalg.norm(N)/np.linalg.norm(D)) * (np.cross(D, R2)/r2 + S)
