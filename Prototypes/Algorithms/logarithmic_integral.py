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


def Li(N):
    return integrate.quad(lambda t: 1/log(t), 0.000000000000000000000000000000000000000000000000000000000000000000000000001, N)

print(Li(4))
