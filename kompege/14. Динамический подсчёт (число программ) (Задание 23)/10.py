def F(x, y):
    if x > y or x == 6:
        return 0
    if x == y:
        return 1
    return F(x + 2, y) + F(x * 3, y)


print(F(1, 25) * F(25, 63))
