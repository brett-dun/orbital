"""
Orbital Mechanics for Egineering Students (Curtis) - Appendix D.12
Calculation of Julian day number at 0 hr UT
"""
import numpy as np


def J0(year: int, month: int, day: int) -> float:
    """
    This function computes the Julian day number at 0 UT for any year between 1900 and 2100 using Equation 5.48.

    :param year:
    :param month:
    :param day:

    :return: Julian day at 00:00 UTC.
    """
    return 367*year - np.fix(7*(year + np.fix((month + 9)/12))/4) + np.fix(275*month/9) + day +  1721013.5
