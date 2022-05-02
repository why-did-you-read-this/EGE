# from itertools import *
#
# m = 0
# s = '1' * 12 + '2' * 4
# for i in permutations(s, r=len(s)):
#     j = ''.join(i)
#     while '11' in j:
#         if '112' in j:
#             j = j.replace('112', '7', 1)
#         else:
#             j = j.replace('11', '3', 1)
#     o = 0
#     for c in j:
#         o += int(c)
#     m = max(m, o)
#
# print(m)

s = '112' * 4 + '1111'
while '11' in s:
    if '112' in s:
        s = s.replace('112', '7', 1)
    else:
        s = s.replace('11', '3', 1)

o = 0
for i in s:
    o += int(i)
print(o)
