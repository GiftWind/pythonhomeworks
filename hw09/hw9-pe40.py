# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# Решение с помощью left fold (однострочник если import не считается):
import functools
print(functools.reduce(lambda x,y: int(x) * int(y), (''.join(str(i) for i in range(1, 200000))[i-1] for i in [10 ** i for i in range(7)])))

# И чистый однострочник:
print(eval('*'.join([''.join(str(i) for i in range(1, 200000))[i-1] for i in [10 ** i for i in range(7)]])))