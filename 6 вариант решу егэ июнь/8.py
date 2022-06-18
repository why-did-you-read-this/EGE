from itertools import *

c = 0
for i in product('ЗИМА', repeat=5):
    s = ''.join(i)
    if s.count('И') + s.count('А') == 1:
        c += 1

print(c)