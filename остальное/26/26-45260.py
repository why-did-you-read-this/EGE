f = open('26-45260.txt')
# f = open('26-test.txt')
n = int(f.readline())
data = f.readlines()
mesta = []
for i in data:
    mesta.append((list(map(int, i.split()))))
mesta.sort(reverse=True)
print(mesta[0])
max_r = 0
min_m = 99999999999999999
flag = 0

for m in mesta:
    print(m[0])
    for i in range(1, 14):
        if [m[0], m[1] + i] in mesta:
            break
    else:
        if [m[0], m[1] + 14] in mesta:
            min_m = m[1] + 1
            max_r = m[0]
            print(max_r)
            break

# for m in mesta:
#     if (m[0] == max_r) and (not ([m[0], m[1] + 1] in mesta)):
#         min_m = min(min_m, m[1] + 1)
#         print(min_m)

print(' ')
print(max_r, min_m)
