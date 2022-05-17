f = open('24-10.txt')
f = [str.strip(i) for i in f.readlines()]
c = 0
for i in f:
    b = i.count('B')
    a = i.count('A')
    if (b / a) >= 1.05:
        c += 1
print(c)
