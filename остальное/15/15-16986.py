a_list = []
for a in range(100):
    for x in range(100):
        for y in range(100):
            if not(((y + 2 * x) != 48) or (a < x) or (x < y)):
                break
        else:
            continue
        break
    else:
        a_list.append(a)

print(max(a_list))
