# https://inf-ege.sdamgia.ru/problem?id=45259
for i in range(10):
    for j in range(10):
        s = int('12345' + str(i) + '7' + str(j) + '8')
        if s % 23 == 0:
            print(s, s / 23)
