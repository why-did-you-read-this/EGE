# https://inf-ege.sdamgia.ru/problem?id=27423
f = open('26-27423.txt')
mem = int(f.readline().split()[0])
a = sorted(list(map(int, f.readlines())))
c = 0
maxF = 0
for i in a:
    if mem - i > 0:
        mem -= i
        c += 1
    else:
        mem += a[c-1]
        break

for i in a[::-1]:
    if mem - i >= 0:
       maxF = i
       break

print(c, maxF)
