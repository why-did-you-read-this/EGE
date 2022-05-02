from functools import *


@lru_cache(None)
def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x + 2, y) + F(x + 4, y) + F(x + 5, y)


for i in range(31, 10001):
    if F(31, i) == 1001:
        print(i)
        break
