def F(x):
    for i in range(18, x - 1, 10):
        if x % i == 0:
            return True


c = 0
for i in range(500_001, 50000000):
    if c >= 5:
        break
    elif F(i):
        c += 1
        print(i)