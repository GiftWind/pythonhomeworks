# Написать скрипт, который будет вытаскивать gps данные
# из фотографии (jpg файл) и передавать их на вход программе
# из hw16.txt
import os
from exif import Image

with open("hw17/spb.jpg", 'rb') as src:
    img = Image(src)
print(img.list_all())
