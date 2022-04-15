f = open('17.txt').read().split()
c = 0
maxSum = 0
for i in range(len(f) - 1):
    fi = int(f[i])
    fii = int(f[i+1])
    if fi % 3 == 0 or fii % 3 == 0:
        c += 1
        maxSum = max(maxSum, fi + fii)
print(c, maxSum)