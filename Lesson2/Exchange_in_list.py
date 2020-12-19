# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

new_list = []
user_list = []
ending = str(0)
user_in = str()

while True:
    user_in = input("Input what you want. For end - 0: ")   #Вводим данные по одному. Чтобы завершить, 0
    if user_in == ending:
        break
    user_list.append(user_in)

print('You are entering: ', user_list)

for pos in range(len(user_list)):
    if pos % 2 == 0:
        new_list.insert(pos + 1, user_list[pos])
    else:
        new_list.insert(pos - 1, user_list[pos])


print('The new list is:  ', new_list)
