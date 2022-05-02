def F(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return F(x - 8, y) + F(x // 2, y)


print(F(102, 43) * F(43, 5))
