user_name = input('Как вас зовут? - ')
user_age = int(input('Сколько вам лет? - '))
user_city = input('В каком городе вы живете? - ')
user_city_living = input(f'Как долго вы живете в городе {user_city}? - ')

print(f"{user_name}, вам {user_age} лет и вы живете в городе {user_city} {user_city_living}. А еще вы {2020 - user_age} года рождения." )

