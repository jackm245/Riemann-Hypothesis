#=============================================================================#
#
#    File:   zeta_approximation.py
#    Author: Jack Morgan
#    Date:   December 2021
#    Description:
#        Displays a plot of the approximation of the output from
#        The Riemann Zeta Function
#
#=============================================================================#


from time import time
#  import numpy as np
#  from cmath import pi, sin
#  from scipy.special import gamma
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count, islice


# (utility) binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


# formula (21) in http://mathworld.wolfram.com/RiemannZetaFunction.html
# Global zeta function by Knopp and Hasse (s != 1)
def zeta(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


def animate(i, x_vals, y_vals):
    _zeta = zeta(2+50j, i)
    x_vals.append(_zeta.real)
    y_vals.append(_zeta.imag)
    plt.cla()

    plt.plot(x_vals, y_vals)
    plt.scatter(x_vals, y_vals)

    plt.xlabel('Re')
    plt.tight_layout()
    plt.ylabel('Im')


def plot():
    plt.style.use('dark_background')

    x_vals = []
    y_vals = []

    ani = FuncAnimation(plt.gcf(), animate, fargs=(x_vals, y_vals,), frames=1000, interval=1)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    start = time()
    plot()
    print(f'--- {time()-start} seconds ---')
