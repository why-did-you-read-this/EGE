# https://inf-ege.sdamgia.ru/problem?id=38602
f = open('24-38602.txt').read()
while 'PP' in f:
    f = f.replace('PP', 'P P')
a = list(map(len, f.split()))
print(max(a))
