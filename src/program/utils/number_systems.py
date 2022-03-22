from math import sin, cos, atan, sqrt, exp, log
import re


class Number:

    def __init__(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def __str__(self):
        print(self.__number)


class Complex(Number):

    """
    Operations and arithmetic involving complex numbers
    Operations include:
        + -
        * /
        **
        == !=
        abs
        str
        repr
        conjugate
        phase
        dump
        polar
        rect
    """


    # initialisation using *args
    def __init__(self, *args):
        super().__init__([*args])
        # check if defined as polar coordinates
        if len(args) == 3 and args[2] == True:
            r = args[0]
            phi = args[1]
            self.__real = r * cos(phi)
            self.__imag = r * sin(phi)
        # for rect coordinates
        else:
            self.__real = args[0]
            self.__imag = args[1] if len(args) > 1 else 0


    # initialisation using parameters
    # problem is with parameter names
    """
    def __init__(self, real, imag=0, rect=True):
        # check if defined as polar coordinates
        if not rect:
            self.__real = real * cos(imag)
            self.__imag = real * sin(imag)
        # for rect coordinates
        else:
            self.__real = real
            self.__imag = imag
    """


    # make the number complex, if possible
    def __correct_type(self, number):
        if isinstance(number, (float,int)):
            number = Complex(number)
        elif not (hasattr(number, 'real') and hasattr(number, 'imag')):
            raise TypeError('number must have a real and imagiary part')
        return number


    # illegal operations for complex numbers
    def __illegal(self, op):
        print(f'Unable to compute \"{op}\"\nThis operation is illegal for complex numbers')


    ### Arithmetic Operations ###
    def __abs__(self):
        """ abs(self) """
        return sqrt(self.__real**2 + self.__imag**2)


    def __add__(self, other):
        """ self + other """
        other = self.__correct_type(other)
        return Complex(self.__real + other.__real, self.__imag + other.__imag)


    def __radd__(self,other):
        """ other + self """
        return self.__add__(other)


    def __sub__(self, other):
        """ self - other """
        other = self.__correct_type(other)
        return Complex(self.__real - other.__real, self.__imag - other.__imag)


    def __rsub__(self, other):
        """ other - self """
        return self.__sub__(other)


    def __mul__(self, other):
        """ self * other """
        other = self.__correct_type(other)
        # (ac-bd) + (ad+bc)i
        return Complex(self.__real*other.__real - self.__imag*other.__imag, self.__real*other.__imag + self.__imag*other.__real)


    def __rmul__(self, other):
        """ other - self """
        return self.__mul__(other)


    def __truediv__(self, other):
        """ self / other """
        other = self.__correct_type(other)
        r = float(other.__real**2 + other.__imag**2)
        return Complex((self.__real*other.__real+self.__imag*other.__imag)/r, (self.__imag*other.__real-self.__real*other.__imag)/r)


    def __rtruediv__(self, other):
        """ other / self """
        return self.__truediv__(other)


    def __pow__(self, other):
        """ self ** other """
        r, phi = self.polar()
        return r**other*(cos(other*phi)+sin(other*phi)*1j)


    def __rpow__(self, other):
        """ other ** self """
        raise NotImplementedError(f'Eror computing {other} ** {self}:\n\tnumber to a complex power is not defined')


    def __eq__(self, other):
        """ self == other """
        other = self.__correct_type(other)
        return self.__real == other.__real and self.__imag == other.__imag


    def __ne__(self,other):
        """ self != other """
        return not(self.__eq__(other))


    def __neg__(self):
        """ -self """
        return Complex(-self.__real, -self.__imag)


    def __pos__(self):
        """ +self """
        return Complex(+self.__real, +self.__imag)


    ### printing and display ###
    def __str__(self):
        """ str(self) """
        if self.__imag >= 0:
            return '(%s+%sj)' % (self.__real, self.__imag)
        else:
            return '(%s-%sj)' % (self.__real, abs(self.__imag))


    def __repr__(self):
        """ repr(self) """
        return 'Complex(%s, %s)' % (self.__real, self.__imag)


    ### illegal operations ###
    def __gt__(self, other):
        self.__illegal(f'{self} > {other}')


    def __ge__(self, other):
        self.__illegal(f'{self} >= {other}')


    def __lt__(self, other):
        self.__illegal(f'{self} < {other}')


    def __le__(self, other):
        self.__illegal(f'{self} <= {other}')


    ### Miscellaneous Functions ###

    # find the complex conjugate of a number
    def conjugate(self):
        """ (a+b*1j).conjugate() returns (a-b*1j) """
        return Complex(self.__real, -self.__imag)


    def phase(self):
         """ self.phase() """
         return atan(self.__imag /  self.__real)


    def dump(self):
        """ self.dump() """
        return self.__dict__


    def polar(self):
        """ self.polar() """
        return (self.__abs__(), self.phase())


    def rect(self):
        """ self.rect() """
        return (self.__real, self.__imag)

    def get_real(self):
        """ self.get_real()"""
        return self.__real

    def get_imag(self):
        """ self.get_imag()"""
        return self.__imag


class Fraction(Number):

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
