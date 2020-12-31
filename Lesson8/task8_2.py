'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class MyException(Exception):
    def __init__(self, text):
        self.text = text


print('Разделим 100 на введенное вами число')
divider = input('Введите делитель: ')
try:
    divider = int(divider)
    if divider == 0:
        raise MyException("На 0 делить нельзя!")
except ValueError:
    print("Вы ввели не число.")
except MyException as err:
    print(err)
else:
    print(f"Результат: {100 / divider:.2f}")