i = 91
print(bin(i)[2:])


def sdvig(x):
    x = x * 2
    if x < 128:
        return x
    else:
        return x % 256


i = sdvig(i)
i = sdvig(i)
i -= 1
i = sdvig(i)
i = sdvig(i)
i -= 1

print(i)
