# https://inf-ege.sdamgia.ru/problem?id=18550
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # if (((y <= z) or ((not x) and w)) == (w == z)) == 1:
                if (((y <= z) or ((not z) and w)) == (w == z)) == 1:
                    print(x, y, z, w)
