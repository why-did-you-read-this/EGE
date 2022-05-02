m = 0
for i in range(10000):
    n = 1024
    s = i
    while s >= 5:
        s = s - 5
        n = n // 2
    if n == 64:
        m = max(m, i)

print(m)
