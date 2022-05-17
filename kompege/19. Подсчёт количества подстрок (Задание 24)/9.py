f = list(map(str.strip, open('24-9.txt')))
c = 0
for i in f:
    if i.count('S') == i.count('X'):
        c += 1

print(c)
