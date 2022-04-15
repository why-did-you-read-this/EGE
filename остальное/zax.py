# Вариант 9325895


# №2
# print('x y z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if ((not z) and x) == 0:
#                 print(x, y, z, 0)
#             else:
#                 print(x, y, z, 1)

# № 5
# q = set()
# for i in range(10, 1001):
#     a = i
#     str = bin(a)
#     str = str[2:]
#     first_1 = str.find('1')
#     while str[first_1 + 1] == '0':
#         str = str[:first_1 + 1] + str[first_1 + 2:]
#         if (len(str) == 1):
#             break
#     str = str[:first_1] + str[first_1 + 1:]
#     if (str == ''):
#         str = '0'
#     str = int(str, 2)
#     s = a - str
#     q.add(s)
# print(len(q))

# № 2 15970
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and (not y)) or (y == z) or w) == 0:
#                     print(x, y, z, w)

# def F(x):
#     if x == 1:
#         return 1
#     if x == 2:
#         return 3
#     if x > 2:
#         return F(x-1) * x + F(x-2) * (x-1)
#
#
# print(F(5))


# № 17 37347
# f = open('17-1.txt')
# q = f.read().split()
#
# maxs = -100000000
# c = 0
# for x1 in range(len(q)):
#     for x2 in range(x1 + 1, len(q)):
#         if ((int(q[x1]) * int(q[x2])) % 14) != 0:
#             c += 1
#             if (int(q[x1]) + int(q[x2])) > maxs:
#                 maxs = (int(q[x1]) + int(q[x2]))
# print(c, maxs)


# for x in range(101, 10000):
#     L = x - 30
#     M = x + 30
#     while L != M:
#         if L > M:
#             L = L - M
#         else:
#             M = M - L
#     if M == 60:
#         print(x)
#         break


# 23 https://inf-ege.sdamgia.ru/problem?id=15638
# def F(x, y):
#     if x > y:
#         return 0
#     elif x == y:
#         return 1
#     elif x == 17:
#         return 0
#     elif x < y:
#         return F(x + 1, y) + F(x * 2, y)
#
#
# print(F(1, 10) * F(10, 21))

# 20. Поиск делителей (Задание 25) https://inf-ege.sdamgia.ru/problem?id=27692
# f = 'ABBBAABABBBBABBBBBB'
# # f = open('20. Поиск делителей (Задание 25).txt').read()
# c = 0
# maxc = 0
# for i in range(len(f) - 1):
#     a = f[i] == 'B' and f[i + 1] == 'B'
#     if a:
#         c += 1
#     if (not a) or (f[i + 1] == 'B' and i + 1 == len(f) - 1):
#         c += 1
#         if c > maxc:
#             maxc = c
#         c = 0
# print(maxc)


# 15 https://inf-ege.sdamgia.ru/problem?id=14277
# P = [i / 10 for i in range(170, 400 + 1)]
# Q = [i / 10 for i in range(200, 570 + 1)]
# A1 = set()
#
#
# def F(x, A):
#     return (not (x in A)) <= (((x in P) and (x in Q)) <= (x in A))
#
#
# for x in set([i / 10 for i in range(10, 1001)]):
#     if not F(x, A1):
#         A1.add(x)
#
# print(sorted(A1))


# 20. Поиск делителей (Задание 25) https://inf-ege.sdamgia.ru/problem?id=28124\
# min_i = 9999999
# max_c = -9999999
# for i in range(568023, 569231):
#     c = 0
#     for j in range(1, 569231):
#         if i % j == 0:
#             c += 1
#     if c > max_c:
#         max_c = c
#         print(i, c)


# 26 https://inf-ege.sdamgia.ru/problem?id=28138
# f = open('28138.txt')
# mem = int(f.readline().split(' ')[0])
# c = 0
# a = [int(i) for i in f]
# a.sort()
# max_i = 0
# for i in a:
#     if mem - i >= 0:
#         mem -= i
#         c += 1
#         max_i = i
#
# mem += max_i
# max_j = 0
# for j in range(mem, max_i, -1):
#     if j in a:
#         if mem - j >= 0:
#             if j > max_j:
#                 max_j = j
#                 mem -= j
# print(c, max_j)


# 27 https://inf-ege.sdamgia.ru/problem?id=35916
# f1 = [int(i) for i in open('27-A.txt').read().split()]
# f1.pop(0)
# f2 = [int(i) for i in open('27-B.txt').read().split()]
# f2.pop(0)
# f1.sort()
# f2.sort()
#
# flag = 0
# for i in range(len(f1)):
#     if flag == 0:
#         for j in range(i + 1, len(f1)):
#             if flag == 0:
#                 for x in range(j + 1, len(f1)):
#                     if flag == 0:
#                         if (f1[i] + f1[j] + f1[x]) % 3 == 0:
#                             print((f1[i] + f1[j] + f1[x]))
#                             flag = 1
# flag = 0
# for i in range(len(f2)):
#     if flag == 0:
#         for j in range(i + 1, len(f2)):
#             if flag == 0:
#                 for x in range(j + 1, len(f2)):
#                     if flag == 0:
#                         if (f2[i] + f2[j] + f2[x]) % 3 == 0:
#                             print((f2[i] + f2[j] + f2[x]))
#                             flag = 1

# 5 https://inf-ege.sdamgia.ru/problem?id=10468

# for n in range(101):
#     a = n
#     n = bin(n)
#     # n = n[::-1]
#     n = n[2:]
#     # n = n[::-1]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     if int(n, 2) > 77:
#         print(a)

# 5 задание
# a = 21
# print(a % 4, a % 3, a % 2)
#
# for i in range(10, 100):
#     s = ''
#     s += str(i % 4)
#     s += str(i % 3)
#     s += str(i % 2)
#     if s == '101':
#         print(i)


# 11 задание
# i = 5
# lc = 5*13
# c = 7 * 2
# print((lc + c) / 8)


# 12 задание
# s = '9' * 127
# while ('333' in s) or ('999' in s):
#     if '333' in s:
#         s = s.replace('333', '9', 1)
#     else:
#         s = s.replace('999', '3', 1)
#     print(s)
# print()
# print(s)


# 14 задание
# i = 36**7 + 6**19 - 18
# ost = ''
# while i > 0:
#     ost = str(i % 6) + ost
#     i = i // 6
# print(ost)
# print(ost.count('0'))


# 17
# f = open('17.txt')
# a = []
# c = 0
# maxr = -9999999
# for s in f:
#     a.append(int(s.strip()))
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if ((a[i] - a[j]) % 60 == 0) and ((a[i] % 15 == 0) or (a[j] % 15 == 0)):
#             c += 1
#             if (a[i] - a[j]) > maxr:
#                 maxr = a[i] - a[j]
#
# print(c, maxr)


# 22
# for x in range(1000):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         if x % 2 > 0:
#             a += 1
#         else:
#             b += x % 6
#         x = x // 6
#     # print(a, b)
#     if a == 2 and b == 8:
#         print(i)


# 20. Поиск делителей (Задание 25)
# def F(x, end):
#     if x > end:
#         return 0
#     if x == end:
#         return 1
#     if x == 5 or x == 10:
#         return 0
#     return F(x + 1, end) + F(x * 2, end) + F(x + 3, end)
#
#
# print(F(2, 14))


# 20. Поиск делителей (Задание 25)
# f = open('20. Поиск делителей (Задание 25).txt').read().split()
# c = 0
# for i in f:
#     if i.count('A') > i.count('E'):
#         c+=1
# print(c)


# 20. Поиск делителей (Задание 25)
# c = 0
# for i in range(700001, 800000):
#     minDel = 0
#     maxDel = 0
#     if c >= 5:
#         break
#     for a in range(2, int(round(i / 2, 0))):
#         if i % a == 0:
#             minDel = a
#             break
#     for a in range(int(round(i / 2, 0)), 2, -1):
#         if i % a == 0:
#             maxDel = a
#             break
#     m = minDel + maxDel
#     if str(m)[-1::] == '8':
#         c += 1
#         print(i, m)


# 26
# f = open('26.txt')
# f.readline()
# a = []
# c = 0
# maxSum = -999999
# for i in f:
#     a.append(int(i.strip()))
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (a[i] % 2) == (a[j] % 2):
#             if (a[i] + a[j]) in a:
#                 c += 1
#                 if maxSum < (a[i] + a[j]):
#                     maxSum = a[i] + a[j]
#                 print(c, maxSum)
# print()
# print(c, maxSum)

# ss = 3
# num = 4
# def perevod(num, ss):
#     ost = ''
#
#     while num > 0:
#         ost = str(num % ss) + ost
#         num = num // ss
#     return ost[-1]
# for i in range(1, 100):
#     if perevod(i, 3) == perevod(i, 5) == '0':
#         print(i)

# def F(n):
#     u = n
#     n3 = 0
#     while u > 0:
#         n3 += u % 3
#         u = u // 3
#     print(n3)
# print(F(3))


# 18
# a= []
# f = open('17.txt').read().split()
# a.append(float(f[0]))
# maxSum = 0
# for i in range(len(f) - 1):
#     if float(f[i]) > float(f[i+1]):
#         a.append(float(f[i + 1]))
#
#     else:
#         if maxSum < sum(a):
#             maxSum = sum(a)
#         a.clear()
#         a.append(float(f[i+1]))
#
# print(maxSum)

# 7
# v = (90 * 48000 * 16 * 2) / 32000
# print(v)

# 7
# v = 10 * 1024 * 1024 * 8
# t1 = v / (2 ** 18)
# t2 = ((v * 0.3) / (2 ** 18)) + 8
# print(t1, t2)
# print(t1 - t2)


# 9 вариант
# https://inf-ege.sdamgia.ru/test?id=9524276


# 15 https://inf-ege.sdamgia.ru/problem?id=18087
# for a in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not ((y + 2*x < a) or (x > 15) or (y > 30)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(a)


# 15 https://inf-ege.sdamgia.ru/problem?id=14704
# c = 0
# for a in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not (((x < 6) <= ((x * x) < a)) and ((y * y) <= a) <= (y <= 6)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(a)
#         c += 1
# print()
# print(c)


# 15 https://inf-ege.sdamgia.ru/problem?id=15803
# for a1 in range(-100, 101):
#     for a2 in range(-100, 101):
#         for x in range(-100, 101):
#             for y in range(-100, 101):
#                 if not (((a1 <= x <= a2) <= ((x ** 2) <= 100)) and (((x ** 2) <= 64) <= (a1 <= x <= a2))):
#                     break
#             else:
#                 continue
#             break
#         else:
#             print(a2 - a1)

# 15 https://inf-ege.sdamgia.ru/problem?id=16045
# for a in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not(((y + 2 * x) != 48) or (a < x) or (a < y)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(a)


# 15 https://inf-ege.sdamgia.ru/problem?id=9804
# for a in range(1, 1000):
#     for x in range(1, 1000):
#         if not (((x & 29) != 0) <= (((x & 17) == 0) <= ((x & a) != 0))):
#             break
#     else:
#         print(a)

# 15 https://inf-ege.sdamgia.ru/problem?id=34534
# w = []
# p = [i for i in range(2, 11)]
# q = [i for i in range(6, 15)]
# for a1 in range(-20, 21):
#     for a2 in range(-20, 21):
#         for x in range(-20, 21):
#             if not(((a1 <= x <= a2) <= (x in p)) or (x in q)):
#                 break
#         else:
#             if (a2 - a1) > 0:
#                 w.append(a2 - a1)
# print(w)
# print()
# print(max(w))

# 15 https://inf-ege.sdamgia.ru/problem?id=34538
# НЕ РАБОТАЕТ !!! \/
# w = []
# p = [i for i in range(30, 46)]
# q = [i for i in range(40, 56)]
# for a1 in range(-80, 81):
#     for a2 in range(-80, 81):
#         for x in range(-80, 81):
#             if not (((not (a1 <= x <= a2)) <= (not (x in p))) and ((x in q) <= (a1 <= x <= a2))):
#                 break
#         else:
#             if (a2 - a1) > 0:
#                 w.append(a2 - a1)
# print(min(w))
# НЕ РАБОТАЕТ !!! /\

# 15 https://inf-ege.sdamgia.ru/problem?id=7929
# НЕ РАБОТАЕТ !!! \/
# w = []
# p = {i for i in range(2, 21, 2)}
# q = {i for i in range(3, 31, 3)}
# for a1 in range(-50, 51):
#     for a2 in range(-50, 51):
#         for x in range(-50, 51):
#             # if not (((a1 <= x <= a2) <= (x in p)) and ((x in q) <= (not (a1 <= x <= a2)))):
#             if ((a1 <= x <= a2) and ((not(x in p)) or (x in q))):
#                 break
#         else:
#             # if (a2 - a1) > 0:
#             w.append(a2 - a1)
# print(min(w))
# НЕ РАБОТАЕТ !!! /\
