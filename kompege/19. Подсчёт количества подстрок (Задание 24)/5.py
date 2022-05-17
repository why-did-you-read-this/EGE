f = open('24-5.txt').readline()
while 'XIXIX' in f:
    f = f.replace('XIXIX', 'XIX XIX')
print(f.count('XIX'))