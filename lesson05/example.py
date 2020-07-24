import os
import json
import requests

url = 'https://api.github.com/users/bostspb'
response = requests.get(url)
data = response.text

# file = open('test.txt', 'w', encoding='UTF-8')
# file.write(data)
# file.close()

with open('test.txt', 'w', encoding='UTF-8') as file:
    file.write(data)

url_img = 'https://images.squarespace-cdn.com/content/5a47cac251a584ab2cc76ad3/1515474001125-Z8UT8CHOY52VKR3X64WT/static1.squarespace.png'
response_img = requests.get(url_img)
img = response_img.content
this_path = os.path.dirname(__file__)
img_path = os.path.join(this_path, 'images', 'test.png')
with open(img_path, 'wb') as file_img:
    file_img.write(img)


print(this_path)

# try:
#     with open("text.txt") as f_obj:
#         for line in f_obj:
#             print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")