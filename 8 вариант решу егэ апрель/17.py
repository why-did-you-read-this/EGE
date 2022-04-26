f = open('17.txt').read().split()
c = 0
maxR = 0
for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if (int(f[i]) - int(f[j])) % 36 == 0:
            # or (int(f[j]) - int(f[i])) % 36 == 0
            if int(f[i]) % 13 == 0 or int(f[j]) % 13 == 0:
                c += 1
                maxR = max(maxR, int(f[i]) - int(f[j]))

print(c, maxR)
