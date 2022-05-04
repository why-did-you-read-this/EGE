from functools import *


def m(h):
    return h + 1, h * 3


@lru_cache(None)
def g(h):
    if h >= 2163:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all(g(i) == 'p1' or g(i) == 'p2' for i in m(h)):
        return 'v2'


for i in range(2163, 1, -1):
    gi = g(i)
    if gi == 'v2':
        print(i, gi)
