from functools import *


@lru_cache(None)
def F(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n > 1:
        return F(n - 1) - F(n - 2) + 3 * n


print(F(40))
