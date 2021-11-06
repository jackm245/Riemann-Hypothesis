#=============================================================================#
#
#    File:   factorial.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Find the factorial of a number
#        x!
#
#=============================================================================#


import numpy as np


# x!\text{ ,  for }x \in  \mathbb{Z}
def factorial(x: int) -> int:
    return np.prod(np.arange(1, x+1))
