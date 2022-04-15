f = open('27_A.txt')
n = int(f.readline())
a = [int(i) for i in f]
ms = float('-inf')
ml = 0
for i in range(n):
    s = []
    for j in range(i, n):
        s += [a[j]]
        if sum(s) % 43 == 0:
            if sum(s) > ms:
                ms = sum(s)
                ml = len(s)
print(ml)
print(-330%25)