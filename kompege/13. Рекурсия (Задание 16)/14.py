from functools import *


@lru_cache(None)
def F(n):
    if n > 30:
        return n ** 2 + 5 * n + 4
    if n <= 30:
        if n % 2 == 0:
            return F(n + 1) + 3 * F(n + 4)
        else:
            return 2 * F(n + 2) + F(n + 5)


o = 0
for i in range(1, 1001):
    f = str(F(i))
    c = 0
    for j in f:
        c += int(j)
    if c == 27:
        o += 1

print(o)
