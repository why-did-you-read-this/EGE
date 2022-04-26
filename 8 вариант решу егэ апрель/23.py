def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 2, y) + F(x * 5, y)


print(F(2, 50))
