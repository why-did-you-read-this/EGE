# https://inf-ege.sdamgia.ru/problem?id=37161

# f = open('26-37161.txt')
f = open('26-test.txt')
f.readline()
a = []
maxR = 0
minM = 0
for s in f.read().split('\n'):
    a += [[int(s.split()[0]), int(s.split()[1])]]
a = sorted(a)

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i][0] == a[j][0]:
            if a[j][1] - a[i][1] == 3:
























# f = open('26-37161.txt')
# n = int(f.readline())
# nums = []
# for _ in range(n):
#     pair = list(map(int, f.readline().split()))
#     pair[1] = -pair[1]
#     nums += [pair]
# nums.sort()
# r, m = 0, 0
# for i in range(1, len(nums)):
#     if nums[i][0] == nums[i-1][0]:
#         if nums[i][1] - nums[i-1][1] == 3:
#             r = nums[i][0]
#             m = -nums[i][1] + 1
#
# print(r, m)
