# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_length = int(input("Введите размер списка: "))
list_original = []
list_mixed = []
for i in range(1, list_length + 1):
    item = input(f"Введите значение {i}-го элемента: ")
    list_original.append(item)
    if i % 2 == 0:
        list_mixed.append(item)
        list_mixed.append(list_original[i - 2])

if len(list_mixed) != list_length:
    list_mixed.append(list_original[list_length - 1])

print(f"Оригинальный список: {list_original}")
print(f"Перемешаный список: {list_mixed}")