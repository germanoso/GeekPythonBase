'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, my_data):
        self.my_data = my_data

    @classmethod
    def data_int(cls, data_to_int):
        return cls.data_valid(list(map(int, data_to_int.split('-'))))

    @staticmethod
    def data_valid(my_data_list):
        if 0 < my_data_list[0] <31 and 0 < my_data_list[1] < 13 and 1900 < my_data_list[2] < 2100:
            return 'Дата введена правильно'
        else:
            return 'Дата введена не правильно'

my_date = Data('11-10-1969')
print(my_date.data_int(my_date.my_data))