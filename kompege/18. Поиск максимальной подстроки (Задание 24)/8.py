f = open('24-8.txt').readline()
f = f.replace('PP', 'P P')
f = f.split()
print(len(max(f, key=len)))
