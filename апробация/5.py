for i in range(10000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'
    r = int(n, 2)
    if r >= 19:
        print(i)
        break
