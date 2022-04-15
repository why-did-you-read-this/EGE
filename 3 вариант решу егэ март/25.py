arr2 = []  # чётные
arr3 = []  # нечётные
arr23 = []

i = 0
while 2 ** i <= 400_000_000:
    arr2 += [2 ** i]
    i += 2
i = 1
while 3 ** i <= 400_000_000:
    arr3 += [3 ** i]
    i += 2

for i2 in range(len(arr2)):
    for i3 in range(len(arr3)):
        chislo = arr2[i2] * arr3[i3]
        if 200_000_000 <= chislo <= 400_000_000:
            arr23 += [chislo]

print(sorted(arr23))
