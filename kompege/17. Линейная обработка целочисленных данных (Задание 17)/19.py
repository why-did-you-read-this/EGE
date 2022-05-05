f = [int(i) for i in open('17-19.txt')]

c = 0
m = float('-inf')


def F(x):
    return (x > 0) and (str(x)[-1] == '9')


for i in range(len(f) - 2):
    i1 = f[i]
    i2 = f[i + 1]
    i3 = f[i + 2]
    if (not(F(i1))) and F(i2) and (not(F(i3))):
        c += 1
        m = max(m, i1 + i2 + i3)

print(c, m)
