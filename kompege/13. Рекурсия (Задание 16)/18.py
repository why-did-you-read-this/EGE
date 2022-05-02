from functools import *


@lru_cache(None)
def F(n):
    s = n**2
    if n > 1:
        s += (2 * n + 1) + F(n - 2) + F(n // 3)
    return s



print(F(100))

