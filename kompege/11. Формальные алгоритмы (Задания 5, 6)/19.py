# m = set()
# for i in range(1000):
#     d = i
#     n = 20
#     s = 40
#     while s + n < d:
#         s -= 10
#         n -= 20
#     if n > 0:
#         m.add(i)
#
# print(len(m))


d = int(input())
n = 20
s = 40
while s + n < d:
    s -= 10
    n -= 20
print(n)