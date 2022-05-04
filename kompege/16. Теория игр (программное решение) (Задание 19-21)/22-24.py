from functools import *


def m(h):
    a, b = h
    x = []
    if a > 0:
        x += [(a - 1, b)]
    if b > 0:
        x += [(a, b - 1)]
    if a > 1:
        x += [((a + 1) // 2, b)]
    if b > 1:
        x += [(a, (b + 1) // 2)]
    return x


@lru_cache(None)
def g(h):
    a, b = h
    if a + b <= 20:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all(g(i) == 'p1' or g(i) == 'p2' for i in m(h)):
        return 'v2'


for i in range(10, 151):
    h = 10, i
    if g(h) == 'v2':
        print(i, g(h))
