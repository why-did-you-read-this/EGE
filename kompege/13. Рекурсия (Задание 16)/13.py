from functools import *


@lru_cache(None)
def F(n):
    if n <= 18:
        return n + 3
    else:
        if n % 3 == 0:
            return (n // 3) * F(n // 3) + n - 12
        else:
            return F(n - 1) + n * n + 5


c = 0
for i in range(1, 1001):
    f = str(F(i))
    if all(int(j) % 2 == 0 for j in f):
        c += 1

print(c)
