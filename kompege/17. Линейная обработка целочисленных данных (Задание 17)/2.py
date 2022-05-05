f = list(map(int, open('17-2.txt').read().split()))
c = 0
m = 99999999999999999
for i in f:
    if (str(i)[-1] == '2' or str(i)[-1] == '7') and (i % 3 == 0) and (i % 11 == 0):
        c += 1
        m = min(m, i)

print(c, m)
