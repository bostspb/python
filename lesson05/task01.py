"""
    1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка.
"""

input_not_empty = True
file = open('task01.tmp', 'w', encoding='UTF-8')
while input_not_empty:
    line = input()
    if line == '':
        input_not_empty = False
    else:
        file.write(line + '\n')
file.close()
