

import numpy as np
from scipy.integrate import quad
from math import log


@np.vectorize
def Ei(x, minfloat=1e-7, maxfloat=10000):
    """Ei integral function."""
    minfloat = min(np.abs(x), minfloat)
    maxfloat = max(np.abs(x), maxfloat)
    def f(t):
        return np.exp(t) / t
    if x > 0:
        return (quad(f, -maxfloat, -minfloat)[0] + quad(f, minfloat, x)[0])
    else:
        return quad(f, -maxfloat, x)[0]


def Li(x):
    return Ei(log(x))


print(Li(100))



