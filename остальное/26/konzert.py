f = open('26-37161.txt')
n = int(f.readline())
data = f.readlines()
mesta = []
for i in data:
    mesta.append((list(map(int, i.split()))))
mesta.sort(reverse=True)

max_r = 0
min_m = 99999999999999999

for m in mesta:
    if (not ([m[0], m[1] + 1] in mesta)) and (not ([m[0], m[1] + 2] in mesta)) and ([m[0], m[1] + 3] in mesta):
        max_r = m[0]
        min_m = m[1] + 1
        break

# for m in mesta:
#     if (m[0] == max_r) and (not ([m[0], m[1] + 1] in mesta)):
#         min_m = min(min_m, m[1] + 1)

print(max_r, min_m)
