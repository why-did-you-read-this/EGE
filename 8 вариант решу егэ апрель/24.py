f = open('zadanie24_2.txt').readline()
while ('LL' in f) or ('DD' in f) or ('RR' in f):
    f = f.replace('LL', 'L L')
    f = f.replace('DD', 'D D')
    f = f.replace('RR', 'R R')

f = f.split()

print(len(max(f, key=len)))