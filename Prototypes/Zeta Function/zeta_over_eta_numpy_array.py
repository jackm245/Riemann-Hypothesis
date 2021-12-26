#=============================================================================#
#
#    File:   zeta_over_eta_numpy_array
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Using the value of zeta divided by eta to calculate the zeta function
#        The value of eta is calculated using numpy arrays rather than scalar quanitities
#
#=============================================================================#


from time import time
import numpy as np
from math import pi

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


# returns value of \zeta(s)
# where s \equiv r + it ,r,t \in \mathbb{C}
# by computing \frac{\zeta(s)\eta(s)}
def zeta(x, y):
    if not x > 0:
        raise ValueError(f'Cannot Compute Zeta({x}, {y})\nReal part {x} is out of domain x > 0')

    result = zeta_over_eta(x, y) * eta(x, y)

    return result.real, result.imag


def test():
    TOL = 1e-3

    test_case_1 = zeta(3.0, 4.5)
    test_case_2 = zeta(1, -2.5)
    test_case_3 = zeta(2, 0)
    test_case_4 = zeta(7, 5)

    # true values taken from wolfram alpha
    test1 = abs(test_case_1[0] - 0.89796690) < TOL and abs(test_case_1[1] - 0.023707555) < TOL
    test2 = abs(test_case_2[0] - 0.61134995) < TOL and abs(test_case_2[1] - 0.213320800) < TOL
    test3 = abs(test_case_3[0] - pi**2/6) < TOL and abs(test_case_3[1] - 0.000000000) < TOL

    print(f'test1: {test1}\ntest2: {test2}\ntest2: {test3}')
    print(test_case_4)


if __name__=='__main__':
    start = time()
    test()
    print(f'--- {time()-start} seconds ---')
