'''
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

file_new = 'files/task5_5.txt'
from random import randint

with open(file_new, 'w', encoding='UTF8') as f:
    list_rand = [f.write(f'{str(randint(1, 500))} ') for i in range(20)]

with open(file_new, 'r', encoding='UTF8') as f:
    print(f'Сумма всех чисел в файле "{file_new}" равна {sum(list(map(int, f.read().split())))}')