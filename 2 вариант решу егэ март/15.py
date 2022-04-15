q = []
for a in range(25):
    for x in range(25):
        for y in range(25):
            if not (((3 * x + 4 * y) != 70) or (a > x) or (a > y)):
                break
        else:
            continue
        break
    else:
        if a > 0:
            print(a)
            q += [a]

print('')
print(min(q))
