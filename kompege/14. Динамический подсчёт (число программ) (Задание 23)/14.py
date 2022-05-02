def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x + 1, y) + F(int(bin(x)[2:] + '0', 2), y) + F(int(bin(x)[2:] + '1', 2), y)


print(F(int('100', 2), int('11101', 2)))
