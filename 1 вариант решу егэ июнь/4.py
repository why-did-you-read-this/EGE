for i in range(1, 10000):
    s = str(i)
    new_s = ''
    for j in s:
        binj = bin(int(j))[2:]
        while len(binj) < 4:
            binj = '0' + binj
        new_s += binj
        sum_s = 0
        for j in new_s:
            sum_s += int(j)
        new_s += str(sum_s % 2)
    if new_s == '01100010100100100110':
        print(i)
        break
