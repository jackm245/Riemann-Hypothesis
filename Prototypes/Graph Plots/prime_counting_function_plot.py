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
from math import sqrt, floor
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# find the primes up to and including limit
def sieve_of_eratosthenes(limit):
    possible_primes = np.ones(limit, dtype=bool)
    possible_primes[0:2:1] = False
    for i in range(2, floor(sqrt(limit))):
        possible_primes[i*i:limit:i] = False
    return np.flatnonzero(possible_primes)


def animate(i, x_vals, y_vals, LIMIT):
    x_vals.append(i)
    y_vals.append(sieve_of_eratosthenes(i).size)
    plt.cla()

    plt.plot(x_vals, y_vals)

    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.tight_layout()


def plot():
    LIMIT = 1*10**6
    plt.style.use('dark_background')

    x_vals = []
    y_vals = []

    animation = FuncAnimation(plt.gcf(), animate, fargs=(x_vals, y_vals, LIMIT), interval=10)
    plt.xlabel('π(N)')
    plt.ylabel('N')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    start = time()
    plot()
    print(f'--- {start-time()} seconds ---')
