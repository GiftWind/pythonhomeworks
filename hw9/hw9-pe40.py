import functools
print(functools.reduce(lambda x,y: int(x) * int(y), (''.join(str(i) for i in range(1, 200000))[i-1] for i in [10 ** i for i in range(7)])))