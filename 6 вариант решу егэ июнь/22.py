for j in range(10000):
    q = 0
    n = j
    for i in range(1, n):
        if n % i == 0:
            q = i
    if q == 17:
        print(j)
        break
