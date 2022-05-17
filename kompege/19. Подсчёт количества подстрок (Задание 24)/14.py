f = open('24-14.txt').readline()
c = 0
for i in range(len(f) - 4):
    if (f[i] + f[i + 1]) == (f[i + 4] + f[i + 3]):
        c += 1
print(c)
