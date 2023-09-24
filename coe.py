
from dataclasses import dataclass


@dataclass
class COE:
    """
    Classical orbital elements.
    """
    h: float
    """
    angular momentum (km^2/s)
    """

    e: float
    """
    eccentricity
    """

    ra: float
    """
    right ascension of the ascending node (rad)
    """

    incl: float
    """
    inclination of the orbit (rad)
    """

    w: float
    """
    argument of perigee (rad)
    """

    ta: float
    """
    true anomaly (rad)
    """

    a: float
