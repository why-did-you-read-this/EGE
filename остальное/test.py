a = set()
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {i for i in range(3, 31, 3)}
r = {i for i in range(12, 61, 12)}


def F(x):
    A = x in a
    P = x in p
    Q = x in q
    R = x in r
    return (not A) <= ((P and Q) <= R)


for x in range(1000):
    if not (F(x)):
        a.add(x)

print(a)
print(18*6)