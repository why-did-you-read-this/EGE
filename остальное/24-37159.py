# https://inf-ege.sdamgia.ru/problem?id=37159
f = open('24.txt').read()
s = f.replace('ad', 'a d').replace('da', 'd a')
a = list(map(len, s.split()))
print(max(a))
