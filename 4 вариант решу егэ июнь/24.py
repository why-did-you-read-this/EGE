f = open('24.txt').readline()
f = f.replace('A', ' ').replace('C', ' ')
f = f.split()
print(len(max(f, key=len)))
