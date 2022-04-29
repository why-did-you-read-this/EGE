for i in range(1000):
    x = i
    q = 7
    p = 10
    k1 = 0
    k2 = 0
    while x <= 100:
        k1 = k1 + 1
        x = x + p
    while x >= q:
        k2 = k2 + 1
        x = x - q
    l = x + k1
    m = x + k2
    if l == 11 and m == 20:
        print(i)
