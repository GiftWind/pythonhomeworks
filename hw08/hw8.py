# 1. После запуска предлагает пользователю ввести текст.
# 2. Проверяет и, если возможно, преобразовывает полученный текст в число,
# используя рекурсивную функцию.
# Если число четное - делит его на 2 и выводит результат.
# Если число нечетное - умножает на 3 и прибавляет 1.
# После чего ждет следующего ввода.
# 3.При получении в качестве вводных данных 'cancel' завершает свою работу.

def reccast(string):
    def loop(string, acc):
        rad = len(string) - 1
        head = string[0]
        if ord(head) not in range(48, 58):
            return False
        elif rad == 0:
            return acc + ord(head) - 48
        else:
            return loop(string[1:], acc + (ord(head) - 48) * 10**rad)
    return loop(string, 0)
    
def loop():
    userinput = input()
    if userinput == 'cancel':
        print("Bye!")
        return
    else:
        num = reccast(userinput)
        if num == False:
            print("Не удалось преобразовать введенный текст в число.")
        elif num % 2 == 0:
            print(num // 2)
        else:
            print(num * 3 + 1)
    return loop()

loop()
        