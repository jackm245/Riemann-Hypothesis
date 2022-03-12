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
from math import exp, log
from number import Number

__all__ = ['Fraction']


class Fraction(Number):
    # subclass of number class
    # subclass of complex class

    """
    Operations and arithmetic involving fractions
    Operations include:

        Binary Operators
        +
        -
        *
        //
        /
        **

        Extended Assignments

        Unary Operators
        -
        +
        abs()

        Comparison Operators
        <
        <=
        ==
        !=
        >=
        >

        Type Conversion
        int()
        str()
        float()
        dump()
        repr()

        Miscellaneous
        __simplify_fraction()
        __get_reciprocal()
    """

    def __init__(self, numerator, denominator=1):
        super().__init__([numerator, denominator])
        self.__numerator = numerator
        self.__denominator = denominator
        self.__validate_input()
        self.__simplify_fraction()


    # makes sure that numerator and denominator are valid numbers
    # accepts different data types (int, float, str, Fraction)
    def __validate_input(self):
        if isinstance(self.__numerator, Fraction) and isinstance(self.__denominator, Fraction):
           self.__convert_to_signal_fraction(self.__numerator, self.__denominator)
        elif isinstance(self.__numerator, Fraction):
            self.__denominator *= self.__numerator.denominator
            self.__numerator = self.__numerator.numerator
        elif isinstance(self.__denominator, Fraction):
            self.__numerator *= self.__denominator.denominator
            self.__denominator = self.__denominator.numerator
        elif not(isinstance(self.__numerator, (float, int, str)) or isinstance(self.__denominator, (float, int, str))):
            raise ValueError(f'Fraction({self.__numerator}, {self.__denominator})\nData must be of type float, int, or str.\nNumerator of type \'{type(self.__numerator)}\'.\nDenominator of type \'{type(self.__denominator)}\'.')
        elif isinstance(self.__numerator, str):
            try:
                float(self.__numerator)
            except ValueError as numerator_value_error:
                raise ValueError(f'{numerator_value_error}\nNumerator must be a number, not \'{self.__numerator}\'').with_traceback(numerator_value_error.__traceback__)
        elif isinstance(self.__denominator, str):
            try:
                float(self.__denominator)
            except ValueError as denominator_value_error:
                raise ValueError(f'{denominator_value_error}\nDenominator must be a number, not \'{self.__denominator}\'').with_traceback(denominator_value_error.__traceback__)
        # convert data types
        if isinstance(self.__numerator, str):
            self.__numerator = float(self.__numerator)
            if self.__numerator == int(self.__numerator):
                self.__numerator = int(self.__numerator)
        if isinstance(self.__denominator, str):
            self.__denominator = float(self.__denominator)
            if self.__denominator == int(self.__denominator):
                self.__denominator = int(self.__denominator)
        if self.__denominator == 0:
            raise ZeroDivisionError(f'Fraction({self.__numerator}, 0)')


    # where a fraction may consist of a fraction on the numerator or denominator
    # simplify this into a single fraction
    def __convert_to_signal_fraction(self, num, denom):
        # \frac{\frac{a}{b}}{\frac{c}{d}}=\frac{a\cdot \:d}{b\cdot \:c}
        fraction = Fraction(num.numerator * denom.denominator, num.denominator * denom.numerator)
        self.__numerator = fraction.numerator
        self.__denominator = fraction.denominator


    # where numerator or denominator are decimals, covert the fraction into a decimal fraction
    def __convert_to_decimal_fraction(self):
        # multiply by largest length
        numerator_decimals, denominator_decimals = 0, 0
        if self.__numerator != int(self.__numerator):
            numerator_decimals = len(re.search(r'(?<=.)\d+$', str(self.__numerator))[0])
        if self.__denominator != int(self.__denominator):
            denominator_decimals = len(re.search(r'(?<=.)\d+$', str(self.__denominator))[0])
        highest_decimal_places = max(numerator_decimals, denominator_decimals)
        self.__numerator = int(self.__numerator*10**highest_decimal_places)
        self.__denominator = int(self.__denominator*10**highest_decimal_places)


    # find the greatest common divisor (highest common factor) between numbers num1 and num2
    def __get_greatest_common_divisor(self, num1, num2):
        # euclidean algorithm
        if num2 == 0:
            return num1
        else:
            return self.__get_greatest_common_divisor(num2, num1 % num2)


    # find the lowest common multiple between numbers num1 and num2
    def __get_lowest_common_multiple(self, num1, num2):
        # special case when num1 and num2 ignored as num2 cant be 0 for fractions
        # {\displaystyle \operatorname {lcm} (a,b)={\frac {|a\cdot b|}{\gcd(a,b)}}.}
        return (abs(num1 * num2)) / self.__get_greatest_common_divisor(num1, num2)


    def __simplify_fraction(self):
        # to a decimal fraction
        self.__convert_to_decimal_fraction()

        # simplify down by dividing numerator and denominator by gcd
        greatest_common_divisor = self.__get_greatest_common_divisor(abs(self.__numerator), abs(self.__denominator))
        self.__numerator //= greatest_common_divisor
        self.__denominator //= greatest_common_divisor

        #make denominator positive
        if self.__denominator < 0:
            self.__denominator = -self.__denominator
            self.__numerator = -self.__numerator


    def __get_reciprocal(self, fraction):
        fraction = self.__convert_to_fraction(fraction, 'reciprocal')
        if fraction.numerator != 0:
            return Fraction(fraction.denominator, fraction.numerator)
        else:
            raise ValueError('Unable to take reciprocal of Fraction(0, 1)')


    # convert variable other to type Fraction
    def __convert_to_fraction(self, other, operation):
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except ValueError as error:
                raise ValueError(f'{error}\nUnable to perform operation \'{operation}\' on numbers \'{self}\' and \'{other}\'').with_traceback(error.__traceback__)
        return other


    ### Binary Operators ###
    def __add__(self, other):
        """ self + other """
        other = self.__convert_to_fraction(other, 'addition')
        resulting_numerator = self.__numerator * self.__denominator + self.__denominator * self.__numerator
        resulting_denominator = self.__denominator * self.__denominator
        return (Fraction(resulting_numerator, resulting_denominator))


    def __radd__(self, other):
        """ other + self """
        return self.__add__(other)


    def __sub__(self, other):
        """ self - other """
        other = self.__convert_to_fraction(other, 'subtraction')
        resulting_numerator = self.__numerator * self.__denominator - self.__denominator * self.__numerator
        resulting_denominator = self.__denominator * self.__denominator
        return (Fraction(resulting_numerator, resulting_denominator))


    def __rsub__(self, other):
        """ other - self """
        return self.__sub__(other)


    def __mul__(self, other):
        """ self * other """
        other = self.__convert_to_fraction(other, 'multiplication')
        return Fraction(self.__numerator * self.__numerator, self.__denominator * self.__denominator)


    def __rmul__(self, other):
        """ other * self """
        return self.__mul__(other)


    def __floordiv__(self, other):
        """ self // other """
        other = self.__convert_to_fraction(other, 'floor division')
        return self.__truediv__(other).__int__()


    def __rfloordiv__(self, other):
        """ other // self """
        #return self.__get_reciprocal(self.__floordiv__(other)).__int__()
        return self.__rtruediv__(other).__int__()


    def __truediv__(self, other):
        """ self / other """
        other = self.__convert_to_fraction(other, 'true division')
        # \frac{a}{b}\div \frac{c}{d} \equiv \frac{a}{b}\cdot \frac{d}{c}
        #return other.__mul__(self.__get_reciprocal(self))
        return Fraction(self.__numerator * self.__denominator, self.__denominator * self.__numerator)


    def __rtruediv__(self, other):
        """ other / self """
        return self.__get_reciprocal(self.__truediv__(other))


    def __pow__(self, other):
        """ self ** other """
        other = self.__convert_to_fraction(other, 'power')
        # X = exp(log(n)/x)
        return Fraction(exp((self.__numerator*log(self))/self.__denominator))


    def __rpow__(self, other):
        """ other ** self """
        other = self.__convert_to_fraction(other, 'right power')
        return other.__pow__(self)


    ### Extended Assignments ###


    ### Unary Operators ###
    def __neg__(self):
        """ -self """
        return Fraction(-self.__numerator, self.__denominator)

    def __pos__(self):
        """ +self """
        return Fraction(+self.__numerator, self.__denominator)


    def __abs__(self):
        """ abs(self) """
        if self.__numerator < 0:
            self.__numerator = -self.__numerator
        return Fraction(self.__numerator, self.__denominator)


    ### Comparison Operators ###
    def __lt__(self, other):
        """ self < other """
        other = self.__convert_to_fraction(other, 'less than')
        lcm = self.__get_lowest_common_multiple(self.__denominator, self.__denominator)
        return self.__numerator * lcm < self.__numerator * lcm


    def __le__(self, other):
        """ self <= other """
        other = self.__convert_to_fraction(other, 'less than or equal to')
        lcm = self.__get_lowest_common_multiple(self.__denominator, self.__denominator)
        return self.__numerator * lcm <= self.__numerator * lcm


    def __eq__(self, other):
        """ self == other """
        other = self.__convert_to_fraction(other, 'equal to')
        lcm = self.__get_lowest_common_multiple(self.__denominator, self.__denominator)
        return self.__numerator * lcm == self.__numerator * lcm


    def __ne__(self, other):
        """ self != other """
        other = self.__convert_to_fraction(other, 'not equal to')
        lcm = self.__get_lowest_common_multiple(self.__denominator, self.__denominator)
        return self.__numerator * lcm != self.__numerator * lcm


    def __gt__(self, other):
        """ self > other """
        other = self.__convert_to_fraction(other, 'greater than')
        lcm = self.__get_lowest_common_multiple(self.__denominator, self.__denominator)
        return self.__numerator * lcm > self.__numerator * lcm


    def __ge__(self, other):
        """ self >= other """
        other = self.__convert_to_fraction(other, 'greater than or equal to')
        lcm = self.__get_lowest_common_multiple(self.__denominator, self.__denominator)
        return self.__numerator * lcm >= self.__numerator * lcm


    ### Type Conversion ###
    def __int__(self):
        """ int(self) """
        return self.__numerator // self.__denominator


    def __float__(self):
        """ float(self) """
        return float(self.__numerator / self.__denominator)


    def dump(self):
        return self.__dict__


    def __str__(self):
        """ str(self) """
        return f'{self.__numerator}/{self.__denominator}'


    def __repr__(self):
        """ repr(self) """
        return f'Fraction({self.__numerator}, {self.__denominator})'


# print(int(Fraction(3, 4)))
print(Fraction(1, 2)**2)
print(Fraction(6, 5) ** Fraction(2, 3))
print(float(2**Fraction(1, 2)))
