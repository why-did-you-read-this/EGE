# c = 0
# def F(n):
#     global c
#     c += 1
#     if n >= 1:
#         c += 1
#         F(n - 1)
#         F(n - 3)
#         c += 1
#
# F(40)
# print(c)


def F(n):
    s = 1
    if n >= 1:
        s += 2 + F(n - 1) + F(n - 3)
    return s


print(F(40))