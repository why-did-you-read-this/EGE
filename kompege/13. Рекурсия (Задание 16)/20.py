from functools import *


@lru_cache(None)
def F(n):
    if n < 3:
        return n + 1
    else:
        if n % 2 == 0:
            return F(n - 2) + n - 2
        else:
            return F(n + 2) + n + 2


c = 0
for i in range(1, 1001):
    try:
        if len(str(F(i))) == 5:
            c += 1
    except:
        pass

print(c)
