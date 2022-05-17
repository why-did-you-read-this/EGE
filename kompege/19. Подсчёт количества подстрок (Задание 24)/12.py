f = [str.strip(i) for i in open('24-12.txt').readlines()]
c = 0
for i in range(len(f)):
    while ('AOAOA' in f[i]) or ('OAOAO' in f[i]):
        f[i] = f[i].replace('AOAOA', 'AOA AOA').replace('OAOAO', 'OAO OAO')
    if f[i].count('AOA') > f[i].count('OAO'):
        c += 1
print(c)
