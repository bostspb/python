#Для проверки:
#time_in_seconds = 2*60*60 + 5*60 + 2

time_in_seconds = int(input('Введите количество секунд, которые нужно преобразовать в формат чч.мм.сс \n> '))

hours = time_in_seconds // (60 * 60)
seconds_for_minutes = time_in_seconds - hours * 60 * 60
minutes = seconds_for_minutes // 60
seconds = seconds_for_minutes % 60

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

print(f"{time_in_seconds} секунд - это {hours}:{minutes}:{seconds}")


