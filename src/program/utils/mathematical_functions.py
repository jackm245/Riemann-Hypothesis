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


from itertools import islice
from functools import reduce
import numpy as np
from operator import mul
from math import ceil, sqrt, log, floor
import scipy.integrate as integrate
from .number_systems import Complex


def ncr(n, r):

    """
    Binomial Coefficient Calculator
    {n \choose r} = \frac{n!}{r! (n-r)!} , \textrm{ for } n \geq r > 0
    """

    r = min(r, n-r)
    numerator = reduce(mul, range(n, n-r, -1), 1)
    denominator = reduce(mul, range(1, r+1), 1)
    return numerator // denominator


def count(start=0, step=1):
    """
    Returns a generator object which contains all values from start
    to whenever the generator will be stopped iterating over, with a given step
    e.g count() -> 1 2 3 4 5 ...
        count(10, 2) -> 10 12 14 16 ...

    """
    n = start
    while True:
        yield n
        n += step


def zeta(real_term, imag_term, number_of_terms=100):

    """
    Riemann Zeta Function
    \zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}
             = \frac{1}{1-2^{1-s}}\sum_{n=0}^{\infty} \frac{1}{2^{n+1}}
             \sum_{k=0}^{n} (-1)^k {n \choose k}(k+1)^{-s}
    This function is implemented using generators
    """
    s = complex(real_term, imag_term)
    if s == 1:
        return Complex('inf')
    else:
        const = 1 / (1 - 2 ** (1 - s))
        term = (1 / 2 ** (n + 1) * sum((-1) ** k * ncr(n, k) * (k + 1) ** (-s)
                                       for k in range(n + 1)) for n in count())
        summation = sum(islice(term, number_of_terms))
        zeta = const * summation
        return Complex(zeta)


def is_zeta_zero(real, imag):

    """
    Given a complex number, the function checks to see if this number is
    approximately a root (zero) of the Riemann Zeta Function
    """

    zeta_value = zeta(real, imag)
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


def integration(func, lower_limit, upper_limit, strips=int(1e6)):
    strip_width = (upper_limit - lower_limit) / strips
    term1 = sum(func(lower_limit + strip_width * h) for h in range(1, strips))
    term2 = 0.5*(func(upper_limit) + func(lower_limit))
    area = strip_width * (term1 + term2)
    return area


def exponential_integral(x, lower_limit=1e-7, upper_limit=10000):

    """
    Exponential integral function
    \mathrm{Ei}(x) = \int_{-x}^{\infty} \frac{e^{-t}}{t}dt
    """
    def func(t):
        return np.exp(t) / t

    lower_limit = min(np.abs(x), lower_limit)
    upper_limit = max(np.abs(x), upper_limit)
    if x > 0:
        return (integrate.quad(func, -upper_limit, -lower_limit)[0]
                + integrate.quad(func, lower_limit, x)[0])
    else:
        return integrate.quad(func, -upper_limit, x)[0]


def logarithmic_integral(N):

    """
    Logaritmic Integral
    \mathrm{Li}(x) = \int_{0}^{x} \frac{dt}{\ln t}
    """

    return exponential_integral(log(N))


def prime_power_function(N):

    """
    Prime Power Function
    \Pi(N) = \pi(N) + \frac{1}{2}\pi(N^{\frac{1}{2}}) +
             \frac{1}{3}\pi(N^{\frac{1}{3}}) + \dots
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
        number_complex = Complex(number.replace('i', 'j'))
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
