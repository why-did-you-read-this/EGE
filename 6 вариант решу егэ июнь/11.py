from itertools import *

for i in range(1, 10000):
    c = 0
    for j in product('2468', repeat=i):
        c += 1
    if c >= 200:
        print(i)
        break
