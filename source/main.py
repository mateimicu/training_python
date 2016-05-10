#!/usr/bin/env python3.4


class Numar():
    def __init__(self, nr = 0):
        if type(nr) == type(5):
            self.nr = nr
        else :
            self.nr = nr.nr

    def __add__(self, alt_numar):
        return Numar(self.nr + Numar(alt_numar).nr)

    def __radd__(self, alt_numar):
        return self + alt_numar

    def __str__(self):
        return str(self.nr)

    def __len__(self):
        return len(str(self))

    def __mul__(self, alt_numar):
        return Numar(self.nr * Numar(alt_numar).nr)

    def __sub__(self, alt_numar):
        return Numar(self.nr - Numar(alt_numar).nr)

    def __neg__(self):
        return Numar(-self.nr)

    def __rsub__(self, alt_numar):
        # return Numar(alt_numar) - self
        return -self + alt_numar

n1 = Numar(2)
n4 = 10 - n1

print("Rezultat : ", n4)
