'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

FILE_NAME = 'files/task5_3.txt'

with open(FILE_NAME, 'r', encoding='UTF-8') as f:
    lines = f.readlines()

    second_names_with_low_salary = []
    average_salary = 0
    for line in lines:
        second_name, salary = line.split()
        salary = float(salary)
        average_salary += salary
        if salary < 20000:
            second_names_with_low_salary.append(second_name)

    print(f'Сотрудники с доходом меньше 20 000 руб.: {second_names_with_low_salary}')
    print(f'Средний величина дохода сотрудников: {round(average_salary / len(lines), 2)} руб.')