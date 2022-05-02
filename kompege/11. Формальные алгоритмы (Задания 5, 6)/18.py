m = set()
for i in range(9, 3000):
    s = i
    n = 3
    while s * n < 243:
        s //= 3
        n *= 9
    if n == 27:
        m.add(i)

print(len(m))
