# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# Пример:

# Input data: 60,01';30,19'
# Output data:
# Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Homework16")
location = geolocator.reverse("60.0166666666666666666,30.322")

print(location.raw)