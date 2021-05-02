#=============================================================================#
#
#    File:   euler_product_formula.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Calculate zeta by a product of primes
#        Where \zeta(s) = \prod_{p, prime} \frac{1}{1-p^{^{-s}}}
#
#=============================================================================#


from time import time
import numpy as np
from math import floor, sqrt, pi

def sieve_of_eratosthenes(limit):
    possible_primes = np.ones(limit, dtype=bool)
    possible_primes[0:2:1] = False
    for i in range(2, floor(sqrt(limit))):
        possible_primes[i*i:limit:i] = False
    return np.flatnonzero(possible_primes)


def zeta(s):
    limit = 1*10**6
    primes = sieve_of_eratosthenes(limit).astype(float)
    elements = 1/(1-primes**(-s))
    return np.prod(elements)


def test():
    TOL = 1e-3

    test_case_1 = zeta(3.0 + 4.5 * 1j)
    test_case_2 = zeta(1 - 2.5 * 1j)
    test_case_3 = zeta(2 + 0 * 1j)
    
    # true values taken from wolfram alpha
    test1 = abs(test_case_1.real - 0.89796690) < TOL and abs(test_case_1.imag - 0.023707555) < TOL
    test2 = abs(test_case_2.real - 0.61134995) < TOL and abs(test_case_2.imag - 0.213320800) < TOL
    test3 = abs(test_case_3.real - pi**2/6) < TOL and abs(test_case_3.imag - 0.000000000) < TOL

    print(f'test1: {test1}\ntest2: {test2}\ntest2: {test3}')


if __name__=='__main__':
    start = time()
    test()
    print(f'--- {time()-start} seconds ---')


