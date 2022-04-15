f = open('26_demo.txt')
ff = f.readline().split()
mem = int(ff[0])
a = []
for i in f:
    a.append(int(i.rstrip()))
a = sorted(a)
maxs = 0
files = []
for i in range(len(a)):
    if mem - a[i] > 0:
        files.append(a[i])
        mem -= a[i]
        maxs = max(maxs, a[i])
    else:
        last = files[-1]
        mem += last
        for j in range(i, len(a)):
            if last < a[j] < mem:
                maxs = max(maxs, a[j])
        break

print(len(files), maxs)
