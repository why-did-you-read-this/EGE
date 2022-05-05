f = open('17-1.txt').read().split()
f = list(map(int, f))
m = 0
c = 0
for i in f:
    if (i % 3 == 0) and (i % 7 != 0) and (i % 17 != 0) and (i % 19 != 0) and (i % 27 != 0):
        c += 1
        m = max(m, i)

print(c, m)
