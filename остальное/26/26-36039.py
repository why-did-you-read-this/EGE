# https://inf-ege.sdamgia.ru/problem?id=36039
f = open('26-36039.txt')
mem = int(f.readline().split()[0])
a = []
for i in f.read().split():
    a += [int(i)]
a = sorted(a)
c = 0
maxF = 0

for i in range(len(a)):
    if mem - a[i] >= 0:
        mem -= a[i]
        c += 1
    else:
        mem += a[i]
        break

for i in range(len(a)-1, c, -1):
    if mem - a[i] >= 0:
        maxF = a[i]
        break

print(c, maxF)
