def F(n):
    if n <= 3:
        return 3
    else:
        if n % 2 == 0:
            return F(n // 2) + 5
        else:
            return F(n - 1) - F(n - 2)


print(F(20))
