# https://inf-ege.sdamgia.ru/problem?id=10282
for i in range(10000, 100000):
    s = str(i)
    i_1 = int(s[0]) + int(s[2]) + int(s[4])
    i_2 = int(s[1]) + int(s[3])
    new_i = int(str(min(i_1, i_2)) + str(max(i_1, i_2)))
    if new_i == 723:
        print(i)
