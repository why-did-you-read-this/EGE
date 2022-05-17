f = open('24-6.txt').readline()
c = 0
for i in range(len(f) - 3):
    if (f[i] + f[i + 1] + f[i + 2] + f[i + 3]) == 'XXXX':
        c += 1

print(c)
print(f.count('XXXX'))
