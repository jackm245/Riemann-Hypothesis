#=============================================================================#
#
#    File:   zeta_over_eta_scalar.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Using Scalar quanities to calculate the zeta function
#        By calculating the zeta function divided by the eta function
#
#=============================================================================#

from time import time
from math import log, cos, sin, pi


# returns the value of \frac{\zeta(s)}{\eta(s)}
# = \frac{ 2^{iy}}{2^{iy}-2^{1-x}} 
def zeta_over_eta(r, t): 
    x = -2**(1-r)
    y = 2**(1j * t)
    res = y / (x + y)
    return res


# approximates the eta function where 
# r is the real part of the input (r\equiv\Re(s))
# and t is the imaginary part of the input (t\equiv\Im(s)) 
# \eta(r+it)=\sum_{n=1}^\infty\frac{(-1)^{n-1}}{n^r}[cos(y\phi_n)-isin(y\phi_n)] 
def eta(r, t):
    # more terms means greater accuracy, but longer computation time
    TERMS = 1 * 10**6
    Re = 0
    Im = 0
    for n in range(1, TERMS+1):
        A = (-1)**(n-1) / n**r
        Pt = t * log(n)
        Re += A * cos(Pt)
        Im -= A * sin(Pt)
    eta = Re +  Im * 1j
    return eta


# returns value of \zeta(s) 
# where s \equiv r + it ,r,t \in \mathbb{C}
# by computing \frac{\zeta(s)\eta(s)}
def zeta(s):
    r = s.real
    t = s.imag
    if not r > 0:
        raise ValueError('Real part of input must be greater than 0')
    zeta = zeta_over_eta(r, t) * eta(r, t)
    return zeta


def main():
    test_cases = [-1, 0, 0+3j, 0.5, 1, 2, 10+15j]
    for test in test_cases:
        try:
            print(f'input: {test}\toutput:{zeta(test)}')
        except ZeroDivisionError as e:
            print(f'{test} error: {e}')
        except ValueError as f:
            print(f'{test} error: {f}')


def test():
    TOL = 1e-3

    test_case_1 = zeta(3.0 + 4.5 * 1j)
    test_case_2 = zeta(1 - 2.5 * 1j)
    test_case_3 = zeta(2 + 0 * 1j)
    
    # true values taken from wolfram alpha
    test1 = abs(test_case_1.real - 0.89796690) < TOL and abs(test_case_1.imag - 0.023707555) < TOL
    test2 = abs(test_case_2.real - 0.61134995) < TOL and abs(test_case_2.imag - 0.213320800) < TOL
    test3 = abs(test_case_3.real - pi**2/6) < TOL and abs(test_case_3.imag - 0.000000000) < TOL

    print(f'test1: {test1}\ntest2: {test2}\ntest2: {test3}')


if __name__=='__main__':
    start = time()
    test()
    print(f'--- {time()-start} seconds ---')

