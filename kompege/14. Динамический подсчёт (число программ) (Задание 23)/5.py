def F(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x - 1, y) + F(x - 3, y) + F(x // 3, y)


print(F(22, 2))
