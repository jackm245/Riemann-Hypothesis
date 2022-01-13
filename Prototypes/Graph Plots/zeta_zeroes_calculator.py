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
import math
from itertools import count, islice
import operator as op
from functools import reduce



# (utility) binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


# formula (21) in http://mathworld.wolfram.com/RiemannZetaFunction.html
# Global zeta function by Knopp and Hasse (s != 1)
def zeta(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * ncr(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


def calculate(i):
    global last
    accuracy = i//500 + 100
    _zeta = zeta((1/2)+(i/accuracy*1j))
    #  if _zeta == 0:
    #  if str(abs(_zeta))[:5] == '0.000':
    #  print(f'1/2 + ({i*1j/accuracy}) \t {_zeta}')
    #  print(i, _zeta)
    if i/accuracy > 131:
        print(accuracy, i/accuracy, _zeta, last)
    if abs(_zeta) < 10e-3:
        if not last:
            print('------------------------------')
            print(accuracy, i/accuracy, _zeta, last)
            print('------------------------------')
        last = True
    else:
        last = False




if __name__=='__main__':
    start = time()
    ...
    i = 0
    last = False
    while True:
        calculate(i)
        i += 1
    print(f'--- {time()-start} seconds ---')


