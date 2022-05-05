f = list(map(int, open('17-13.txt').readlines()))

c = 0
m = float('inf')

for i in range(len(f) - 1):
    i1 = f[i]
    i2 = f[i + 1]
    s = abs(i1) + abs(i2)
    if 50 <= s <= 200:
        c += 1
        m = min(m, min(i1, i2))

print(c, m)
