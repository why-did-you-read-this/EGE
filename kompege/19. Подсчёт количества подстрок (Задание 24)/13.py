f = open('24-13.txt').readline()
c = 0
for i in range(6, 10):
    for j in range(len(f) - i):
        if f[j] == 'A' and f[j + i] == 'F':
            c += 1

print(c)
