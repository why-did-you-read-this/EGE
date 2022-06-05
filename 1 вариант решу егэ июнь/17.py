f = [int(i) for i in open('17.txt')]
summa = 0
c = 0
for i in f:
    if i % 2 == 0:
        c += 1
        summa += i
sr_ch = summa / c
c = 0
max_sum = 0
for i in range(len(f) - 1):
    if (f[i] % 3 == 0) or (f[i + 1] % 3 == 0):
        if (f[i] < sr_ch) or (f[i + 1] < sr_ch):
            c += 1
            max_sum = max(max_sum, f[i] + f[i + 1])

print(c, max_sum)
