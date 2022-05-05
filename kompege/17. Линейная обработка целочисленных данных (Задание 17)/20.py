f = [int(i) for i in open('17-20.txt')]

c = 0
m = float('inf')
s = 0

for i in f:
    if i % 35 == 0:
        i = str(i)
        for j in i:
            s += int(j)

for i in range(len(f) - 1):
    i1 = f[i]
    i2 = f[i + 1]
    if ((i1 > s) and (not (i2 > s)) and (hex(i2)[-2] + hex(i2)[-1] == 'ef')) or (
            (i2 > s) and (not (i1 > s)) and (hex(i1)[-2] + hex(i1)[-1] == 'ef')):
        c += 1
        m = min(m, i1 + i2)

print(c, m)
