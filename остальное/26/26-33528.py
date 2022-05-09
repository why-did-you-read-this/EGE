# https://inf-ege.sdamgia.ru/problem?id=33528
f = open('26-33528.txt')
money = int(f.readline().split()[1])
a = []
b = []
count_B = 0

for s in f.readlines():
    r = s.split()
    if r[2] == 'A':
        a.append([int(r[0]), int(r[1])])
    else:
        b.append([int(r[0]), int(r[1])])

b.sort()

for i in range(len(a)):
    while a[i][1] > 0:
        if money - a[i][0] > 0:
            money -= a[i][0]
            a[i][1] -= 1
        else:
            break
    else:
        continue
    break

for i in range(len(b)):
    while b[i][1] > 0:
        if money - b[i][0] > 0:
            money -= b[i][0]
            b[i][1] -= 1
            count_B += 1
        else:
            break
    else:
        continue
    break

print(count_B, money)
