# https://inf-ege.sdamgia.ru/problem?id=37161

f = open('26-37161.txt')
f.readline()
a = []
otvet = []
maxR = 0
minM = 0
for s in f.read().split('\n'):
    a += [[int(s.split()[0]), int(s.split()[1])]]
a = sorted(a)

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i][0] == a[j][0]:
            if a[j][1] - a[i][1] == 3:
                otvet += [a[i]]
maxa = 0
minb = 10 ** 20
for a, b in otvet[::-1]:
    maxa = max(maxa, a)
    if a == maxa:
        minb = min(minb, b)
    else:
        break
print(maxa, minb + 1)
