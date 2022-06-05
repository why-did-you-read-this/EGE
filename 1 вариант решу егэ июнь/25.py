def deliteli(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 1:
                d.add(i)
            if x % (x / i) == 0:
                if (x / i) % 2 == 1:
                    d.add(int(x / i))
    return sorted(d)


o = []
for j in range(45_000_000, 50_000_001):
    if j % 100_000 == 0:
        print(j)
    if len(deliteli(j)) == 5:
        o += [j]

print('')
print(sorted(o))
