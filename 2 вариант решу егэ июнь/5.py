a = set()
for i in range(10, 1001):
    bin_i = bin(i)[3:]
    j = int(bin_i, 2)
    a.add(i - int(j))

print(len(a))
