# s = '9' * 100 + '2' * 48 + '1' * 14
s = '9992' * 33 + '2' * 15 + '1' * 14 + '9'

while ('999' in s) or ('22' in s):
    if '999' in s:
        s = s.replace('999', '12', 1)
    else:
        s = s.replace('22', '1', 1)

print(s.count('1'))
