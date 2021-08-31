# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# Пример:

# Input data: 60,01';30,19'
# Output data:
# Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322

from geopy.geocoders import Nominatim

# Не совсем понятен формат записи координат. 
# Допустим, координаты с указанием угловых секунд имеют вид 60,01'10"
def parsetodec(str):
    degminsec = str.split(',')
    deg = float(degminsec[0])
    minsec = degminsec[1].split("'")
    min = float(minsec[0])
    # Угловые секунды могут отсутствовать
    sec = minsec[1]
    if sec != "":
        sec = float(sec.rstrip('"'))
    else:
        sec = 0
    return deg + min / 60 + sec / 3600

def getcoordinatesfromfile(file):
    with open(file, 'r') as f:
        coords = f.readline().split(";")
        latitude = parsetodec(coords[0])
        longitude = parsetodec(coords[1])
    return f"{latitude},{longitude}"

coordinates = getcoordinatesfromfile('coordinates.txt')

geolocator = Nominatim(user_agent="Homework16")
location = geolocator.reverse(coordinates)

print(f"Location: {location}")
print(f"Google Maps URL: https://www.google.com/maps/search/?api=1&query={coordinates}")