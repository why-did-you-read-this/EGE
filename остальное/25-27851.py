# https://inf-ege.sdamgia.ru/problem?id=27851

for i in range(210235,210301):
    deliteli = []
    for d in range(2, int(i**0.5) + 1):
        k = i // d
        if len(deliteli) > 4:
            break
        if i % d == 0:
            deliteli += [d]
        if i % k == 0:
            deliteli += [k]
        if d == k:
            deliteli.pop(-1)
    if len(deliteli) == 4:
        deliteli = sorted(deliteli)
        print(*deliteli)