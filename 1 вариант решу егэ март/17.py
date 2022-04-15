# https://inf-ege.sdamgia.ru/problem?id=37337
f = open('17.txt').read().split()
max_ch = -1 * 10 ** 10
c = 0

for i in range(len(f)):
    for j in range(i + 1, len(f)):
        fi = int(f[i])
        fj = int(f[j])
        if (fi % 160 != fj % 160) and ((fi % 7 == 0) or (fj % 7 == 0)):
            c += 1
            max_ch = max(max_ch, fi + fj)
print(c, max_ch)
