#=====================================================#
#
#    File:   zeta_zeroes_plot.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Shows the position of the zeta zeroes along the critical strip
#
#=============================================================================#


from time import time
import numpy as np
from cmath import pi, sin
from scipy.special import gamma
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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
def zeta(x, y=0):
    result = zeta_over_eta(x, y) * eta(x, y)
    return result


def is_sign_change(previous, number):
    print(f'prev: {previous}, number {number}')
    previous_sign = previous / abs(previous)
    number_sign = number / abs(number)
    return previous_sign == number_sign


def animate(i, x_vals, y_vals):
    _zeta = zeta(1/2, i/50)
    print(_zeta.real, _zeta.imag)
    print(x_vals[-10:])
    print(y_vals[-10:])
    if is_sign_change(y_vals[-1].real, _zeta.real) and is_sign_change(y_vals[-1].imag, _zeta.imag):
        x_vals.append(1/2)
        y_vals.append(i/50)

    plt.cla()

    plt.scatter(x_vals, y_vals)

    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.tight_layout()


def plot():
    plt.style.use('dark_background')

    x_vals = [1]
    y_vals = [1]

    ani = FuncAnimation(plt.gcf(), animate, fargs=(x_vals, y_vals,), interval=10)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.tight_layout()
    plt.show()


if __name__=='__main__':
    start = time()
    plot()
    print(f'--- {time()-start} seconds ---')

