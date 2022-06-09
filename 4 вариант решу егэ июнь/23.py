def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 3, y)


print(F(1, 9) * F(9, 17))
