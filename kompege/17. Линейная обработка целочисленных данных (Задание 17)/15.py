f = list(map(int, open('17-15.txt').readlines()))

c = 0
m = float('inf')
s = 0

for i in f:
    if i % 19 == 0:
        s = max(s, i)

for i in range(len(f) - 1):
    i1 = f[i]
    i2 = f[i + 1]
    if (i1 > s) or (i2 > s):
        c += 1
        m = min(m, i1 + i2)

print(c, m)
