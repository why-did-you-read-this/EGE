def deliteli(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 2):
        if x % i == 0 and i % 2 == 0:
            d.add(i)
        k = x // i
        if x % k == 0 and k % 2 == 0:
            d.add(k)
    d = sorted(d)
    return d


for j in range(110203, 110246):
    dI = deliteli(j)
    if len(dI) == 4:
        print(*dI)
