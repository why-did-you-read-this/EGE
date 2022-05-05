f = list(map(int, open('17-5.txt').readlines()))
c = 0
s = 0

for i in f:
    if hex(i)[2:][-1] == 'b' and (i % 7 == 0) and (i % 6 != 0) and (i % 13 != 0) and (i % 19 != 0):
        s += i
        c += 1

print(s, c)
