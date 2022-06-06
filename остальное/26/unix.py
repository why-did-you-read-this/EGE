f = open('26.txt')
n = int(f.readline())
unix_list = f.readlines()
L = []

for i in range(n):
    st, en = map(int, unix_list[i].split())
    L.append((st, 1))
    if en == 0:
        en = 2000000000
    L.append((en, -1))
L.sort()
mxk = dt = k = 0
w0 = 1634515200
w1 = w0 + 7 * 24 * 3600

for t, dk in L:
    k += dk
    if w0 < t < w1:
        if k > mxk:
            mxk, dt = k, 0
        if k - dk == mxk:
            dt += t - t0
    t0 = t
print(mxk, dt)
