def F(x, y):
    if x > y or x == 11 or x == 18:
        return 0
    if x == y:
        return 1
    return F(x + 1, y) + F(x + 2, y) + F(x * 3, y)


print(F(4, 8) * F(8, 23))
