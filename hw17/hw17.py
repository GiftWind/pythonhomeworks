#!/usr/bin/env python3
# Написать скрипт, который будет вытаскивать gps данные
# из фотографии (jpg файл) и передавать их на вход программе
# из hw16.txt
import sys
import hw16
from exif import Image

def getcoordinates(photo):
    with open(photo, 'rb') as src:
        img = Image(src)
    latitude = img['gps_latitude']
    longitude = img['gps_longitude']
    # Convert float degrees, minutes and seconds to int
    latitude = list(map(lambda x: int(x), latitude))
    longitude = list(map(lambda x: int(x), longitude))
    latitudestring = f"{latitude[0]},{latitude[1]}'{latitude[2]}" + '"'
    longitudestring = f"{longitude[0]},{longitude[1]}'{longitude[2]}" + '"'
    return f"{latitudestring};{longitudestring}"

def writecoordinates(photo):
    with open('coordinates.txt', "w") as f:
        f.write(getcoordinates(photo))

if __name__ == '__main__':
    # First argument is a path to image
    photo = sys.argv[1]
    writecoordinates(photo)
    hw16.main()
