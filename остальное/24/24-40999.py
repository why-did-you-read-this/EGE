# https://inf-ege.sdamgia.ru/problem?id=40999
def F(x: str):
    if x.count('A') >= 3:
        return len(x)
    return 0


f = open('24.txt').readline()
s = f.replace('E', ' ').split()
a = list(map(F, s))
print(max(a))
