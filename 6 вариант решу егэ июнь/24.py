f = open('24.txt').readline()
f = f.replace('AB', '*').replace('CB', '*').replace('A', ' ').replace('B', ' ').replace('C', ' ').split()
print(len(max(f, key=len)))
