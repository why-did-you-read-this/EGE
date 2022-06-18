for i in range(1, 10000):
    n = bin(i)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    r = int(n, 2)
    if r > 43:
        print(r)
        break