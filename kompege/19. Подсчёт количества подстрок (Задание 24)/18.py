f = open('24-18.txt').readline()
a = sorted('QWERTYUIOPLKJHGFDSAZXCVBNM')
b = [0] * len(a)

for i in range(len(f) - 4):
    if (f[i] + f[i + 1]) == (f[i + 4] + f[i + 3]) == 'CB':
        b[a.index(f[i + 2])] += 1

print(a[b.index(max(b))] + str(max(b)))
