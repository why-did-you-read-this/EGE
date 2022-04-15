f = open('24.txt').readline()
alphabet = []
for letter in range(65, 91):
    alphabet += [chr(letter)]

otvet = [0]*len(alphabet)

for i in range(1, len(f) - 1):
    if f[i-1] == f[i+1]:
        otvet[alphabet.index(f[i])] += 1

print(alphabet[otvet.index(max(otvet))])

