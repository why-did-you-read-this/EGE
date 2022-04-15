def F(number, base):
    if type(number) != int or number < 0:
        return 'Функция поддержитвает только целые, не отрицательные числа'
    if base < 2 or base > 36 or type(base) != int:
        return 'Основание СС должно быть целым числом и не может быть меньше 2 или больше 36'

    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_i = ''
    while number > 0:
        new_i += alphabet[number % base]
        number //= base
    return new_i[::-1]


n = int(input('Введите число которое хотите перевести в другую СС: '))
b = int(input('Введите основание СС: '))
print(F(n, b))
