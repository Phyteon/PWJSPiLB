
class Complex:
    pi = 3.141592653589793238462
    import math

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        fil = "+"
        if self.imag < 0:
            fil = ""
        return str(self.real) + fil + str(self.imag) + "i"

    def __truediv__(self, other):
        coef = other.real**2 + other.imag**2
        return Complex((self.real*other.real+self.imag*other.imag)/coef, (self.imag*other.real-self.real*other.imag)/coef)

    def __mul__(self, other):
        return Complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)

    def conj(self):
        return Complex(self.real, -self.imag)

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def ang(self):
        if self.imag > 0:
            if self.real > 0:
                return self.math.atan(self.imag/self.real)
            elif self.real < 0:
                return self.math.atan(self.imag/abs(self.real)) + self.pi/2
            else:
                return self.pi/2
        elif self.imag < 0:
            if self.real < 0:
                return self.math.atan(abs(self.imag)/abs(self.real)) + self.pi
            elif self.real > 0:
                return self.math.atan(abs(self.imag)/self.real) + 1.5*self.pi
            else:
                return self.pi*1.5
        else:
            if self.real > 0:
                return 0
            else:
                return self.pi

    def ang2(self):
        if self.imag > 0:
            if self.real > 0:
                return self.math.atan(self.imag/self.real)*180/self.pi
            elif self.real < 0:
                return self.math.atan(self.imag/abs(self.real))*180/self.pi + 90
            else:
                return 90
        elif self.imag < 0:
            if self.real < 0:
                return self.math.atan(abs(self.imag)/abs(self.real))*180/self.pi + 180
            elif self.real > 0:
                return self.math.atan(abs(self.imag)/self.real)*180/self.pi + 270
            else:
                return 270
        else:
            if self.real > 0:
                return 0
            else:
                return 180
