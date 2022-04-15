def F(x, y):
    if x > y or x == 24:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F((x * 2) + 1, y)


print(F(1, 25))
