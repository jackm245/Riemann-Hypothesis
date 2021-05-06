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


import re


__all__ = ['Fraction']


class Fraction:
    # subclass of number class
    # subclass of complex class

    """
    Operations and arithmetic involving fractions
    Operations include:
        Simplification of fractions
        abs ()
        + -
        * /
        int(), str(), repr()
        _get_reciprocal()
    """


    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self._validate_input()

    
    # makes sure that numerator and denominator are valid numbers
    # accepts different data types (int, float, str, Fraction)
    def _validate_input(self):
        if isinstance(self.numerator, Fraction) and isinstance(self.denominator, Fraction):
           self._convert_to_single_fraction(self.numerator, self.denominator)
        elif isinstance(self.numerator, Fraction):
            self.denominator *= self.numerator.denominator
            self.numerator = self.numerator.numerator
        elif isinstance(self.denominator, Fraction):
            self.numerator *= self.denominator.denominator
            self.denominator = self.denominator.numerator
        elif not(isinstance(self.numerator, (float, int, str)) or isinstance(self.denominator, (float, int, str))):
            raise ValueError(f'Fraction({self.numerator}, {self.denominator})\nData must be of type float, int, or str.\nNumerator of type \'{type(self.numerator)}\'.\nDenominator of type \'{type(self.denominator)}\'.')
        elif isinstance(self.numerator, str):
            try:
                float(self.numerator)
            except ValueError as numerator_value_error:
                raise ValueError(f'{numerator_value_error}\nNumerator must be a number, not \'{self.numerator}\'').with_traceback(numerator_value_error.__traceback__)
        elif isinstance(self.denominator, str):
            try:
                float(self.denominator)
            except ValueError as denominator_value_error:
                raise ValueError(f'{denominator_value_error}\nDenominator must be a number, not \'{self.denominator}\'').with_traceback(denominator_value_error.__traceback__)
        # convert data types
        if isinstance(self.numerator, str):
            self.numerator = float(self.numerator)
            if self.numerator == int(self.numerator):
                self.numerator = int(self.numerator)
        if isinstance(self.denominator, str):
            self.denominator = float(self.denominator)
            if self.denominator == int(self.denominator):
                self.denominator = int(self.denominator)
        if self.denominator == 0:
            raise ZeroDivisionError(f'Fraction({self.numerator}, 0)')
        self._simplify_fraction()

    
    # where a fraction may consist of a fraction on the numerator or denominator
    # simplify this into a single fraction
    def _convert_to_single_fraction(self, num, denom):
        # \frac{\frac{a}{b}}{\frac{c}{d}}=\frac{a\cdot \:d}{b\cdot \:c}
        fraction = Fraction(num.numerator * denom.denominator, num.denominator * denom.numerator)
        self.numerator = fraction.numerator
        self.denominator = fraction.denominator


    # where numerator or denominator are decimals, covert the fraction into a decimal fraction
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


    # find the greatest common divisor (highest common factor) between numbers num1 and num2
    def _get_greatest_common_divisor(self, num1, num2):
        # euclidean algorithm
        if num2 == 0:
            return num1
        else:
            return self._get_greatest_common_divisor(num2, num1 % num2)


    # find the lowest common multiple between numbers num1 and num2
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

    
    def _get_reciprocal(self, fraction):
        fraction = self._convert_to_fraction(fraction, 'reciprocal')
        return Fraction(fraction.denominator, fraction.numerator)


    # convert variable other to type Fraction
    def _convert_to_fraction(self, other, operation):
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except ValueError as error:
                raise ValueError(f'{error}\nUnable to perform operation \'{operation}\' on numbers \'{self}\' and \'{other}\'').with_traceback(error.__traceback__)
        return other


    def __abs__(self):
        """ abs(self) """
        if self.numerator < 0:
            self.numerator = -self.numerator
        return Fraction(self.numerator, self.denominator)


    def __add__(self, other):
        """ self + other """
        other = self._convert_to_fraction(other, 'addition')
        resulting_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        resulting_denominator = self.denominator * other.denominator
        return (Fraction(resulting_numerator, resulting_denominator))


    def __radd__(self, other):
        """ other + self """
        return self.__add__(other)


    def __sub__(self, other):
        """ self - other """
        other = self._convert_to_fraction(other, 'subtraction')
        resulting_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        resulting_denominator = self.denominator * other.denominator
        return (Fraction(resulting_numerator, resulting_denominator))


    def __rsub__(self, other):
        """ other - self """
        return self.__sub__(other)


    def __mul__(self, other):
        """ self * other """
        other = self._convert_to_fraction(other, 'multiplication')
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)


    def __rmul__(self, other):
        """ other * self """
        return self.__mul__(other)


    def __truediv__(self, other):
        """ self / other """
        other = self._convert_to_fraction(other, 'true division')
        # \frac{a}{b}\div \frac{c}{d} \equiv \frac{a}{b}\cdot \frac{d}{c}
        return self.__mul__(self._get_reciprocal(other))

    
    def __rtruediv__(self, other):
        """ other / self """
        return self._get_reciprocal(self.__truediv__(other))


    def __str__(self):
        """ str(self) """
        return f'{self.numerator}/{self.denominator}'


    def __repr__(self):
        """ repr(self) """
        return f'Fraction({self.numerator}, {self.denominator})'


    def __int__(self):
        """ int(self) """
        return self.numerator // self.denominator


print(Fraction(Fraction(2, 1), Fraction(3, 4)))
