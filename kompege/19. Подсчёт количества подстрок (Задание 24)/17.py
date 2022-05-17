f = open('24-17.txt').readline().strip()
a = sorted('QWERTYUIOPLKJHGFDSAZXCVBNM')
b = [0] * len(a)
for i in range(1, len(f) - 1):
    if f[i - 1] == f[i + 1]:
        b[a.index(f[i])] += 1

print(a[b.index(max(b))] + str(max(b)))
