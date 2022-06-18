f = [int(i) for i in open('17.txt').readlines()]
c = 0
ms = 0
ch = []

for i in f:
    if i % 2 == 0:
        ch.append(i)

sr_ch = sum(ch) / len(ch)

for i in range(len(f) - 1):
    if ((f[i] % 3 == 0) or (f[i + 1] % 3 == 0)) and ((f[i] < sr_ch) or (f[i + 1] < sr_ch)):
        c += 1
        ms = max(ms, f[i] + f[i + 1])

print(c, ms)
