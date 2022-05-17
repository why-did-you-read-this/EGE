f = [int(i) for i in open('KIM_0002848150_17.txt')]
c = 0
m = 99999999999999999
mS = -9999

for i in f:
    if i % 6 == 0:
        m = min(m, i)

for i in range(len(f) - 1):
    if (f[i] % m == 0) and (f[i + 1] % m == 0):
        c += 1
        mS = max(mS, f[i] + f[i + 1])

print(c, mS)
