f = list(map(int, open('17-6.txt').readlines()))
c = 0
m = 0

for i in range(len(f) - 1):
    j = i + 1
    if ((f[i] + f[j]) % 3 == 0) and ((f[i] + f[j]) % 6 != 0) and (str((f[i] * f[j]))[-1] == '8'):
        c += 1
        m = max(m, f[i] + f[j])

print(c, m)
