# https://inf-ege.sdamgia.ru/problem?id=36880
d2 = []
d3 = []
d23 = []
for i in range(0, 600_000_000, 2):
    if 2**i <= 600_000_000:
        d2 += [2**i]
    if 2**i > 600_000_000:
        break

for u in range(1, 600_000_000, 2):
    if 3**u <= 600_000_000:
        d3 += [3**u]
    if 3**u > 600_000_000:
        break


for j in d2:
    for k in d3:
        if 400_000_000 <= j*k <= 600_000_000:
            d23 += [j * k]

d23 = sorted(d23)
print(d23)

