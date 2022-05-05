f = [int(i) for i in open('17-18.txt')]

c = 0
m = float('-inf')

for i in range(len(f) - 1):
    i1 = f[i]
    i2 = f[i + 1]
    if (i1 % 9 == 0) and (i2 % 9 != 0) and (oct(i2)[-1] == '3'):
        c += 1
        m = max(m, max(i1, i2))
    elif (i1 % 9 != 0) and (i2 % 9 == 0) and (oct(i1)[-1] == '3'):
        c += 1
        m = max(m, max(i1, i2))

print(c, m)
