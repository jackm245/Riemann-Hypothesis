from itertools import count, islice


# binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


# Global zeta function
def zeta(s, t=100):
    if s == 1: return float('inf')
    sum1 = 0
    for n in range(t):
        sum2 = 0
        for k in range(n+1):
            term1 = (-1)**k * binom(n, k) * (k+1)** (-s)
            sum2 += term1
        term2 = (1/(2**(n+1)))
        sum1 += sum2 * term2
    term1 = (1/(1-2**(1-s)))
    return sum1 * term1


c_num = 100+100j
print(test_zeta(c_num))
print(zeta(c_num))
