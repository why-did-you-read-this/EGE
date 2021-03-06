# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1. Строится двоичная запись числа N.
# 2. Если N четное, то в конец полученной записи (справа) дописывается 0,
# в начало – 1; если N – нечётное в конец и начало дописывается по две единицы.
# 3. Результат переводится в десятичную систему и выводится на экран.
# Пример. Дано число N = 13. Алгоритм работает следующим образом:
# 1. Двоичная запись числа N: 1101.
# 2. Число нечетное, следовательно по две единицы по краям – 11110111.
# 3. На экран выводится число 247.
# Укажите наименьшее число, большее 52, которое может являться результатом работы автомата.
m = 999999999
for i in range(1000):
    n = i
    n_bin = bin(n)[2:]
    if n % 2 == 0:
        n_bin = '1' + n_bin + '0'
    else:
        n_bin = '11' + n_bin + '11'
    n = int(n_bin, 2)
    if n > 52:
        m = min(m, n)

print(m)

