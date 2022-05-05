f = list(map(int, open('17-10.txt').readlines()))
c = 0
s = 0


def p(x, ss):
    new_x = ''
    while x > 0:
        new_x += str(x % ss)
        x //= ss
    return new_x[::-1]


for i in range(len(f) - 2):
    i1 = f[i]
    i2 = f[i + 1]
    i3 = f[i + 2]
    if p(i1, 3)[-1] == '2' or p(i2, 3)[-1] == '2' or p(i3, 3)[-1] == '2':
        c += 1
        s += min(i1, i2, i3)

print(c, s)
