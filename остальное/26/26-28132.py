f = open('26-28132.txt')
mem = int(f.readline().split()[0])
a = []
for i in f.read().split():
    a += [int(i)]

c = 0
maxF = 0
a = sorted(a)
for i in range(len(a)):
    if mem - a[i] >= 0:
        mem -= a[i]
        c += 1
    else:
        mem += a[i]
        break

for i in range(len(a) - 1, c, -1):
    if mem - a[i] >= 0:
        maxF = a[i]
        break
print(c, maxF)
