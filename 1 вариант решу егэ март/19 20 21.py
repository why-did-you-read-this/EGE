# 19 https://inf-ege.sdamgia.ru/problem?id=27416
# 20 https://inf-ege.sdamgia.ru/problem?id=27417
# 21 https://inf-ege.sdamgia.ru/problem?id=27418
from functools import *


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 77:
        return 'w'
    if any(game(i) == 'w' for i in moves(h)):
        return 'p1'
    if all(game(i) == 'p1' for i in moves(h)):  # для 19 нужно заменить all на any
        return 'v1'
    if any(game(i) == 'v1' for i in moves(h)):
        return 'p2'
    if all(game(i) == 'p1' or game(i) == 'p2' for i in moves(h)):
        return 'v2'


for i in range(1, 70):
    h = 7, i
    print(i, game(h))
