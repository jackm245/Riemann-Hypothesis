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


# __all__ = ['Complex']

class Complex():
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
        # check if defined as polar coordinates
        if len(args) == 3 and args[2] == True:
            r = args[0]
            phi = args[1]
            self.real = r * cos(phi)
            self.imag = r * sin(phi)
        # for rect coordinates
        else:
            self.real = args[0]
            self.imag = args[1] if len(args) > 1 else 0


    # initialisation using parameters
    # problem is with parameter names
    """
    def __init__(self, real, imag=0, rect=True):
        # check if defined as polar coordinates
        if not rect:
            self.real = real * cos(imag)
            self.imag = real * sin(imag)
        # for rect coordinates
        else:
            self.real = real
            self.imag = imag
    """


    # make the number complex, if possible
    def _correct_type(self, number):
        if isinstance(number, (float,int)):
            number = Complex(number)
        elif not (hasattr(number, 'real') and hasattr(number, 'imag')):
            raise TypeError('number must have a real and imagiary part')
        return number


    # illegal operations for complex numbers
    def _illegal(self, op):
        print(f'Unable to compute \"{op}\"\nThis operation is illegal for complex numbers')


    ### Arithmetic Operations ###
    def __abs__(self):
        """ abs(self) """
        return sqrt(self.real**2 + self.imag**2)


    def __add__(self, other):
        """ self + other """
        other = self._correct_type(other)
        return Complex(self.real + other.real, self.imag + other.imag)


    def __radd__(self,other):
        """ other + self """
        return self.__add__(other)


    def __sub__(self, other):
        """ self - other """
        other = self._correct_type(other)
        return Complex(self.real - other.real, self.imag - other.imag)


    def __rsub__(self, other):
        """ other - self """
        return self.__sub__(other)


    def __mul__(self, other):
        """ self * other """
        other = self._correct_type(other)
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)
        # (ac-bd) + (ad+bc)i


    def __rmul__(self, other):
        """ other - self """
        return self.__mul__(other)


    def __truediv__(self, other):
        """ self / other """
        other = self._correct_type(other)
        r = float(other.real**2 + other.imag**2)
        return Complex((self.real*other.real+self.imag*other.imag)/r, (self.imag*other.real-self.real*other.imag)/r)


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
        other = self._correct_type(other)
        return self.real == other.real and self.imag == other.imag


    def __ne__(self,other):
        """ self != other """
        return not(self.__eq__(other))


    def __neg__(self):
        """ -self """
        return Complex(-self.real, -self.imag)


    def __pos__(self):
        """ +self """
        return Complex(+self.real, +self.imag)


    ### printing and display ###
    def __str__(self):
        """ str(self) """
        if self.imag >= 0:
            return '(%s+%sj)' % (self.real, self.imag)
        else:
            return '(%s-%sj)' % (self.real, abs(self.imag))


    def __repr__(self):
        """ repr(self) """
        return 'Complex(%s, %s)' % (self.real, self.imag)


    ### illegal operations ###
    def __gt__(self, other):
        self._illegal(f'{self} > {other}')


    def __ge__(self, other):
        self._illegal(f'{self} >= {other}')


    def __lt__(self, other):
        self._illegal(f'{self} < {other}')


    def __le__(self, other):
        self._illegal(f'{self} <= {other}')


    ### Miscellaneous Functions ###

    # find the complex conjugate of a number
    def conjugate(self):
        """ (a+b*1j).conjugate() returns (a-b*1j) """
        return Complex(self.real, -self.imag)


    def phase(self):
         """ phase(self) """
         return atan(self.imag /  self.real)


    def dump(self):
        """ dump(self) """
        return self.__dict__


    def polar(self):
        """ polar(self) """
        return (self.__abs__(), self.phase())


    def rect(self):
        """ rect(self) """
        return (self.real, self.imag)


print(5**Complex(5, 0))
print(Complex(5, 2)**3)
