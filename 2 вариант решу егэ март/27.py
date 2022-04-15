f = open('27-A.txt')
f.readline()
a = []
group1 = []  # чётные
group2 = []  # нечётные
group3 = []

for i in f:
    ss = i.split()
    try:
        a.append([int(ss[j]) for j in range(3)])
    except None:
        pass

for i in range(len(a)):
    group3.append(max(a[i]))
    a[i].remove(max(a[i]))
    group1.append(a[i][0])
    group2.append(a[i][1])

print(sum(group1))
print(sum(group2))
print(sum(group3))
