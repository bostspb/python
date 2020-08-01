"""
    3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
    вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
    только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
    соответственно. В методе деления должно осуществляться округление значения до целого числа.

    Сложение. Объединение двух клеток.
    При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

    Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
    количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

    Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
    произведение количества ячеек этих двух клеток.

    Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
    как целочисленное деление количества ячеек этих двух клеток.

    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    Данный метод позволяет организовать ячейки по рядам.

    Метод должен возвращать строку вида *****\n*****\n*****...,
    где количество ячеек между \n равно переданному аргументу.
    Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n**.

    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class OrganicCell(object):
    def __init__(self, size: int):
        if size <= 0:
            raise Exception('Клетка не может иметь меньше одной ячейки')
        self.size = size

    def __add__(self, other):
        return OrganicCell(self.size + other.size)

    def __sub__(self, other):
        result = self.size - other.size
        if result > 0:
            return OrganicCell(result)
        else:
            raise Exception(f'Ошибка! Вычитание {self} из {other} невозможно!')

    def __mul__(self, other):
        return OrganicCell(self.size * other.size)

    def __truediv__(self, other):
        return OrganicCell(self.size // other.size)

    def make_order(self, row_size: int) -> str:
        rows = ['*' * row_size for _ in range(self.size // row_size)]
        tail = '*' * (self.size % row_size)
        rows.append(tail)
        return '\n'.join(rows)

    def __str__(self):
        return '*' * self.size


if __name__ == '__main__':
    ameba_1 = OrganicCell(2)
    ameba_2 = OrganicCell(6)
    ameba_add = ameba_1 + ameba_2
    try:
        ameba_sub1 = ameba_1 - ameba_2
    except Exception as e:
        ameba_sub1 = None
        print(e)
    ameba_sub2 = ameba_2 - ameba_1
    ameba_mul = ameba_1 * ameba_2
    ameba_div = ameba_2 / ameba_1

    print('ameba_1\t', ameba_1)
    print('ameba_2\t', ameba_2)
    print('add\t\t', ameba_add)
    print('sub1\t', ameba_sub1)
    print('sub2\t', ameba_sub2)
    print('mul\t\t', ameba_mul)
    print('div\t\t', ameba_div)

    ameba_3 = OrganicCell(18)
    order_18_5 = ameba_3.make_order(5)
    print(f'\norder_18_5\n{order_18_5}')