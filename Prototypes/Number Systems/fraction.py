#=============================================================================#
#
#    File:   fraction.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Contains the class Fraction
#        Computes arithmetic operations involving fractions
#
#=============================================================================#


"""
operations
fractions divided by fractions
"""


import re


__all__ = ['Fraction']


class Fraction:
    # subclass of number class
    # subclass of complex class

    """
    Operations and arithmetic involving fractions
    Operations include:

    """


    def __init__(self, numerator, denominator=1):
        #FRACTIONS DIVIDED BY FRACTIONS. FRAC AS NUM AND DENOM
        if not(isinstance(numerator, (float, int, str)) or isinstance(denominator, (float, int, str))):
            raise ValueError(f'Fraction({numerator}, {denominator})\nData must be of type float, int, or str')
        elif isinstance(numerator, str):
            try:
                float(numerator)
            except ValueError as numerator_value_error:
                raise ValueError(f'{numerator_value_error}\nNumerator must be a number')
        elif isinstance(denominator, str):
            try:
                float(denominator)
            except ValueError as denominator_value_error:
                raise ValueError(f'{denominator_value_error}\nDenominator must be a number')
        
        # convert data types
        if isinstance(numerator, str):
            numerator = float(numerator)
            if numerator == int(numerator):
                numerator = int(numerator)
        if isinstance(denominator, str):
            denominator = float(denominator)
            if denominator == int(denominator):
                denominator = int(denominator)

        # where numerator and denominator are floats
        if denominator == 0:
            raise ZeroDivisionError(f'Fraction({numerator}, 0)')
       
        self.numerator = numerator
        self.denominator = denominator
        self._simplify_fraction()


    def _convert_to_decimal_fraction(self):
        # multiply by largest length
        numerator_decimals, denominator_decimals = 0, 0
        if self.numerator != int(self.numerator):
            numerator_decimals = len(re.search(r'(?<=.)\d+$', str(self.numerator))[0])
        if self.denominator != int(self.denominator):
            denominator_decimals = len(re.search(r'(?<=.)\d+$', str(self.denominator))[0])
        highest_decimal_places = max(numerator_decimals, denominator_decimals)
        self.numerator = int(self.numerator*10**highest_decimal_places)
        self.denominator = int(self.denominator*10**highest_decimal_places)


    def _get_greatest_common_divisor(self, num1, num2):
        if num2 == 0:
            return num1
        else:
            return self._get_greatest_common_divisor(num2, num1 % num2)


    def _simplify_fraction(self):
        # to a decimal fraction
        self._convert_to_decimal_fraction()

        # simplify down by dividing numerator and denominator by gcd
        greatest_common_divisor = self._get_greatest_common_divisor(abs(self.numerator), abs(self.denominator))
        self.numerator //= greatest_common_divisor
        self.denominator //= greatest_common_divisor

        #make denominator positive
        if self.denominator < 0:
            self.denominator = -self.denominator
            self.numerator = -self.numerator


    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'


print(Fraction(5.0, 1.0))
print(Fraction(2.5, 7.5))
print(Fraction(1.5, 3.111))
