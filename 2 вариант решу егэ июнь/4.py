s = '011110111001100'
i = int(s, 2)
new_i = ''
while i > 0:
    new_i += str(i % 8)
    i //= 8
new_i = new_i[::-1]
print(new_i)
