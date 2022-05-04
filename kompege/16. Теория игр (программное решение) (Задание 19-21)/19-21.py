from functools import *


def m(h):
    a, b, c = h
    return (a + 3, b, c), (a, b + 3, c), (a, b, c + 3), (a + 13, b, c), (a, b + 13, c), (a, b, c + 13), (
        a + 23, b, c), (a, b + 23, c), (a, b, c + 23)


@lru_cache(None)
def g(h):
    a, b, c = h
    if a + b + c >= 73:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all(g(i) == 'p1' or g(i) == 'p2' for i in m(h)):
        return 'v2'


for i in range(1, 24):
    h = 2, i, 2 * i
    if g(h) == 'v2':
        print(i, g(h))
