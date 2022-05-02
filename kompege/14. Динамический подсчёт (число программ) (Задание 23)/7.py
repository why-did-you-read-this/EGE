def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x + 1, y) + F(x * 2, y)


print(F(1, 12) * F(12, 30))
