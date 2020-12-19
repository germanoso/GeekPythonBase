# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month = int(input('Enter number of month: '))

# Создаем словарь

seasons = {1: 'зима', 2: 'зима', 12: 'зима',
           3: 'весна',4: 'весна', 5: 'весна',
           6: 'лето', 7: 'лето', 8: 'лето',
           9: 'осень', 10: 'осень', 11: 'осень'}

# Создаем списки

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if user_month in winter:
    print('This id Winter')
elif user_month in spring:
    print('This is Spring')
elif user_month in summer:
    print('This is Summer')
elif user_month in autumn:
    print('This is Autumn')
else:
    print('There are no such month')        # Печать решения через списки

print(f'Это {seasons.get(user_month)}')     # Печать решения через словарь