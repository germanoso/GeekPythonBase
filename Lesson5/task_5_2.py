'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

i = 0
with open('files/task5_2.txt', 'r', encoding='UTF8') as my_f:
    for line in my_f:
        count_words = len(line.split())
        print(f'В строке "{line[:-1]}" - {count_words} слов')
        i += 1
    print(f'Всего {i} строк')
