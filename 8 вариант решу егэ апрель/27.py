f = open('27-A.txt')
f.readline()
a = []
for i in f.read().split('\n'):
    ii = i.split()
    if len(ii) > 0:
        a += [[int(ii[0]), int(ii[1])]]



