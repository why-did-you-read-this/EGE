m = 10**20
for i in range(10001):
    s = i
    n = 100
    while s - n >= 100:
        s += 20
        n += 40
    if s != i:
        m = min(m, i)

print(m)

# s = int(input())
# n = 1000
# while s - n >= 100:
#     s += 20
#     n += 40
# print(s)
