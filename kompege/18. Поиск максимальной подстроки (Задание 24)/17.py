f = open('24-16.txt').readline()
f = f.replace('D', ' ').split()
m = 0
for i in range(len(f) - 2):
    s = f[i] + 'D' + f[i + 1] + 'D' + f[i + 2]
    m = max(m, len(s))

print(m)
