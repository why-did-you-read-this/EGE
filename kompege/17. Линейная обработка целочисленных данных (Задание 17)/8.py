f = list(map(int, open('17-8.txt').readlines()))
c = 0
m = 0
for i in range(len(f) - 2):
    i1 = f[i]
    i2 = f[i + 1]
    i3 = f[i + 2]
    if (i1 * i2 * i3) % 7 == 0 and str(i1 + i2 + i3)[-1] == '5':
        c += 1
        m = max(m, i1 + i2 + i3)

print(c, m)
