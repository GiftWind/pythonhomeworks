# Вычислить число шагов для числа n, согласно гипотезе
# Коллатца необходимых для достижения этим числом единицы.

def collatz(n):
    def loop(i, steps):
        if i == 1:
            return steps
        if i % 2 == 0:
            return loop(i // 2, steps+1)
        return loop(i * 3 + 1, steps+1)
    return loop(n, 0)

def collatzdemo(n):
    result = collatz(n)
    print(f"Для вычисления последовательности Коллатца для числа {n} потребовалось {result} шагов.")

collatzdemo(1)
collatzdemo(2)
collatzdemo(1024)
collatzdemo(12)
collatzdemo(100000000000)