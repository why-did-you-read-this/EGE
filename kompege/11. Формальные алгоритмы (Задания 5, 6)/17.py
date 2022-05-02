m = 0
for i in range(1000):
    s = i
    n = 3
    while s < 220:
        s += 6
        n += 3
    if n > 40:
        m = max(m, i)

print(m)
