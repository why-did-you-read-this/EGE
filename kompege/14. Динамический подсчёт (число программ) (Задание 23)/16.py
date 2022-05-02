def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x % 2 == 0:
        return F(x + 1, y) + F(x * 1.5, y)
    else:
        return F(x + 1, y)


print(F(1, 20))
