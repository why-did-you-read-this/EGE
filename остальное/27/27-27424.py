f = open('27-B_demo.txt')
n = int(f.readline())
s = 0
minn = 10 ** 20
d = 0
for i in range(n):
    x, y = map(int, f.readline().split())
    s += max(x, y)
    d = abs(x - y)
    if d % 3 != 0:
        minn = min(d, minn)
if s % 3 != 0:
    print(s)
else:
    print(s - minn)
