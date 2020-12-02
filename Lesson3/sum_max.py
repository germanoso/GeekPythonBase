'''
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(a, b, c):
    num_list = [a, b, c]
    # min_num = min(num_list)
    num_list.remove(min(num_list))
    return sum(num_list)

num_1 = 10
num_2 = 20
num_3 = 30
print(f'{num_1} {num_2} {num_3} sum of 2 max numbers is'
      f' {my_func(num_1, num_2, num_3)}')