#=============================================================================#
#
#    File:   logarithmic_integral.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Find the Logarithmic Integral of a number
#        Li(x)
#
#=============================================================================#


import scipy.integrate as integrate
from math import log


def reciprocal_log(t):
    if t == 1:
        return 0
    else:
        return 1/log(t)


# Li(N) = \int_{0}^{N}\frac{dt}{\ln{t}}
# def Li(N):
    # return integrate.quad(lambda t: 1/log(t), 0.000000001, N)

def Li(N):
    return integrate.quad(reciprocal_log, 0, N)[0]

print(1, Li(4))
