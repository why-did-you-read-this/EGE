def F(x, y):
    if x > y or x == 43:
        return 0
    if x == y:
        return 1
    return F(x + 2, y) + F(2 * x - 1, y) + F(2 * x + 1, y)


print(F(7, 63))
