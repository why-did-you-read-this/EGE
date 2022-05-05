f = list(map(int, open('17-12.txt').readlines()))

c = 0
m = -float('inf')

for i in range(len(f) - 1):
    i1 = f[i]
    i2 = f[i + 1]
    if (i1 + i2 >= 100) and (i1 < 0 or i2 < 0):
        c += 1
        m = max(m, i1 * i2)

print(c, m)
