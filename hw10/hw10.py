# Вычислить число шагов для числа n, согласно гипотезе
# Коллатца необходимых для достижения этим числом единицы.

# Хвостовая рекурсия
# Разбираюсь с декораторами, чтобы убрать print каждого шага

def collatz(n):
    def loop(i, steps):
        if i == 1:
            print(i)
            return steps
        elif i % 2 == 0:
            print(i)
            return loop(i // 2, steps+1)
        else:
            print(i)
            return loop(i * 3 + 1, steps+1)
    return loop(n, 0)

def collatzdemo(n):
    print(f"Шаги вычисления для {n}:")
    result = collatz(n)
    print(f"Потребовалось {result} шагов.")

collatzdemo(1)
collatzdemo(2)
collatzdemo(1024)
collatzdemo(12)
collatzdemo(100000000000)