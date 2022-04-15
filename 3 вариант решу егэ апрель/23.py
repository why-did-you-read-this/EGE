def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 2, y) + F(x + (x - 1), y)


print(F(2, 9))
