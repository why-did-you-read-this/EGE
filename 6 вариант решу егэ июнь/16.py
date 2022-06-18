def F(n):
    if n > 0:
        G(n - 1)


def G(n):
    print("*")
    c += 1
    if n > 1:
        F(n - 3)


F(11)
