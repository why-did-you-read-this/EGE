f = open('26/26-35484.txt')
f.readline()
a = []
for i in f.read().split():
    if int(i) % 2 == 0:
        a += [int(i)]

print(len(a))