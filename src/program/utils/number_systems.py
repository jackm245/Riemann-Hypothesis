from math import sin, cos, atan2, sqrt, exp, log
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
        +
        -
        *
        /
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
    def __init__(self, *args, rect=True):
        super().__init__([*args])
        self.args = args
        self.rect = rect
        if not self.rect:
            # for polar coordinates
            r = float(self.args[0])
            phi = float(self.args[1])
            self.__real = r * cos(phi)
            self.__imag = r * sin(phi)
        else:
            if isinstance(args[0], Complex):
                # if already in Complex form
                self.__real = args[0].get_real()
                self.__imag = args[0].get_imag()
            elif isinstance(args[0], complex):
                # if already in python complex form
                self.__real = args[0].real
                self.__imag = args[0].imag
            else:
                # for rect coordinates
                self.__real = float(self.args[0])
                self.__imag = float(self.args[1]) if len(self.args) > 1 else 0


    # make the number complex, if possible
    def __correct_type(self, number):
        """Polymorphsim"""
        #  print(f'correcting type on {number}, type {type(number)}')
        if isinstance(number, Complex):
            return number
        elif isinstance(number, (float,int)):
            number = Complex(number)
        elif not (hasattr(number, 'real') and hasattr(number, 'imag')):
            raise TypeError('Number must have a real and imagiary part')
        else:
            raise TypeError(f'Number of type {type(number)} not of correct format')
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
        """
        self ** other
        self^other = \rho^c e^{-d\theta}(\cos(d\ln\rho + c\theta)+i \sin(d\ln\rho + c\theta))
        where self = a+bi, other=c+di, \theta=\arctan(\frac{b}{a}), \rho=sqrt{a^2 + b^2}
        """
        rho, theta = self.polar()
        c = Complex(other).get_real()
        d = Complex(other).get_imag()
        mod = rho ** c * exp(-d * theta)
        arg = d * log(rho) + c * theta
        return Complex(mod, arg, rect=False)
        #  return r**other*(cos(other*phi)+sin(other*phi)*1j)


    def __rpow__(self, other):
        """ other ** self """
        return self.__pow__(other)


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
            return '(%s+%si)' % (self.__real, self.__imag)
        else:
            return '(%s-%si)' % (self.__real, abs(self.__imag))


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

    def conjugate(self):
        """ (a+b*1j).conjugate() returns (a-b*1j) """
        return Complex(self.__real, -self.__imag)


    def phase(self):
         """ self.phase() """
         return atan2(self.__imag, self.__real)


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

class Fraction:
    pass
"fraction class removed"
