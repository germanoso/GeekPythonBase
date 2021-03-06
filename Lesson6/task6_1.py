'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния
(красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.


!!!!!!  ДОПЛНИЛ еще одно решение этой же задачи в task6_1_1.py


Устанавливаем цикл на 20 повторений
Длительность зеленого устанавливаем 7 секунд
'''


import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        count = 0
        while count <= 20:
            for i in TrafficLight.__color:
                if i == 'Красный':
                    print(f'{i} 7 секунд')
                    time.sleep(7)
                elif i == 'Желтый':
                    print(f'{i} 2 секунды')
                    time.sleep(2)
                elif i == 'Зеленый':
                    print(f'{i} 7 секунд')
                    time.sleep(7)
        count += 1

a = TrafficLight()
a.running()