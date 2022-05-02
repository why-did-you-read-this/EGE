from functools import *


@lru_cache(None)
def F(n):
    if n <= 1:
        return n
    if n > 1:
        if n % 3 == 0:
            return n + F(n / 3)
        else:
            return n + F(n + 3)


for i in range(1, 1001):
    try:
        if F(i) > 100:
            print(i)
            break
    except:
        pass
