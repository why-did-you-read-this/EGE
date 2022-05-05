f = list(map(int, open('17-14.txt').readlines()))

c = 0
m = -float('inf')
sr = sum(f) / len(f)

for i in range(len(f) - 2):
    a = sorted([f[i], f[i + 1], f[i + 2]])
    i1 = a[0]
    i2 = a[1]
    i3 = a[2]
    if (i1 > sr) + (i2 > sr) + (i3 > sr) >= 2:
        c += 1
        m = max(m, sum(a))

print(c, m)
