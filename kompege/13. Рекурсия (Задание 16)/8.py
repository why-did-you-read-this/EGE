def C(n: float):
    return int(round(n - 0.5, 0))


def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        if n % 2 == 0:
            return C((n + F(n - 2)) / 5)
        else:
            return C((2 * n + F(n - 1) + F(n - 2)) / 4)


print(F(50))
