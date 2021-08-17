# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержатся все элементы из каждой коллекции, в упорядоченном виде.

# list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]

def merge(iterable1, iterable2):
    iterator1=iter(iterable1)
    iterator2=iter(iterable2)
    current1 = next(iterator1)
    current2 = next(iterator2)

    while True:
        if current1 <= current2:
            yield current1
            try:
                current1 = next(iterator1)
            except StopIteration:
                while True:
                    yield current2
                    try:
                        current2 = next(iterator2)
                    except StopIteration:
                        return
        else:
            yield current2
            try:
                current2 = next(iterator2)
            except StopIteration:
                while True:
                    yield current1
                    try:
                        current1 = next(iterator1)
                    except StopIteration:
                        return

print(list(merge((x for x in range(1,4)),(x for x in range(2,5)))))