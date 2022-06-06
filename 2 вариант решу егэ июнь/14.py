def p(x, ss):
    new_x = ''
    alph = sorted('0123456789QWERTYUIOPLKJHGFDSAZXCVBNM')
    while x > 0:
        new_x += alph[x % ss]
        x //= ss
    new_x = new_x[::-1]
    return new_x


for i in range(1, 1000):
    if (len(p(i, 6)) == 2) and (len(p(i, 5)) == 3) and (p(i, 11)[-1] == '1'):
        print(i)
