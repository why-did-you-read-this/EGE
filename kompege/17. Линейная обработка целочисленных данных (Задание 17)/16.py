f = list(map(int, open('17-16.txt').readlines()))
c11 = 0
c17 = 0
maxF = float('-inf')
minF = float('inf')

for i in f:
    if i % 11 == 0:
        c11 += 1
        minF = min(minF, i)
    if i % 17 == 0:
        c17 += 1
        maxF = max(maxF, i)

if c11 > c17:
    print(c11, minF)
else:
    print(c17, maxF)
