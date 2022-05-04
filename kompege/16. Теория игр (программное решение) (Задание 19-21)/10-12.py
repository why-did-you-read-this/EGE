from functools import *


def m(h):
    a, b = h
    return (a + 1, b), (b + 1, a), (a * 2, b), (a, b * 2)


@lru_cache(None)
def g(h):
    a, b = h
    if a + b > 76:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all(g(i) == 'p1' or g(i) == 'p2' for i in m(h)):
        return 'v2'


for i in range(1, 70):
    h = 7, i
    if g(h) == 'v2':
        print(i, g(h))
