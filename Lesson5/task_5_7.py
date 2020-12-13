'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json

file_in = 'files/task5_7.txt'
file_out = 'files/task5_7.json'

with open(file_in, 'r', encoding='UTF-8') as f:
    sum_profit = 0
    res = {}
    lines = f.readlines()
    for line in lines:
        name, form, income, outcome = line.split()
        profit = float(income) - float(outcome)
        res[name] = profit
        if profit > 0:
            sum_profit += profit

res['Average profit'] = round(sum_profit / len(lines), 2)
print(res)

with open(file_out, 'w', encoding='UTF-8') as f:
    json.dump(res, f)