'''
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
def printdates(nm, sn, yb, city, em, ph):
    print(f'{nm} {sn} was born on {yb}, live in {city}. email:{em}, phone nr {ph}')

name = 'Samanta'
surname = 'Smith'
year_birth = 1999
city = 'Paris'
email = 'samanta@yahoo.com'
phone = '325-25-78'

printdates(name, surname, year_birth, city, email, phone)