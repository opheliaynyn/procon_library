#---------------------------------------------------------------
#BIT(Bynary Indeked Tree, Fenwick Tree)
class BIT(object):
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (self.size + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def __str__(self):
        return str(self.bit)
