from functools import *


@lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n > 0:
        if n % 2 == 0:
            return F(n // 2)
        else:
            return 1 + F(n - 1)


o = 0
for i in range(1, 501):
    if F(i) == 8:
        o += 1

print(o)
