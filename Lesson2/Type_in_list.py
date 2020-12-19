# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать # функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

user_list = [18, 137.8, 0b10001, 0o21, 0x11, 'Some string', True, {'name': 'Some name', 'surname': 'Some surname', 'age': 35}, (35, 43, 55)]
count = 0
for el in user_list:
    print(f'Element number {count} consist "{user_list[count]}" is {type(user_list[count])}')
    count += 1