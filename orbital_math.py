
USE_NUMPY = True

if USE_NUMPY:
    import numpy as np

    cos = np.cos
    cosh = np.cosh
    sin = np.sin
    sinh = np.sinh
    sqrt = np.sqrt
    pi = np.pi
else:
    import math

    cos = math.cos
    cosh = math.cosh
    sin = math.sin
    sinh = math.sinh
    sqrt = math.sqrt
    pi = math.pi
