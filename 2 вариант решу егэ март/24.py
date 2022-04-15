f = open('24.txt').readline()
alphabet = ''
q = []
c = []

for i in range(65, 91):
    alphabet += chr(i)

for i in alphabet:
    q.append('A' + i)

for i in q:
    a = f.count(i)
    c += [a]

max_letter_index = 0
max_letter = max(c)
for i in range(len(q)):
    if c[i] == max_letter:
        max_letter_index = i
        break
print(alphabet[max_letter_index])

