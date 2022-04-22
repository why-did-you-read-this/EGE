# https://inf-ege.sdamgia.ru/problem?id=33771
f = open('26-33771.txt')
# f = open('26-test.txt')
mem = int(f.readline().split()[1])
a = []
b = []
countA = 0
for i in f.readlines():
    price, c, t = i.split()
    if t == 'A':
        a.append([int(price), int(c)])
    if t == 'B':
        b.append([int(price), int(c)])

a.sort()
b.sort()

for i in b:
    if mem > 0:
        while i[1] > 0:
            if mem > 0:
                mem -= i[0]
                i[1] -= 1
            else:
                break
    else:
        if mem < 0:
            mem += i[0]
            i[1] += 1
        break

for i in a:
    while i[1] > 0:
        if mem > 0:
            mem -= i[0]
            i[1] -= 1
            countA += 1
        else:
            if mem < 0:
                mem += i[0]
                i[1] += 1
                countA -= 1
            break

print(countA, mem)
