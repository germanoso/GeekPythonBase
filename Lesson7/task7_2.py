'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def fabric_total(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 42:
            self.__size = 42
        elif size > 68:
            self.__size = 68
        else:
            self.__size = size

    def fabric_total(self):
        return round(self.__size / 6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1:
            self.__height = 1
        elif height > 2.10:
            self.__height = 2.10
        else:
            self.__height = height

    def fabric_total(self):
        return round(self.__height * 2 + 0.3, 2)

m = Coat(30)
print(f'Для костюма размера {m.size} нужно {m.fabric_total()} м. ткани')

w = Suit(1.76)
print(f'Для пальто роста {w.height} нужно {w.fabric_total()} м. ткани')
