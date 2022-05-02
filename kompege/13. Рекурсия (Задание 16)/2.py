def F(n):
    if n <= 3:
        return n
    else:
        if n % 3 == 0:
            return n ** 3 + F(n - 1)
        elif n % 3 == 1:
            return 4 + F(n // 3)
        else:
            return n ** 2 + F(n - 2)


print(F(100))
