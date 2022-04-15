# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [154026; 154043], числа,
# имеющие ровно 4 различных делителя. В ответе для каждого найденного числа запишите два его наибольших делителя в
# порядке возрастания.

def F(x: int):
    deliteli = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            deliteli += [i]
            k = x // i
            if x % k == 0:
                deliteli += [k]
                if i == k:
                    deliteli.remove(deliteli[-1])
    return sorted(deliteli)


for i in range(154026, 154043 + 1):
    f = F(i)
    if len(f) == 4:
        a = sorted([f[0], f[1], f[2], f [3]])
        print(a[2], a[3])
