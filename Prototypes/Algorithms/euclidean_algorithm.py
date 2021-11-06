#=============================================================================#
#
#    File:   euclidean_algorithm.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Recursive function for the euclidean algorithm
#        Computes the greatest common divisor (highest common factor) of two numbers a and b
#
#=============================================================================#


# function to find the greatest common divisor of two integers
def gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

