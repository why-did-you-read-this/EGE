f = open('24-14.txt').readline()

for i in 'ABCEF':
    f = f.replace(i, '*')

f = f.replace('D', ' ')
f = f.split()
print(len(min(f, key=len)) + 2)
