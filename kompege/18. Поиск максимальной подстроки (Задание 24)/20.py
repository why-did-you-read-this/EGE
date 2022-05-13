f = open('24-20.txt').readline()
f1 = f
f = f.replace('XYZ', '*').replace('X', ' ').replace('Y', ' ').replace('Z', '')
f = f.split()
m = max(f, key=len)
m = m.replace('*', 'XYZ')
ms = len(m)
for i in 'XYZ':
    if ((i + m) in f1) or ((m + i) in f1):
        ms = len(m) + 1
    for j in 'XYZ':
        if (i + m + j) in f1:
            ms = len(m) + 2

print(ms)
