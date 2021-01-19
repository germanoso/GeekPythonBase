

import time
from itertools import cycle

class TrafficLight:
    __color = 'red'
    __counter = 0
    __stop = 20     #устанавливаем 20 циклов

    def running(self):
        for el in cycle([('red', 7), ('yellow', 2), ('green', 4)]):
            self.__color = el[0]
            print(self.__color)
            time.sleep(el[1])
            self.__counter += 1
            if self.__counter == self.__stop:
                break

a = TrafficLight()
a.running()