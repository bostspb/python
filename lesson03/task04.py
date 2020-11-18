"""
    4. Программа принимает действительное положительное число x и целое отрицательное число y.
    Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
    Подсказка: попробуйте решить задачу двумя способами.
    Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_abs(x):
    return x if x >= 0 else x * -1


def raising_to_power(x, y):
    result = x
    for i in range(my_abs(y) - 1):
        result *= x
    if y < 0:
        result = 1 / result
    return result


try:
    basis = int(input("x = "))
    degree = int(input("y = "))
    print(f"x ** y =  {raising_to_power(basis, degree)}")
except ValueError as e:
    print(e)