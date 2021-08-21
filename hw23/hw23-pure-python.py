# Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# >> [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# >> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]

def n_arr(dims):
    expression = '""'
    def decorate(expression, n):
        return f'[{expression} for _ in range({n})]'
    for n in dims:
        expression = decorate(expression, n)
    return eval(expression)

a = n_arr([2,2,2])
a[0][0][0] = 1
print(a)

b = n_arr([2,2])
b[1][0] = 1
print(b)