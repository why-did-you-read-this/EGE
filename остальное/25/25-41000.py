def F(x):
    deliteli = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            deliteli.add(d)
            if x % (x // d) == 0:
                deliteli.add(x // d)
    return sorted(deliteli)


c = 0
for i in range(11_000_000, 10 ** 100):
    if c >= 5:
        break
    f = F(i)
    if len(f) >= 2:
        s = f[-1] + f[-2]
        if 2 <= s < 10_000:
            c += 1
            print(s)
