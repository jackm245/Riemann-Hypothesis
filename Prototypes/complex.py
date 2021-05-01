class Complex(): 


    """ 
    Operations and arithmetic involving complex numbers
    Operations include:
        + -
        * /
        == !=
        abs
        repr
        str
    """


    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag


    # make the number complex, if possible
    def _correct_type(self, number):
        if isinstance(number, (float,int)):                                    
            number = Complex(number)
        elif not (hasattr(number, 'real') and hasattr(number, 'imag')):
            raise TypeError('number must have a real and imagiary part')
        return number


    # illegal operations for complex numbers 
    def _illegal(self, op):
        print(f'Unable to compute\noperation \"{op}\" illegal for complex numbers')


    def __abs__(self):
        """ |self| """
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


    def __eq__(self, other):
        """ self == other """
        other = self._correct_type(other)
        return self.real == other.real and self.imag == other.imag


    def __ne__(self,other):
        """ self != other """
        return not(self.__eq__(other))

    ### printing and display ###
    def __str__(self):
        """ str(self) """
        if self.imag >= 0:
            return '(%s + %sj)' % (self.real, self.imag)
        else:
            return '(%s - %sj)' % (self.real, abs(self.imag))


    def __repr__(self):
        """ repr(self) """
        return 'Complex(%s, %s)' % (self.real, self.imag)

    ### illegal operations ###    
    def __gt__(self, other):
        self._illegal('>')
    

    def __ge__(self, other):
        self._illegal('>=')
    

    def __lt__(self, other):
        self._illegal('<')
    

    def __le__(self, other):
        self._illegal('<=')

# print(Complex(3, -1) < Complex(2,-1))

