#=============================================================================#
#
#    File:   zeta_calculator.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        The user will input a value into the zeta calculator
#        The program will output the result
#        A step-by-step solution will be shown
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


def get_float_input(message):
    while 1:
        user_input = input(message)
        try:
            float_input = float(user_input)
        except ValueError:
            print("Input must be a real number\nPlease try again")
        else:
            return float_input


def get_user_input():
    print('Enter the value for which you would like to find the zeta value of')
    print('In the form a ± bi)')
    real_input = get_float_input('a : ')
    imag_input = get_float_input('b : ')
    return real_input + imag_input * 1j


def calculator():
    user_input = get_user_input()
    zeta_of_input = zeta(user_input.real, user_input.imag)
    # would use printing function of complex class
    print(f'ζ{user_input} = {zeta_of_input}')


if __name__=='__main__':
    start = time()
    calculator()
    print(f'--- {time()-start} seconds ---')
