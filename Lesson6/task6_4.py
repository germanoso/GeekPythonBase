'''
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


Предпочел бы сделать класс Полицейский авто и там обьявлять это. Но, выполнил по заданию

в дочерних классах можно было не писать:
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
'''

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self_color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} едет')

    def stop(self):
        print(f'Автомобиль {self.name} стоит')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.speed} км/ч выше допустимой!')
        else:
            print(f'Скорость {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.speed} км/ч выше допустимой!')
        else:
            print(f'Скорость {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

car = PoliceCar(speed=0, color='красный', name='Ford')
car.go()
car.speed = 50
car.show_speed()
car.turn('лево')
car.speed = 70
car.show_speed()
car.speed = 40
car.show_speed()
car.speed = 0
car.show_speed()
car.stop()

# my_PoliceCar = PoliceCar(speed=90, color="красный", name="Mazda")
# my_PoliceCar.go()
# my_PoliceCar.turn("лево")
# my_PoliceCar.stop()
# if my_PoliceCar.is_police == True:
#     print(f'Это полицеский автомобиль и может ехать со скоростью {my_PoliceCar.speed}')
#
# my_WorkCar = WorkCar(speed=30, color='желтый', name='Catarpilar')
# print(f'{my_WorkCar.name}. Скорость {my_WorkCar.show_speed()} км/ч')
#
# my_TownCar = TownCar(speed=80, color="синий", name="Mersedes")
# print(my_TownCar.go())
# my_TownCar.turn("право")
# my_TownCar.stop()
# print(my_TownCar.is_police)


