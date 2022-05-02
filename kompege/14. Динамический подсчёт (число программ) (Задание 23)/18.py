def F(x, y, c=0):
    if x > y:
        return 0
    if x == y and c != 7:
        return 0
    if x == y and c == 7:
        return 1
    return F(x + 1, y, c + 1) + F(x + 4, y, c + 1) + F(x * 2, y, c + 1)


print(F(3, 27, 0))
