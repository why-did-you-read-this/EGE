f = open('24-11.txt').readline()
f = f.replace('X', '1').replace('Y', '2').replace('Z', '3')
maxC = 0
c = 1
for i in range(len(f)):
    if int(f[i - 1]) <= int(f[i]) or i == len(f):
        c += 1
    else:
        maxC = max(maxC, c)
        c = 1
print(maxC)
