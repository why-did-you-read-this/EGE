f = [int(i) for i in open('17.txt')]
e21 = 999999999999999999
for i in f:
    if i % 21 == 0:
        e21 = min(e21, i)

c = 0
m = 0

for i in range(len(f) - 1):
    if (f[i] % e21 == 0) or (f[i + 1] % e21 == 0):
        c += 1
        m = max(m, f[i] + f[i + 1])

print(c, m)
