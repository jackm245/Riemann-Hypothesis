"""
mathematical_functions.py
=========================

Contains many mathematical functions that are used throughout the program

These Functions include:
    - ncr
    - zeta
    - sieve_of_eratosthenes
    - prime_counting_function_estimation
    - exponential_integral
    - logarithmic_integral
    - prime_power_function
    - make_complex
    - make_int
"""


from itertools import islice, count
from functools import reduce
import numpy as np
import operator as op
from math import ceil, sqrt, log, floor
import scipy.integrate as integrate


__all__ = ['ncr', 'zeta', 'sieve_of_eratosthenes', 'prime_power_function',
        'exponential_integral', 'logarithmic_integral', 'prime_power_function',
        'make_complex', 'make_int']


def ncr(n, r):

    """
    Binomial Coefficient Calculator
    {n \choose r} = \frac{n!}{r! (n-r)!} , \textrm{ for } n \geq r > 0
    """

    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


def zeta(s, t=100):

    """
    Riemann Zeta Function
    \zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}
             = \frac{1}{1-2^{1-s}}\sum_{n=0}^{\infty} \frac{1}{2^{n+1}} \sum_{k=0}^{n} (-1)^k {n \choose k}(k+1)^{-s}

    """

    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * ncr(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


def is_zeta_zero(real, imag):

    """
    Given a complex number, the function checks to see if this number is
    approximately a root (zero) of the Riemann Zeta Function

    """

    zeta_value = zeta(complex(real, imag))
    return abs(zeta_value) < 10e-3


def sieve_of_eratosthenes(limit):

    """
    The Sieve of Eratosthenes return a list of all of the prime numbers up to
    a given limit
    """

    limit = floor(limit)
    possible_primes = np.ones(limit, dtype=bool)
    possible_primes[0:2:1] = False
    for i in range(2, ceil(sqrt(limit))):
        possible_primes[i*i:limit:i] = False
    return np.flatnonzero(possible_primes)


def prime_counting_function_estimation(N):

    """
    Computes \frac{n}{log(n)} in order to estimate the prime counting function
    """

    return N/log(N)


@np.vectorize
def exponential_integral(x, minfloat=1e-7, maxfloat=10000):

    """
    Exponential integral function
    \mathrm{Ei}(x) = \int_{-x}^{\infty} \frac{e^{-t}}{t}dt
    """

    minfloat = min(np.abs(x), minfloat)
    maxfloat = max(np.abs(x), maxfloat)
    def f(t):
        return np.exp(t) / t
    if x > 0:
        return (integrate.quad(f, -maxfloat, -minfloat)[0] + integrate.quad(f, minfloat, x)[0])
    else:
        return integrate.quad(f, -maxfloat, x)[0]


def logarithmic_integral(N):

    """
    Logaritmic Integral
    \mathrm{Li}(x) = \int_{0}^{x} \frac{dt}{\ln t}
    """

    return exponential_integral(log(N))


def prime_power_function(N):

    """
    Prime Power Function
    \Pi(N) = \pi(N) + \frac{1}{2}\pi(N^{\frac{1}{2}}) + \frac{1}{3}\pi(N^{\frac{1}{3}}) + \dots
           =  \sum_{r=1}^{\lfloor log_2  N\rfloor} \pi(N^{\frac{1}{r}})
    """

    total = 0
    for r in range(1, floor(log(N, 2))+1):
        total += sieve_of_eratosthenes(N**(1/r)).size
    return total


def make_complex(number):

    """
    Given the variable number which is of form a+bi or a+bj and of any datatype,
    and where a and b are integers, return this number as one with
    the complex datatype
    """

    try:
        number_complex = complex(number.replace('i', 'j'))
    except ValueError as e:
        return False
    else:
        return number_complex


def make_int(number):

    """
    Given the variable number, return this number with the int datatype if possible
    otherwise, return False
    """

    try:
        number_int = int(number)
    except ValueError as e:
        return False
    else:
        return number_int
