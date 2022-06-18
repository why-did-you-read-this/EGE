def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x + 1, y) + F(x + 2, y) + F(x * 3, y)


print(F(2, 8) * F(8, 10) * F(10, 12))
