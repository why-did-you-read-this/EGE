g1 = []  # чётные
g2 = []  # нечётные
g3 = []
f = open('27-A.txt')
f.readline()
a = []
for i in f:
    a += [i.rstrip()]
for s in a:
    ss = [int(j) for j in s.split()]
    ss = sorted(ss)
    g3.append(min(ss))
    ss.remove(min(ss))
    g1.append(max(ss))
    ss.remove(max(ss))
    g2.append(ss[0])

print(sum(g1))
print(sum(g2))
print(sum(g3))
