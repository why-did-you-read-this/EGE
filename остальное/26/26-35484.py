f = open('26-35484.txt')
# f = open('26-test.txt')
f.readline()
a = []
vse = []
for i in f.read().split():
    vse += [int(i)]
    if int(i) % 2 == 0:
        a += [int(i)]

maxF = 0
c = 0
for i in range(len(a)):
    print(i)
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) / 2 in vse:
            c += 1
            maxF = max(maxF, (a[i] + a[j]) / 2)

print('')
print(c, int(maxF))
