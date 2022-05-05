f = list(map(int, open('17-9.txt').readlines()))
c = 0
m = 0
for i in range(len(f)-2):
    i1 = f[i]
    i2 = f[i + 1]
    i3 = f[i + 2]
    if ((i1 % 12 == 0) or (i2 % 12 == 0) or (i3 % 12 == 0)) and (i1 % 3 == 0) and (i2 % 3 == 0) and (i3 % 3 == 0):
        c += 1
        m = min(m, (i1 + i2 + i3) / 3)

print(c, m)
