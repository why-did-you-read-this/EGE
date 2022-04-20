# https://inf-ege.sdamgia.ru/problem?id=29672
f = open('inf_22_10_20_24.txt').read().split()
c = 0
for i in f:
    if i.count('E') > i.count('A'):
        c+=1
print(c)
