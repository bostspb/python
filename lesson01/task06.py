first_day_result = int(input(f"Введите результат пробежки в первый день (км): "))
goal = int(input(f"Введите желаемый результат (км): "))

today_result = first_day_result
day = 1

print(f"{day}-й день: {today_result} км")

while today_result < goal:
    day += 1
    today_result = round(0.1 * today_result + today_result, 3)
    print(f"{day}-й день: {today_result} км")

print(f"На {day}-й день вы достигните желаемого результата {goal} км")