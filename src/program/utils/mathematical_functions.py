from itertools import islice, count
from functools import reduce
import numpy as np
import operator as op
from math import ceil, sqrt, log, floor
import scipy.integrate as integrate


def ncr(n, r):
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


def zeta(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * ncr(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


def is_zeta_zero(real, imag):
    zeta_value = zeta(complex(real, imag))
    return abs(zeta_value) < 10e-3

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


def make_complex(number):
    try:
        number_complex = complex(number.replace('i', 'j'))
    except ValueError as e:
        return False
    else:
        return number_complex


def make_int(number):
    try:
        number_int = int(number)
    except ValueError as e:
        return False
    else:
        return number_int
