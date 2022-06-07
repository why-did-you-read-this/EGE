f = open('27-B_1.txt')
n = int(f.readline())
s = 0
minn = 20001
d = 0
for i in range(n):
    x, y = map(int, f.readline().split())
    s += max(x, y)
    d = abs(x - y)
    if d % 5 != 0:
        minn = min(d, minn)
if s % 5 != 0:
    print(s)
else:
    print(s - minn)
