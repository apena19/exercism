from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self._reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        c = Rational((self.numer * other.denom + other.numer * self.denom), (self.denom * other.denom))
        return c

    def __sub__(self, other):
        c = Rational((self.numer * other.denom - other.numer * self.denom), (self.denom * other.denom))
        return c

    def __mul__(self, other):
        c = Rational((self.numer * other.numer), (self.denom * other.denom))
        return c

    def __truediv__(self, other):
        c = Rational((self.numer * other.denom), (self.denom * other.numer))
        return c

    def __abs__(self):
        c = Rational(abs(self.numer), abs(self.denom))
        return c

    def __pow__(self, power):
        c = Rational(self.numer ** power, self.denom ** power)
        return c

    def __rpow__(self, base):
        return base**(self.numer/self.denom)

    def _reduce(self):
        div = gcd(self.numer, self.denom)
        self.numer = self.numer//div
        self.denom = self.denom//div
        if self.denom < 0:
            self.numer = -self.numer
            self.denom = -self.denom
        return self
