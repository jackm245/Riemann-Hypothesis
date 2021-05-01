class Complex(): 

    """ 
    Operations involving complex numbers
    Operations include:
        + / -
        *
        abs
        str
    """

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    # make the number complex, if possible
    def correct_type(self, number):
        if isinstance(number, (float,int)):                                    
            number = Complex(number)
        elif not (hasattr(number, 'real') and hasattr(number, 'imag')):
            raise TypeError('number must have a real and imagiary part')
        return number


    def __abs__(self):
        """ |self| """
        return sqrt(self.real**2 + self.imag**2)


    def __add__(self, other):
        """ self + other """    
        other = self.correct_type(other)
        return Complex(self.real + other.real, self.imag + other.imag)


    def __radd__(self,other):
        """ other + self """
        return self.__add__(other)


    def __sub__(self, other):
        """ self - other """
        other = self.correct_type(other)
        return Complex(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        """ other - self """
        return self.__sub__(other)

    def __mul__(self, other):
        """ self * other """
        other = self.correct_type(other)
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)
        # (ac-bd) + (ad+bc)i

    def __rmul__(self, other):
        """ other - self """
        return self.__mul__(other)

    def __str__(self):
        """ str(self) """
        return '(%s + %sj)' % (self.real, self.imag)

