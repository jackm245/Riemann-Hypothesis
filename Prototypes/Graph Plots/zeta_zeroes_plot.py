#=============================================================================#
#
#    File:   zeta_zeroes_plot.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Plotting the values of zeta along the critical strip
#
#=============================================================================#


from time import time
import numpy as np
from cmath import pi, sin
from scipy.special import gamma
import matplotlib.pyploy as plt

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
# for x = 1/2
def zeta(x=, y=0):
    result = zeta_over_eta(x, y) * eta(x, y)
    return result

def plot():
    pass

if __name__=='__main__':
    start = time()
    test()
    print(f'--- {time()-start} seconds ---')


