f = open('24-18.txt').readline()
f = f.replace('КОТ', "*").replace('К', ' ').replace('О', ' ').replace('Т', ' ')
f = f.split()
print(len(max(f, key=len)))
