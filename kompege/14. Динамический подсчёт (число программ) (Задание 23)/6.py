def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x + 1, y) + F(x * 2, y)


print(F(1, 10) * F(10, 20))
