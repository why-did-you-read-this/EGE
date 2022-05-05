f = list(map(int, open('17-11.txt').readlines()))
c = 0
m = 99999999999999999999999999
print(f)
for i in range(len(f) - 3):
    i1 = f[i]
    i2 = f[i + 1]
    i3 = f[i + 2]
    i4 = f[i + 3]
    if i1 > i2 > i3 > i4 and (max(i1, i2, i3, i4) - min(i1, i2, i3, i4)) > 1000:
        c += 1
        m = min(m, i1 + i2 + i3 + i4)

print(c, m)
