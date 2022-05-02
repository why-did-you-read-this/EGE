s_end = '1' * 28 + '2' * 34 + '3' * 45
a = []
for x in range(100):
    for y in range(100):
        for z in range(100):
            s = '0' + '1' * x + '2' * y + '3' * z
            s1 = s
            while ('01' in s) or ('02' in s) or ('03' in s):
                s = s.replace('01', '302', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '20', 1)
            if (s.count('1') == s_end.count('1')) \
                    and (s.count('2') == s_end.count('2')) \
                    and (s.count('3') == s_end.count('3')):
                print(s1.count('1'))
                break
        else:
            continue
        break
    else:
        continue
    break
