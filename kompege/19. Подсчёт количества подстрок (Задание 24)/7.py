f = open('24-7.txt').readline()
c = 0
for i in range(len(f) - 3):
    if (f[i] == 'G') and ((f[i + 2] + f[i + 3]) == 'ME'):
        c += 1
print(c)
