# https://inf-ege.sdamgia.ru/problem?id=33104
# решает примерно за 62 секунды
def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for x in range(289123456, 389123456 + 1):
    # нечётное кол-во делителей только у квадратов
    if int(x ** 0.5) ** 2 == x:  # если число являестя квадратом целого числа
        d = div(x)
        if len(d) == 3:
            print(x, d[2])
