f = list(map(int, open('17-3.txt').readlines()))

c = 0
maxF = 0
minF = 99999999999999999999999

for i in f:
    if (str(i)[-1] == '5' or str(i)[-1] == '7') and (i % 9 != 0) and (i % 11 != 0):
        c += 1
        maxF = max(i, maxF)
        minF = min(i, minF)

print(c, maxF + minF)
