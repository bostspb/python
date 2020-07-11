revenue = int(input("Введите размер выручки (руб.): "))
costs = int(input("Введите размер издержек (руб.): "))
profit = revenue - costs

if revenue > costs:
    print("Поздравляем, ваша фирама работает с прибылью")
    profitability = round((profit / revenue) * 100, 1)
    print(f"Рентабельность составляет {profitability}%")
    employees_number = int(input("Введите количество сотрудников: "))
    profit_per_employee = round(profit / employees_number, 2);
    print(f"Прибыль на одного сотрудника составляет: {profit_per_employee} руб.")
else:
    print("Сожалеем, но ваша фирама работаете в убыток")