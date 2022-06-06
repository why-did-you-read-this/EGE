from itertools import *

c = 0

for i in permutations('МАТВЕЙ', r=6):
    s = ''.join(i)
    if (s[0] != 'Й') and (not ('АЕ' in s)):
        c += 1
print(c)
