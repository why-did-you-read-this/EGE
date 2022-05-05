f = list(map(int, open('17-17.txt').readlines()))

min4 = float('inf')
max4 = float('-inf')
m = float('-inf')
c = 0

for i in f:
    if str(i)[-1] == '4':
        min4 = min(min4, i)
        max4 = max(max4, i)

sum4 = min4 + max4

for i in range(len(f) - 1):
    i1 = f[i]
    i2 = f[i + 1]
    if (i1 + i2) < sum4:
        c += 1
        m = max(m, i1 + i2)

print(c, m)
