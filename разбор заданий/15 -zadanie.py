# # наименьшую возможную длину такого отрезка A
# # задание из демоверсии
# D = [i / 10 for i in range(170, 580 + 1)]
# C = [i / 10 for i in range(290, 800 + 1)]
# A1 = set()
#
#
# def F1(x, A):
#     return (x in D) <= ((not (x in C) and not (x in A)) <= (not (x in D)))
#
#
# for x in set([i / 10 for i in range(10, 1001)]):
#     if not F1(x, A1):
#         A1.add(x)
#
# print(sorted(A1))
#
#
# # наибольшую возможную длину такого отрезка A
# # https://inf-ege.sdamgia.ru/problem?id=34534
#
# P = [i / 10 for i in range(20, 100 + 1)]
# Q = [i / 10 for i in range(60, 140 + 1)]
# A2 = [i / 10 for i in range(10, 200 + 1)]
#
#
# def F2(x, A):
#     return ((x in A) <= (x in P)) or (x in Q)
#
#
# for x in [i / 10 for i in range(10, 1001)]:
#     if not F2(x, A2):
#         A2.remove(x)
#
# print(sorted(A2))
# # print(int(len(A2) - 2)/10)

# https://inf-ege.sdamgia.ru/problem?id=15986
# for a in range(1, 100):
#     for x in range(1, 100):
#         for y in range(1, 100):
#             if not (((y + 2 * x) != 48) or (a < x) or (x < y)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(a)


# на множества https://www.youtube.com/watch?v=amxHbTyRZhc

def F(x):
    P = x in {i for i in range(2, 21, 2)}
    Q = x in {i for i in range(5, 51, 5)}
    A = x in a
    return (A <= P) and (Q <= (not A))


a = set(range(1000))
for x in range(1000):
    if F(x) == 0:
        a.remove(x)
print(len(a))
