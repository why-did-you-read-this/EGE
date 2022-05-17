f = open('24-8.txt').readline()
c = 0
for i in range(len(f) - 4):
    if f[i] == f[i + 2] == f[i + 4] == 'A':
        c += 1

print(c)
