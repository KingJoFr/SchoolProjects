class Rational:
    """Rational number reduced to lowest terms.
    Allow all the standard operations producing another Rational.
    Rational operands may be mixed with an int to produce another Rational,
    but operations with (potentially inexact) floats produce a float.
    A Rational may be explicitly created from int numerator and denominator
    values or from a fraction string or an int or a Rational."""
    @staticmethod
    def gcd(a, b): # note no self parameter for static method
        """Return the greatest common divisor of the pair (a,b)"""
        m, n = abs(a), abs(b)
        while n != 0:  # Euclidean algorithm
            m, n = n, m % n
        return m

    def __init__(self, numerator, denominator = 1):
        """Initializes a new Rational"""
        if denominator != 0:
            divisor     = self.gcd(numerator, denominator)      # get the GCD
            if denominator < 0:                          
                divisor = -divisor                              # denominator > 0  when reduced
                self._num   = numerator // divisor             
                self._den   = denominator // divisor   
        else:
            # Problem
            raise ValueError("It is not possible to construct a rational number with a denominator of 0")

    def __str__(self):
        if self._den == 1:
            return f"{self._num} / {self._den}"
        else:
            return f"{self._num}" 

    def __add__(self, frac2):
        """return self + frac2 as a new rational"""
        frac1 = Rational(self._num, self._den)
        if isinstance(frac2, int):
            frac2 = Rational(frac2)
        elif not isinstance(frac2,Rational):
            return NotImplemented
        return Rational(frac1._num * frac2._den + frac1._den * frac2._num, frac1._den * frac2._den)


    def __sub__(self, frac2):
        """return self - frac2 as a new rational"""
        frac1 = Rational(self._num, self._den)
        if isinstance(frac2, int):
            frac2 = Rational(frac2)
        elif not isinstance(frac2,Rational):
            return NotImplemented
        return Rational(frac1._num * frac2._den - frac1._den * frac2._num, frac1._den * frac2._den)

    def __mul__(self, frac2):
        """return self - frac2 as a new rational"""
        frac1 = Rational(self._num, self._den)
        if isinstance(frac2, int):
            frac2 = Rational(frac2)
        elif not isinstance(frac2,Rational):
            return NotImplemented
        return Rational(frac1._num * frac2._num, frac1._den * frac2._den)

    def __div__(self, frac2):
        """return self - frac2 as a new rational"""
        frac1 = Rational(self._num, self._den)
        if isinstance(frac2, int):
            frac2 = Rational(frac2)
        elif not isinstance(frac2,Rational):
            return NotImplemented
        return Rational(frac1._num * frac2._num, frac1._den * frac2._den)
        
    def __neg__(self):
        return Rational(-self._num, self._den)
    def __float__(self):
        return self._num / self._den

a = Rational(-2,3)
b = Rational(1,2)
c = Rational(4,2)
d = 1 + a
e = a + -b
f = a - b


print(a," ",b," ",c)
