m = 0
for i in range(1000):
    s = i
    n = 1
    while s <= 80:
        s += 7
        n *= 3
    if n == 81:
        m = max(m, i)

print(m)
