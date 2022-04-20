# https://inf-ege.sdamgia.ru/problem?id=41001
f = open('26-41001.txt')
n = f.readline()
processes = []
a = []
b = []
for s in f:
    a += [s.split()]
t_begin = 1633046400
t_end = t_begin + 7 * 24 * 60 * 60
max_time = 0
for i in a:
    if t_begin <= int(i[0]) < t_end:
        if int(i[1]) > t_begin:
            b += [i]
for time in range(t_begin, t_end + 1):
    if time % 1000 == 0:
        print(time)
    p = 0
    for i in b:
        if int(i[0]) <= time:
            if time <= int(i[1]) or int(i[1]) == 0:
                p += 1
    processes += [p]

print('')
print(max(processes))
