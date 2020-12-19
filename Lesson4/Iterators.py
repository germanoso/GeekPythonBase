'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

from itertools import count, cycle

start_num = 9
end_num = 20
list_num = []
list_str = []
start_str = 'python'

for el in count(start_num):
    if el > end_num:
        break
    else:
        list_num.append(el)
print(f'Сгенерированный список от {start_num} до {end_num}: {list_num}')

i = 0
for str_el in cycle(start_str):
    if i > end_num:
        break
    else:
        list_str.append(str_el)
        i += 1
print(f'Сгенерированный список из строки "{start_str}": {list_str}')