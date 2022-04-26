f = open('28141.txt')
c = 0
maxF = 0
mem = int(f.readline().split()[0])
a = []
for i in f.read().split():
    a += [int(i)]
a.sort()

for i in a:
    if mem - i >= 0:
        mem -= i
        c += 1
        maxF = max(maxF, i)
    else:
        mem += i
        break

for i in range(len(a) - 1, c + 1, -1):
    if mem - a[i] >= 0:
        mem -= a[i]
        maxF = max(maxF, a[i])
        break
print(c, maxF)
