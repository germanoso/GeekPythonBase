'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''

class ComplexDigitStd:
    """Работа с комплексными числами с использованием стандартных функций Python"""
    def __init__(self, num1, num2):
        self.num = complex(num1, num2)

    def __add__(self, other):
        return f'{self.num + other.num}'

    def __mul__(self, other):
        return f'{self.num * other.num}'


class ComplexDigitMy:
    """Самостоятельная реализация работы с комплексными числами"""
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return f'Сумма ({self.num1}{self.num2:+}j) и ({other.num1}{other.num2:+}j) равна '  \
               f'({self.num1 + other.num1}{self.num2 + other.num2:+}j)'

    def __mul__(self, other):
        return f'Произведение ({self.num1}{self.num2:+}j) и ({other.num1}{other.num2:+}j)' \
               f' равно ({self.num1 * other.num1 + self.num2 * other.num2 * -1}' \
               f'{self.num1 * other.num2 + self.num2 * other.num1:+}j)'


n_1 = ComplexDigitStd(3, 1)
n_2 = ComplexDigitStd(2, -3)
print(n_1 + n_2)
print(n_1 * n_2)
n_1 = ComplexDigitMy(3, 1)
n_2 = ComplexDigitMy(2, -3)
print(n_1 + n_2)
print(n_1 * n_2)