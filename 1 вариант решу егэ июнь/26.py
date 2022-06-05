f = open('26.txt')
f.readline()
f = [int(i) for i in f.readlines()]
c = 0
sr = 0
nch_f = []
for i in f:
    if i % 2 == 1:
        nch_f += [i]

for i in range(len(nch_f)):
    for j in range(i + 1, len(nch_f)):
        q = (nch_f[i] + nch_f[j]) / 2
        if q in f:
            c += 1
            sr = max(sr, q)

print(c, sr)
