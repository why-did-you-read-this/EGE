f = open('24.txt').readline()
maxc = 0
cD = 0
c = 0
for i in range(len(f)):
    c += 1
    if i == len(f) - 1:
        maxc = max(maxc, c)
    if f[i] == 'D':
        cD += 1
    if cD > 1:
        c -= 1
        maxc = max(maxc, c)
        cD = 0
        c = 0
g = f[::-1]
cD = 0
c = 0
for i in range(len(g)):
    c += 1
    if i == len(g) - 1:
        maxc = max(maxc, c)
    if g[i] == 'D':
        cD += 1
    if cD > 1:
        c -= 1
        maxc = max(maxc, c)
        cD = 0
        c = 0
print(maxc)
