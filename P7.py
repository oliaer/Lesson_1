print('Задача 1')

class Matrix:
    def __init__(self, m):
        self.m = m

    def __add__(self, other):
        list= []
        for i, j in zip(self.m, other.m):
            list.append([sum(z) for z in zip(i,j)])
        return list

    def __str__(self):
        for row in self.m:
           z = '\t'.join(map(str, row))
           print(z)
        return ''

m_1 = Matrix([[10, 20, 30], [11, 22, 33], [111, 222, 333]])
m_2 = Matrix([[40, 50, 60], [44, 55, 66], [444, 555, 666]])
print(m_1 + m_2)
print(m_1)


print('Задача 2')

from abc import ABC, abstractmethod

all = []

class AbstractClother(ABC):
    @abstractmethod
    def __init__(self, m):
         self.m = m

class Req:

    @property
    def requre(self):
        self.req = sum(all)
        return self.req


class Suit(AbstractClother):
    def __init__(self, v):
        self.v = v
        self.s_size = 2 * v + 0.3
        all.append(self.s_size)


class Coat(AbstractClother):
    def __init__(self, h):
        self.h = h
        self.s_size = h/6.5 + 0.5
        all.append(self.s_size)


suit_1 = Suit(3)
suit_2 = Suit(4)
coat_1 = Coat(3)
coat_2 = Coat(4)
print(suit_1.s_size)
a = Req()
print(round(a.requre))


print('Задача 3')

class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return f"Ячеек {self.count + other.count}"

    def __sub__(self, other):
        if self.count > other.count:
            return f"Ячеек {self.count - other.count}"
        else:
            return f"Не нужно вычитать {other.count} из {self.count}"

    def __mul__(self, other):
        return f"Ячеек {self.count * other.count}"

    def __truediv__(self, other):
        return f"Ячеек {self.count // other.count}"

    def make_order(self, p):
        row = self.count // p
        last = self.count % p
        return '\n'.join(['*' * p] * row + ['*' * last])


c1 = Cell(19)
c2 = Cell(220)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(5))
