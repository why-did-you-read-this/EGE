f = [str.strip(i) for i in open('24-11.txt').readlines()]
c = 0
for i in f:
    for j in range(len(i) - 3):
        if (i[j] + i[j + 2] + i[j + 3]) == 'KGE':
            c += 1
            break

print(c)
