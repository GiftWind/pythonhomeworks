# 1. После запуска предлагает пользователю ввести целые неотрицательные числа,
# разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
# 2. Получив вводные данные, выделяет полученные числа, суммирует их,
# и печатает полученную сумму.
import re
print("Введите набор целых неотрицательных чисел для суммирования:")
userinput = input()
numberslist = [int(n) for n in re.findall('-?\d+', userinput)]
print(sum(numberslist))