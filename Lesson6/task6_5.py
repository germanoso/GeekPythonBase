'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print(f'Рисуем')

class Pen(Stationery):

    def draw(self):
        print(f'{self.title} рисует тонкие линии')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует красивые линии')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} рисует яркие линии')

my_pen = Pen('Ручка')
my_pen.draw()

my_pencil = Pencil('Карандаш')
my_pencil.draw()

my_handle = Handle('Маркер')
my_handle.draw()