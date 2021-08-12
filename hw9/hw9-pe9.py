import time
start = time.perf_counter()
print([a * b * c for a in range(1,1000) for b in range(1,1000) for c in [1000-b-a] if a**2 + b**2 == c**2 and a < b and b < c][0])
stop = time.perf_counter()
print(stop - start)