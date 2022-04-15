# https://inf-ege.sdamgia.ru/problem?id=27850
otvet = []
otvet_index = []
c = 0
for i in range(245690, 245757):
    deliteli = []
    c += 1
    for d in range(2, int(i**0.5)+1):
        if len(deliteli) > 0:
            break
        if i % d == 0:
            deliteli += [d]
    if len(deliteli) == 0:
        otvet += [i]
        otvet_index += [c]

for i in range(len(otvet)):
    print(otvet_index[i], otvet[i])


