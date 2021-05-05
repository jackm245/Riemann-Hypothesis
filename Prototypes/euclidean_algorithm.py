#=============================================================================#
#
#    File:   euclidean_algorothm.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Recursive function for the euclidean algorithm
#        Computes the greatest common divisor (highest common factor) of two numbers a and b
#
#=============================================================================#



def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

