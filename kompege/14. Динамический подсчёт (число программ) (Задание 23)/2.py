def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 1, y) + F(x * 2, y) + F(x ** 2, y)


print(F(5, 154))
