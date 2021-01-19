'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

'''
Добавил вывод должности
'''


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}, {self.position}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

# user_name = input('Введите имя > ')
# user_surname = input('Введите фамилию > ')
# user_position = input('Введите должность > ')
# user_wage = float(input('Введите сумму оклада > '))
# user_bonus = float(input('Введите сумму премии > '))

staff = Position(name='Иван', surname='Пупкин', position='проектировщик', income = {'wage': 83500, 'bonus': 17650})

# staff = Position(user_name, user_surname, user_position, user_wage, user_bonus)
print(f'Сотрудник {staff.get_full_name()} получил с учетом премии {staff.get_total_income():.2f} руб.')
