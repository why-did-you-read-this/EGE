f = open('24.txt').readline()
while 'XZZY' in f:
    f = f.replace('XZZY', 'XZZ ZZY')

f = f.split()
print(len(max(f, key=len)))
