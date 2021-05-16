#=============================================================================#
#
#    File:   zeta_combined.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Using the value of zeta divided by eta to calculate the zeta function
#        Calculates the value of zeta for all inputs
#
#=============================================================================#


from time import time
import numpy as np
from cmath import pi, sin
from scipy.special import gamma


# returns the value of \frac{\zeta(s)}{\eta(s)}
# = \frac{ 2^{iy}}{2^{iy}-2^{1-x}}
def zeta_over_eta(x, y):
    A = -2**(1 - x)
    B = 2**(y * 1j)
    zeta_over_eta = B / (A + B)
    return zeta_over_eta


# approximates the eta function where
# r is the real part of the input (r\equiv\Re(s))
# and t is the imaginary part of the input (t\equiv\Im(s))
# \eta(r+it)=\sum_{n=1}^\infty\frac{(-1)^{n-1}}{n^r}[cos(y\phi_n)-isin(y\phi_n)]
def eta(x, y, limit=5*10**3):
    n = np.arange(1, limit)
    coefficient = (-1)**(n-1) / n**x
    phi_y = np.log(n) * y
    real_parts = coefficient * np.cos(phi_y)
    imaginary_parts = coefficient * np.sin(phi_y)

    real_summation = real_parts.sum()
    imaginary_summation = imaginary_parts.sum()
    eta = real_summation - imaginary_summation * 1j

    return eta


# \zeta(s) = 2^{s} \cdot  \pi^{s-1} \cdot \sin(\frac{\pi s}{2})\cdot \Gamma(1-s)\cdot \zeta(1-s)
def riemanns_functional_equation(x, y, limit=5*10**3):
    s = x + y * 1j
    _zeta = (2**s)*(pi**(s-1))*sin(pi*s/2)*gamma(1-s)*zeta((1-s).real, (1-s).imag)
    return _zeta


# returns value of \zeta(s)
# where s \equiv r + it ,r,t \in \mathbb{C}
# by computing \frac{\zeta(s)\eta(s)}
def zeta(x, y=0):
    if x < 0:
        result = riemanns_functional_equation(x, y)
    elif x >= 0:
        if x == 1:
            raise ValueError(f'zeta({x}+{y}j) is undefined')
        result = zeta_over_eta(x, y) * eta(x, y)
    return result


def test():
    TOL = 1e-3

    test_case_1 = zeta(-3.0, 4.5)
    test_case_2 = zeta(-1, -2.5)
    test_case_3 = zeta(-2, 0)
    test_case_4 = zeta(2)

    # true values taken from wolfram alpha
    print(test_case_1)
    test1 = abs(test_case_1.real - -0.06603051) < TOL and abs(test_case_1.imag - 0.390014416) < TOL
    test2 = abs(test_case_2.real - 0.226906) < TOL and abs(test_case_2.imag - 0.0120162) < TOL
    test3 = abs(test_case_3.real - 0.0000000) < TOL and abs(test_case_3.imag - 0.000000000) < TOL
    test4 = abs(test_case_4.real - pi**2/6) < TOL and abs(test_case_4.imag - 0.00000000) < TOL

    print(f'test1: {test1}\ntest2: {test2}\ntest3: {test3}\ntest4: {test4}')


if __name__=='__main__':
    start = time()
    test()
    print(f'--- {time()-start} seconds ---')

