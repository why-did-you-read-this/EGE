def F(x, a):
    return ((x % 2 == 0) <= (not (x % 5 == 0))) or ((x + a) >= 90)


for a in range(1, 1000):
    if all(F(x, a) == 1 for x in range(1, 100000)):
        print(a)
        break
