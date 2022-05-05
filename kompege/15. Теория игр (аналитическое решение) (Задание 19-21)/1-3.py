from functools import *


def m(h):
    return h + 1, h + 2, h + 3


@lru_cache(None)
def g(h):
    if h >= 21:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all(g(i) == 'p1' or g(i) == 'p2' for i in m(h)):
        return 'v2'
    if any(g(i) == 'v2' for i in m(h)):
        return 'p3'
    if any(g(i) == 'p3' for i in m(h)):
        return 'v3'


for i in range(1, 21):
    if g(i) == 'v1' or g(i) == 'v2' or g(i) == 'v3':
        print(i, g(i))
