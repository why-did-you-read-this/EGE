f = [int(i) for i in open('17.txt').readlines()]

c = 0
ms = 0
for i in range(len(f) - 1):
    for j in range(i + 1, len(f)):
        if (((f[i] - f[j]) % 2 == 0) or ((f[j] - f[i]) % 2 == 0)) and ((f[i] % 31 == 0) or (f[j] % 31 == 0)):
            c += 1
            ms = max(ms, f[i] + f[j])

print(c, ms)
