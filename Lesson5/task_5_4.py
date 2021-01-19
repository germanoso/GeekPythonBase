'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

read_file = 'files/task5_4_1.txt'
write_file = 'files/task5_4_2.txt'

dig_translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open(read_file, 'r', encoding='UTF8') as f:
    lines = f.readlines()
    new_lines = [f'{dig_translate[line.split(" — ")[0]]} - {line.split(" — ")[-1]}' for line in lines]
    print(new_lines)

with open(write_file, 'w', encoding='UTF8') as f:
    f.writelines(new_lines)