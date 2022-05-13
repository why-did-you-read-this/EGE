f = open('24-15.txt').readline()
for i in 'ABCEF':
    f = f.replace(i, ' ')

f = f.split()
print(len(min(f, key=len)))
