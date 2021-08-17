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
# Минимальным пропущеным может быть число на единицу больше текущего 
missingnumbers = missingnumbers | set([i + 1 for i in numbersset])
# Если число содержится в изначальном множестве, то оно не пропущено
missingnumbers = missingnumbers - numbersset
minimalmissingnumber = min(missingnumbers)
print(minimalmissingnumber)