string_with_numbers = input('Введите целое положительное число, желательно побольше \n> ')
string_length = len(string_with_numbers)

# Если бы не условие в задании, то я бы лучше использовал цикл for .. in ..
i = 0
biggest_digit = 0
while i < string_length:
    if(int(string_with_numbers[i]) > biggest_digit) :
        biggest_digit = int(string_with_numbers[i])
    i += 1

print(f"Самая большая цифра в числе: {biggest_digit}")
