# https://inf-ege.sdamgia.ru/problem?id=29674
f = open('26-29674.txt')
f.readline()
a = sorted(list(map(int, f.readlines())))
stoimost = 0
for i in range(51):
    while i in a:
        stoimost += i
        a.remove(i)

mm = 0
while len(a) > 0:
    max_a = max(a)
    stoimost += max_a
    a.remove(max_a)
    if len(a) > 0:
        min_a = min(a)
        mm = min_a
        stoimost += min_a * 0.75
        a.remove(min_a)

print(round(stoimost + 0.5, 0), mm)
