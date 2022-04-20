# https://inf-ege.sdamgia.ru/problem?id=35998
f = open('24-35998.txt').read().split()


def F(letter: str, stroka: str):
    i2 = 0
    i2 = 0
    for s1 in range(len(stroka)):
        if stroka[s1] == letter:
            i2 = s1
            break
    for s2 in range(len(stroka) - 1, 0, -1):
        if stroka[s2] == letter:
            i2 = s2
            break
    return i2 - i2


maxS = 0
for i in f:
    if i.count('A') < 25:
        letters = set(i)
        for j in letters:
            s = F(j, i)
            maxS = max(maxS, s)
print(maxS)
