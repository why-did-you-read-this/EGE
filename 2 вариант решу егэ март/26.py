# https://inf-ege.sdamgia.ru/problem?id=33528
f = open('26.txt')
count_b = 0
a = []
b = []

limit = limit1 = int(f.readline().split()[1])
f = f.read().split('\n')
c = 0
for s in f:
    ss = s.split()
    try:
        if len(ss) == 3:
            if ss[2] == 'A':
                a.append([int(ss[0]), int(ss[1])])
            else:
                b.append([int(ss[0]), int(ss[1])])
    except None:
        pass

a = sorted(a)
b = sorted(b)

for i in range(len(a)):
    while a[i][1] > 0:
        if limit > 0:
            if a[i][1] > 0:
                limit -= a[i][0]
                a[i][1] -= 1
        else:
            a[i][1] += 1
            limit += a[i][0]
            break

for i in range(len(b)):
    while b[i][1] > 0:
        if limit > 0:
            if b[i][1] > 0:
                limit -= b[i][0]
                b[i][1] -= 1
                count_b += 1
        else:
            b[i][1] += 1
            limit += b[i][0]
            count_b -= 1
            break

print(count_b, limit)
