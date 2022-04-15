# https://inf-ege.sdamgia.ru/problem?id=27699
f = open('24-27699.txt').read()
s = 'LDR'
while s in f:
    s += s[len(s) % 3]
s = s[:-1]
print(len(s))
