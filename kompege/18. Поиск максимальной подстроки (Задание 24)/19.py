f = open('24-19.txt').readline()
f1 = f
f = f.replace('DBAC', '*')
for i in 'ABCDEF':
    f = f.replace(i, ' ')
f = f.split()
m = str(max(f, key=len))
ms = 0
f1 = f1.replace(m.replace('*', 'DBAC'), '!')

if f1[f1.index('!') + 1] == 'D':
    ms = len(m) * 4 + 1
if (f1[f1.index('!') + 1] + f1[f1.index('!') + 2]) == 'DB':
    ms = len(m) * 4 + 2
if (f1[f1.index('!') + 1] + f1[f1.index('!') + 2] + f1[f1.index('!') + 3]) == 'DBA':
    ms = len(m) * 4 + 3

print(ms)
