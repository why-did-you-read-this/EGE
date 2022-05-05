f = list(map(int, open('17-4.txt').readlines()))
c = 0
maxF = 0
minF = 99999999999999999999999
for i in f:
    if (i % 13 == 7) and (i % 7 != 0) and (i % 11 != 0):
        c += 1
        maxF = max(maxF, i)
        minF = min(minF, i)

print(maxF - minF, c)
