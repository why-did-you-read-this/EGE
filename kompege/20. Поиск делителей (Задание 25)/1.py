# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457; 174505], числа,
# имеющие ровно два различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа
# запишите эти два делителя в таблицу на экране с новой строки в порядке возрастания произведения этих двух
# делителей. Делители в строке таблицы также должны следовать в порядке возрастания.

def F(x: int):
    deliteli = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            deliteli += [i]
            k = x // i
            if x % k == 0:
                deliteli += [k]
                if i == k:
                    deliteli.remove(deliteli[-1])
    return sorted(deliteli)


for i in range(174457, 174505 + 1):
    f = F(i)
    if len(f) == 2:
        print(f[0], f[1], f[0] * f[1])
