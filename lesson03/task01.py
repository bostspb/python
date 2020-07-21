"""
    1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return
    return result


try:
    n1 = float(input("a = "))
    n2 = float(input("b = "))
    print(f"a / b = {divide(n1, n2)}")
except ValueError:
    print("Incorrect input value")






