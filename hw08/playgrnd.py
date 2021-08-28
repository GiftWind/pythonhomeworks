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
        
print(reccast('1234'))