def F(x, y):
    def G(u):
        u = str(u)
        new_u = ''
        for i in u:
            i = int(i)
            if i < 9:
                new_u += str(i + 1)
            else:
                new_u += '9'
        return int(new_u)

    if x > y:
        return 0
    if x == y:
        return 1
    return F(x + 1, y) + F(G(x), y)


print(F(25, 51))
