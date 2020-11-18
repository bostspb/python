"""
    4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
    Сформировать итоговый массив чисел, соответствующих требованию.
    Элементы вывести в порядке их следования в исходном списке.
    Для выполнения задания обязательно использовать генератор.

    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
    Результат: [23, 1, 3, 10, 4, 11]
"""


def my_counter(lst:list) -> dict:
    result = {}
    for key, value in enumerate(lst):
        if result.get(value) is None:
            result[value] = 1
        else:
            result[value] += 1
    return result


list_src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
counter = my_counter(list_src)
list_res = [x for x, n in counter.items() if n == 1]
print(list_res)
