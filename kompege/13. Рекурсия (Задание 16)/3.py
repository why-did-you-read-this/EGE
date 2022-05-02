def F(n):
    if n <= 10:
        return n
    elif n <= 36:
        return n // 4 + F(n - 10)
    else:
        return 2 * F(n - 5)


print(F(100))
