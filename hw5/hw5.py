# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.

print("Введите набор целых неотрицательных чисел, разделенных пробелами:")
userinput = input()

numbersarray = [int(n) for n in userinput.split()]
numbersset = set(numbersarray)
# Предположим, что в множестве чисел пропущена единица 
missingnumbers = set([1])
# Если число содержится в изначальном множестве, то оно не пропущено
# Тогда минимальным пропущеным может быть число на единицу больше текущего 
for i in numbersset:
    if i in missingnumbers:
        missingnumbers.remove(i)
        missingnumbers.add(i + 1)
minimalmissingnumber = min(missingnumbers)
print(minimalmissingnumber)