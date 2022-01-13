#=============================================================================#
#
#    File:    critical_strip_plot.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Plotting the values of zeta along the critical strip
#
#=============================================================================#


from time import time
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
    accuracy = 100
    _zeta = zeta((1/2)+(i*1j/accuracy))
    #  if _zeta == 0:
    #  if str(abs(_zeta))[:5] == '0.000':
    print(f'1/2 + ({i*1j/accuracy}) \t {_zeta}')
    x_vals.append(_zeta.real)
    y_vals.append(_zeta.imag)
    plt.cla()

    plt.plot(x_vals, y_vals)

    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.tight_layout()


def plot():
    plt.style.use('dark_background')

    x_vals = []
    y_vals = []

    ani = FuncAnimation(plt.gcf(), animate, fargs=(x_vals, y_vals,), interval=1)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.tight_layout()
    plt.show()


if __name__=='__main__':
    start = time()
    plot()
    print(f'--- {time()-start} seconds ---')


