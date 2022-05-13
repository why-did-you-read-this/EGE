f = open('24-13.txt').readline()
s = f[0]
max_s = ''
for i in range(1, len(f)):
    if f[i - 1] > f[i]:
        s += f[i]
    else:
        max_s = max(max_s, s, key=len)
        s = f[i]
    if i == len(f) - 1:
        s += f[i]
        max_s = max(max_s, s, key=len)

print(max_s)
