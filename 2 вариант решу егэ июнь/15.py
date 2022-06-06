m = 0

for a1 in range(-100, 101):
    for a2 in range(a1 + 1, 101):
        for x in range(-100, 101):
            if not (((a1 <= x <= a2) <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= (a1 <= x <= a2))):
                break
        else:
            m = max(m, a2 - a1)

print(m)
