f = open('24-16.txt').readline().strip()
a = sorted('QWERTYUIOPLKJHGFDSAZXCVBNM')
b = [0] * len(a)
for i in f:
    b[a.index(i.capitalize())] += 1

print(max(b) - min(b))
