from functools import *


@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) - 2 * G(n - 1)


def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + G(n - 1) + n


o = 0
for i in str(G(36)):
    o += int(i)
print(o)
