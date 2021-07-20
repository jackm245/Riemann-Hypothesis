#=============================================================================#
#
#    File:   prime_counting_function_plot.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        A plot of the prime counting function,
#
#=============================================================================#


import numpy as np
from time import time
from math import sqrt, ceil, floor, log
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.integrate as integrate


# find the primes up to and including limit
def sieve_of_eratosthenes(limit):
    limit = floor(limit)
    possible_primes = np.ones(limit, dtype=bool)
    possible_primes[0:2:1] = False
    for i in range(2, ceil(sqrt(limit))):
        possible_primes[i*i:limit:i] = False
    return np.flatnonzero(possible_primes)


def prime_counting_function_estimation(N):
    return N/log(N)


@np.vectorize
def exponential_integral(x, minfloat=1e-7, maxfloat=10000):
    """Ei integral function."""
    minfloat = min(np.abs(x), minfloat)
    maxfloat = max(np.abs(x), maxfloat)
    def f(t):
        return np.exp(t) / t
    if x > 0:
        return (integrate.quad(f, -maxfloat, -minfloat)[0] + integrate.quad(f, minfloat, x)[0])
    else:
        return integrate.quad(f, -maxfloat, x)[0]


def logarithmic_integral(N):
    return exponential_integral(log(N))


def prime_power_function(N):
    sum_ = 0
    for r in range(1, floor(log(N, 2))+1):
        sum_ += sieve_of_eratosthenes(N**(1/r)).size
    return sum_


def animate(i, x_vals, y_vals_pcf, y_vals_x_logx, y_vals_li, y_vals_ppf, LIMIT):
    if i >  2:
        x_vals.append(i)
        y_vals_pcf.append(sieve_of_eratosthenes(i).size)
        y_vals_x_logx.append(prime_counting_function_estimation(i))
        y_vals_li.append(logarithmic_integral(i))
        y_vals_ppf.append(prime_power_function(i))
        plt.cla()

        plt.scatter(x_vals, y_vals_pcf, label='Prime Counting Function')
        plt.plot(x_vals, y_vals_x_logx, label='x / log(x)', color='yellow')
        plt.plot(x_vals, y_vals_li, label='Logarithmic Integral', color='green')
        plt.plot(x_vals, y_vals_ppf, label='Prime Power Function', color='blue')

        plt.legend(loc='upper left')
        plt.xlabel('')
        plt.ylabel('')
        plt.tight_layout()


def plot():
    LIMIT = 1*10**6
    plt.style.use('dark_background')

    x_vals = []
    y_vals_pcf = []
    y_vals_x_logx= []
    y_vals_li = []
    y_vals_ppf = []

    animation = FuncAnimation(plt.gcf(), animate, fargs=(x_vals, y_vals_pcf, y_vals_x_logx, y_vals_li, y_vals_ppf, LIMIT), interval=10)
    plt.xlabel('')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    start = time()
    plot()
    print(f'--- {start-time()} seconds ---')
