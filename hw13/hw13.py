# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.

def convert(temperature, unit):

    def to_fahrenheit(temp):
        if temp < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля.")
        return temp * 9 / 5 + 32

    def to_celsius(temp):
        if temp < -459.67:
            raise ValueError("Температура не может быть ниже абсолютного нуля.")
        return (temp - 32) * 5 / 9

    if unit.upper() == 'C':
        return (to_fahrenheit(temperature), 'F')
    elif unit.upper() == 'F':
        return (to_celsius(temperature), 'C')
    else:
        print("Введите корректную единицу измерения температуры: F или С")

print(convert(32, 'F'))
print(convert(0, 'C'))
print(convert(-300, 'C'))
