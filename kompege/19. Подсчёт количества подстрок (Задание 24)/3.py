f = open('24-3.txt').readline()
c = 0
f = f.replace('STOCK', ' ').replace('OCK', '*')
print(f.count('*'))
