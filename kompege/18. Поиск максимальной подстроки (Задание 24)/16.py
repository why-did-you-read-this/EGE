f = open('24-16.txt').readline()
f = f.split('A')
m = 0
for i in range(len(f) - 1):
    sub = f[i] + 'A' + f[i + 1]
    m = max(m, len(sub))
print(m)
