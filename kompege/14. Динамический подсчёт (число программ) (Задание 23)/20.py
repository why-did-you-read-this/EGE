a = set()


def F(x, c=0):
    if c == 8:
        if 1000 <= x <= 1024:
            a.add(x)
    else:
        F(x + 1, c + 1)
        F(x + 5, c + 1)
        F(x * 3, c + 1)


F(1)
print(len(a))
