from math import sqrt

c = 0
for i in range(200_000_001, 10 ** 20):
    if c >= 5:
        break
    deliteli = []
    for d in range(2, int(sqrt(i)) + 1):
        if i % d == 0:
            deliteli += [d]
            k = i // d
            if i % k == 0:
                deliteli += [k]
            if d == k:
                deliteli.pop(-1)
    deliteli = sorted(deliteli)
    if len(deliteli) >= 5:
        q = deliteli[0] * deliteli[1] * deliteli[2] * deliteli[3] * deliteli[4]
        if q < i:
            c += 1
            print(q, i)
