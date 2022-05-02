a = set()


def F(x, c=0):
    if c == 15:
        a.add(x)
    else:
        F(x * 2, c + 1)
        F(x * 2 + 1, c + 1)


F(1)
print(len(a))
