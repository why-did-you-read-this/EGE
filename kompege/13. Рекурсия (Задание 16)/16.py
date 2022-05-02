from functools import *


@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n >= 2:
        if n % 2 == 0:
            return F(n / 2) + 1
        else:
            return F(n - 1) + n


m = 999999999999999999999
for i in range(1, 1001):
    if F(i) == 19:
        m = min(m, i)

print(m)
