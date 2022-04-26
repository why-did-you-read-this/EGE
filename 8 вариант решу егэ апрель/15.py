p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
a = set(range(1000))


def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) or ((not Q) <= (not A))


for x in range(1000):
    if not f(x):
        a.remove(x)

print(len(a))
