u = 5 * (216 ** 3031) + 4 * (36 ** 3042) - 3 * (6 ** 3053) - 3064
new_u = ''
while u > 0:
    new_u += str(u % 6)
    u //= 6
new_u = new_u[::-1]
s = 0
for i in new_u:
    s += int(i)
print(s)
