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
        # euclidean algorithm
        if num2 == 0:
            return num1
        else:
            return self._get_greatest_common_divisor(num2, num1 % num2)

    
    def _get_lowest_common_multiple(self, num1, num2):
        # special case when num1 and num2 ignored as num2 cant be 0 for fractions
        # {\displaystyle \operatorname {lcm} (a,b)={\frac {|a\cdot b|}{\gcd(a,b)}}.}
        return (abs(num1 * num2)) / self._get_greatest_common_divisor(num1, num2)
     

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

    
    def _get_reciprocal(self):
        return Fraction(self.denominator, self.numerator)


    def __add__(self, other):
        """ self + other """
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except ValueError as error:
                raise ValueError(f'{error}\nUnable to add numbers {self} and {other}')
        resulting_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        resulting_denominator = self.denominator * other.denominator
        return (Fraction(resulting_numerator, resulting_denominator))


    def __radd__(self, other):
        """ other + self """
        return self.__add__(other)


    def __sub__(self, other):
        """ self - other """
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except ValueError as error:
                raise ValueError(f'{error}\nUnable to subtract numbers {self} and {other}')
        resulting_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        resulting_denominator = self.denominator * other.denominator
        return (Fraction(resulting_numerator, resulting_denominator))


    def __rsub__(self, other):
        """ other - self """
        return self.__sub__(other)


    def __mul__(self, other):
        """ other * self """
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)


    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'


print(Fraction(1, 2) - 'x')
