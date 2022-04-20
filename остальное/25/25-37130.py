# https://inf-ege.sdamgia.ru/problem?id=37130
otvet = []
otvetdel = []
c = 0
for i in range(600000, 10**20):
    if c >= 5:
        break
    for d in range(17, i - 1 + 1, 10):
        if i % d == 0:
            c += 1
            print(i,d)
            break
            