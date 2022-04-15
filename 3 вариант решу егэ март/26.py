f = open('inf_22_10_20_26.txt')
f.readline()
a = []
a_new = []
for i in f:
    a += [int(i)]
a = sorted(a)
stoimost = 0
for i in range(len(a) - 1):
    if a[i] <= 100:
        stoimost += a[i]
        a[i] = 0
while 0 in a:
    a.remove(0)

while a:
    a_new += [a[-1]]
    a.pop(-1)
    a_new += [a[0]]
    a.pop(0)

a_skidka = []
for i in range(1, len(a_new), 2):
    a_skidka += [a_new[i]]
    a_new[i] = a_new[i] * 0.7

vsego = int(sum(a_new) + stoimost)
if type(sum(a_new)) != int:
    vsego += 1
print(vsego, max(a_skidka))
