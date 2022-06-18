def F(x):
    deliteli = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            deliteli.add(d)
            if x % (x // d) == 0:
                deliteli.add(x // d)
    return sorted(deliteli)


c = 0
for i in range(452_022, 10 ** 100):
    if c >= 5:
        break
    f = F(i)
    if len(f) >= 2:
        s = f[0] + f[-1]
        if s % 7 == 3:
            c += 1
            print(i, s)
