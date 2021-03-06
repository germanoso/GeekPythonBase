# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# all_goods = []
# item = []
# count_of_goods = 2
# for product_index in range(count_of_goods):
#     name = input('Enter name: ')
#     price = input('Enter price: ')
#     quantity = int(input('Enter quantity: '))
#     unit = input('Enter units: ')
#     product = {'название': name, 'цена': price, 'количество': quantity, 'eд': unit}
#     item.append(product_index + 1)
#     item.append(product)
#     item_in_pos = tuple(item)
#     all_goods.append(item_in_pos)
#
# print(all_goods)

all_goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
             (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
             (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]


num_items = 4
count_of_goods = len(all_goods)
i = 0
value = []
names = []
items = []

for num, val in all_goods:
    name = list(val.keys())
    values = list(val.values())
    value.append(values)

for i in range(num_items):
    print(f'"{name[i]}": ', end='')
    items.clear()
    for n in range(count_of_goods):
        items.append(value[n][i])
    print(items)
