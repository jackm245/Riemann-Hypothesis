#=============================================================================#
#
#    File:   complex.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Contains the class Complex
#        Computes arithmetic operations involving complex numbers
#
#=============================================================================#

## in same cases it says that operations are illegal or not implemented
## but havent tried to convert for int first
## should work e.g for Complex(4, 0) < Complex(5, 0)

from math import sin, cos, atan, sqrt
from number import Number

# __all__ = ['Complex']

class Complex(Number):
    # subclass of number class

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



print(Complex(5, 2)**3)
help(Complex.__add__)
