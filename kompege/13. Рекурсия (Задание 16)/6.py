def F(n):
    if n <= 1:
        return 1
    else:
        if n % 2 == 0:
            return 3 * n + F(n - 1)
        else:
            return 2 * F(n - 2)


print(F(31))
