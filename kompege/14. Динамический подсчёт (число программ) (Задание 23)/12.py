def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x + 1, y) + F(x * 2, y) + F(x * 2 + 1, y) + F(x * 10, y)


print(F(1, 15))
