f = open('24-9.txt').readline()
f = f.replace('XZZY', 'XZZ ZZY')
f = f.split()
print(len(max(f, key=len)))
