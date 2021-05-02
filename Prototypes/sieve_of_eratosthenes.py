#=============================================================================#
#
#    File:   sieve_of_eratosthenes.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Uses a sieve to find all of the prime numbers up to a limit
#        Three versions, each faster than the last
#
#=============================================================================#


import numpy as np
from time import time
from math import sqrt, floor


# print the prime numbers up to limit
# first version
def sieve_of_eratosthenes_1(limit):
    possible_primes = [True for _ in range(limit)]
    possible_primes[0] = possible_primes[1] = False
    for index, isprime in enumerate(possible_primes):
        if isprime:
            yield index
            for i in range(index**2, limit, index):
                possible_primes[i] = False
    return possible_primes


#second version
def sieve_of_eratosthenes_2(limit):
    possible_primes = np.ones(limit)
    possible_primes[0:2:1] = 0
    for (i, isprime) in enumerate(possible_primes):
        if bool(isprime):
            yield i
            possible_primes[i*i:limit:i] = 0
    return possible_primes

# third version
def sieve_of_eratosthenes_3(limit):
    possible_primes = np.ones(limit, dtype=bool)
    possible_primes[0:2:1] = False
    for i in range(2, floor(sqrt(limit))):
        possible_primes[i*i:limit:i] = False
    return np.flatnonzero(possible_primes)


def main():
    limit = 1*10**6

    start1 = time()
    print(list(sieve_of_eratosthenes_1(limit)))
    end1 = time()

    start2 = time()
    print(list(sieve_of_eratosthenes_2(limit)))
    end2 = time()

    start3 = time()
    print(sieve_of_eratosthenes_3(limit))
    end3 = time()

    print(f'time 1: {end1-start1} seconds')
    print(f'time 2: {end2-start2} seconds')
    print(f'time 3: {end3-start3} seconds')


if __name__ == "__main__":
    main()
