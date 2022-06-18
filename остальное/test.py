f = open('24.txt').readline()
f = f.replace('LDR', '*').replace('L', ' ').replace('D', ' ').replace('R', ' ').split()
m = len(max(f, key=len))

if ('LDR' * m + 'LD') in f:
    m = m * 3 + 2
elif ('LDR' * m + 'L') in f:
    m = m * 3 + 1
else:
    m = m * 3

print(m)
