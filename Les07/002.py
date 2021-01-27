"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def fabric_size(self):
        pass


class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = int(V)

    @property
    def fabric_size(self):
        return round(self.V/6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = int(H)

    @property
    def fabric_size(self):
        return round(2 * self.H + 0.3, 2)


c = Coat('Польтишко', 40)
print(c.name)
print(c.V)
print(c.fabric_size)

s = Suit('Костюмчик', 40)
print(s.name)
print(s.H)
print(s.fabric_size)

print(c.fabric_size+s.fabric_size)