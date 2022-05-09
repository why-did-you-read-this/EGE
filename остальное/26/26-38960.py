# https://inf-ege.sdamgia.ru/problem?id=38960
# Не верное решение

f = open('26-38960.txt')
money1 = int(f.readline().split()[1])
a = []
vse = []

for i in f.readlines():
    r = i.split()
    vse.append([int(r[0]), r[1]])
    if r[1] == 'A':
        a.append(int(r[0]))

vse.sort()
a.sort()


def F(x: list):
    s = 0
    for index in range(len(x)):
        s += x[index][0]
    return s


isp = []
money = money1

for i in vse:
    if money - i[0] > 0:
        if i[1] == 'A':
            a.pop(0)
        money -= i[0]
        isp += [i]

a_c = 0
tempB = ''
for i in range(len(isp)):
    if F(isp) < money1:
        if isp[i][1] == 'B':
            tempB = isp[i]
            isp[i] = [a[a_c], 'A']
            a_c += 1
    else:
        isp[i - 1] = tempB
        break

ostatok = money1 - F(isp)
count_A = 0
for i in isp:
    if i[1] == 'A':
        count_A += 1

print('↓ Ответ не верный ↓')
print(count_A, ostatok)
print('↑ Ответ не верный ↑')
