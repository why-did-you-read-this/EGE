f = open('24-36037.txt').read()
f = f.replace('XZZY', 'XZZ ZZY').split()
i = list(map(len, f))
print(max(i))
