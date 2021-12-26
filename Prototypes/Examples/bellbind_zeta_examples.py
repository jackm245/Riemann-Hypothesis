# Programming for Calc Riemann Zeta function

from itertools import count, islice


# Basic definition of zeta func
# zeta(s) = sum(1/n^s)
# (Re(s) > 1)
def zeta1(s, t=10000):
    term = (1 / (n ** s) for n in count(1))
    return sum(islice(term, t))


print(zeta1(2)) # => 1.6449...
print((zeta1(2) * 6) ** 0.5) # => PI = 3.1415...
#print(zeta1(0.5+14.134725142j)) # invalid


# formula (20) in http://mathworld.wolfram.com/RiemannZetaFunction.html
#
#   sum((-1)^n/n^s) + sum(1/n^2) = 2 * sum(1/n^s, n=2,4,6,...)
#                                = 2 * sum(1/(2*n)^s)
#                                = 2 * 2^-s * sum(1/n^s)
#
#   sum((-1)^n/n^s) + zeta(s) = 2^(1-s) * zeta(s)
#
#   zeta(s) = 1/(1 - 2^(1-s)) * sum((-1^(n-1)) / n^s)
#   (Re(s) > 0 and s != 1)
def zeta2(s, t=10000):
    if s == 1: return float("inf")
    #term = ((-1)**(n - 1) / (n ** s) for n in count(1))
    #return sum(islice(term, t)) / (1 - 2**(1 - s))
    term = ((-1) ** n * n ** -s for n in count(1))
    return sum(islice(term, t)) / (2 ** (1 - s) -  1)


print(zeta2(2))
print((zeta2(2) * 6) ** 0.5)
print(abs(zeta2(0.5+14.134725142j))) # => 0
print(abs(zeta2(0.5-14.134725142j))) # => 0
#print(zeta2(0)) # invalid


# (utility) binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


# formula (21) in http://mathworld.wolfram.com/RiemannZetaFunction.html
# Global zeta function by Knopp and Hasse (s != 1)
def zeta3(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


print(zeta3(2))
print((zeta3(2) * 6) ** 0.5)
print(abs(zeta3(0.5+14.134725142j))) # => 0
print(abs(zeta3(0.5-14.134725142j))) # => 0
print(zeta3(1)) # => inf
print(zeta3(0)) # => -1/2
print(zeta3(-1)) # => -1/12 = 0.08333...
print(zeta3(-2)) # => 0
print(zeta3(100+100j))
