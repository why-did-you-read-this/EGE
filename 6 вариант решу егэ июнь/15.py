c = 0
for a in range(101):
    for x in range(101):
        for y in range(101):
            if not (((x < a) <= (x ** 2 < 81)) and ((y ** 2 <= 36) <= (y <= a))):
                break
        else:
            continue
        break
    else:
        c += 1

print(c)
