f = list(map(int, open('17-7.txt').readlines()))
c = 0
m = 999999999999999999999

for i in range(len(f) - 1):
    j = i + 1
    if (f[i] * f[j]) > 0 and (f[i] + f[j]) % 7 == 0:
        m = min(m, f[i] * f[j])
        c += 1

print(c, m)
