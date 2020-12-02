'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def check_symb(numbers, symb):
    numbers = numbers.split(' ')
    if symb in numbers:
        flag = False
        numbers.remove(symb)
    else:
        flag = True
    return (numbers, flag)


numbers = []
symb = '#'
flag = True
num_sum = 0

while flag == True:
    numbers = input(f'Введите числа через пробел, для завершения нажмите {symb} ')
    num_list, flag = check_symb(numbers, symb)
    num_int = map(int, num_list)
    num_sum += sum(num_int)
    print(num_sum)

print('FINISH!!!')