f = list(map(str.strip, open('24-19.txt').readlines()))
m = ''
s1 = ''
for i in f:
    if i.count('Q') >= m.count('Q'):
        m = i
    s1 += i
d = {x: m.count(x) for x in sorted(set(m)) if m.count(x) != 0}
m = min(d.values())
l = [i for i in d if d[i] == m]
print(l[0] + str(s1.count(l[0])))
