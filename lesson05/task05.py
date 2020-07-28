"""
    5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open('task05.tmp', 'w', encoding='UTF-8') as file:
    glue = ''
    for _ in range(5):
        file.write(glue + str(random.randint(0, 10)))
        glue = ' '

with open('task05.tmp', 'r', encoding='UTF-8') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Содержимое файла:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")
