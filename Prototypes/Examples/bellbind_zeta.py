from itertools import count, islice


# (utility) binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


# formula (21) in http://mathworld.wolfram.com/RiemannZetaFunction.html
# Global zeta function by Knopp and Hasse (s != 1)
def zeta(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


def test_zeta(s, t=100):
    if s == 1: return float('inf')
    term1 = (1/(1-2**(1-s)))
    sum1 = 0
    for n in range(t):
        sum2 = 0
        term2 = (1/(2**(n+1)))
        for k in range(n+1):
            term3 = (-1)**k * binom(n, k) * (k+1)** (-s)
            sum2 += term3
        sum1 += sum2 * term2
    return sum1 * term1


c_num = 100+100j
print(test_zeta(c_num))
print(zeta(c_num))
