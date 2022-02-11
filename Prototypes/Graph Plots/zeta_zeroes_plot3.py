from time import time
import math
from itertools import count, islice
import operator as op
from functools import reduce
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# (utility) binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


def ncr(n, r):
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def zeta(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * ncr(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


def is_root(i, accuracy):
    _zeta = zeta(complex(1/2, i/accuracy))
    if abs(_zeta) < 10e-3:
        return True
    else:
        return False


def animate(i, x_vals, y_vals):
    accuracy = i//500 + 100
    if is_root(i, accuracy):
        y_vals.append(i/accuracy)
        x_vals.append(1/2)
    plt.cla()
    plt.scatter(x_vals, y_vals)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.ylim(0)
    plt.xlim(0, 1)
    plt.tight_layout()


def plot():
    x_vals = []
    y_vals = []
    ani = FuncAnimation(plt.gcf(), animate, fargs=(x_vals, y_vals), interval=1)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.tight_layout()
    plt.show()


if __name__=='__main__':
    start = time()
    plot()
    print(f'--- {time()-start} seconds ---')
