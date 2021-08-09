# 1. После запуска предлагает пользователю ввести текст, содержащий любые слова,
# слоги, числа или их комбинации, разделенные пробелом.
# 2. Считывает строку с текстом, и разбивает его на элементы списка, считая
# пробел символом разделителя.
# 3. Печатает этот же список элементов (через пробел), однако с удаленными
# дубликатами.
print("Введите строку для удаления дублирующихся слов:")
line = input()
words = line.split()
# set не сохранит исходный порядок, поэтому используем sorted для его восстановления 
uniquewords = sorted(set(words), key = lambda word: words.index(word))
print(" ".join(uniquewords))