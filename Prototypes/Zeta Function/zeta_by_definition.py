#=============================================================================#
#
#    File:   zeta_by_definition.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Computes the zeta function for Re(s) > 1
#        where \zeta(s)=\sum _{n=0}^{\infty }\frac{1}{n^s}
#
#=============================================================================#


# calculates zeta(s) for any complex number where Re(s) > 1
# where \zeta(s)=\sum _{n=0}^{\infty }\frac{1}{n^s}
def zeta(s: complex) -> complex:
    # validate that Re(s) > 1
    if not s.real > 1:
        raise ValueError('Real part of input must be greater than 1')
    TERMS = 1 * 10**6 # the number of terms that we wish to compute.
    result = 0
    # computes an approximation for the infinite sum
    for n in range(1, TERMS+1):
        result += 1/(n**s)
    # output the final result
    return result


for x in range(2,10):
    for y in range(2,10):
        print(zeta(x + y * 1j))
