# Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# >> [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# >> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]

import numpy as np

def n_arr(dims):
    nparray = np.zeros(tuple(dims), dtype=np.int8)
    return nparray.tolist()

a = n_arr([2,2,2])
a[0][0][0] = 1
print(a)

b = n_arr([2,2])
b[1][0] = 1
print(b)