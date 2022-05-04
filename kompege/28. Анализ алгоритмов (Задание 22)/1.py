for i in range(1, 100000000):
    x = i
    a = 0
    b = 0
    while x > 0:
        a += 1
        if x % 11 > b:
            b = x % 11
        x = x // 11
    if a == 7 and b == 7:
        print(i)
        break
