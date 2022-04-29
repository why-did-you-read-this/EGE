from itertools import *

c = 0
for i in product('ЕЛНОСЦ', repeat=5):
    s = ''.join(i)
    c += 1
    if s.count('Е') <= 1 and s.count('Л') == 0:
        print(c, s)
        break
