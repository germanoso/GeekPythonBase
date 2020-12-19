'''
6. Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
'''

def cap(text):
    new_text = chr(ord(text[:1]) - 32) + text[1:]
    return new_text


text_list = ['love', 'pain', 'flowers', 'компьютер']
for text in text_list:
    print(f'{text} --> {cap(text)}')