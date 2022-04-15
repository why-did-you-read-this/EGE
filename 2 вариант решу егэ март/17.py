f = open('17.txt').read().split()
c = 0
max_sum = -9999
for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if (int(f[i]) - int(f[j])) % 2 == 0 and ((int(f[i]) % 31 == 0) or (int(f[j]) % 31 == 0)):
            c += 1
            max_sum = max(max_sum, int(f[i]) + int(f[j]))
print(c, max_sum)
