f = [int(i) for i in open('17.txt').readlines()]
d = 160
p = 7
a = []

for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if ((f[i] % d) != (f[j] % d)) and ((f[i] % p == 0) or (f[j] % p == 0)):
            a.append(f[i] + f[j])

print(len(a), max(a))
