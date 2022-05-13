f = open('24-12.txt').readline()
maxC = 0
c = 1
for i in range(1, len(f)):
    if f[i - 1] < f[i] or i == len(f) - 1:
        c += 1
    else:
        maxC = max(maxC, c)
        c = 1

print(maxC)
