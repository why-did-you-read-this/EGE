f = open('KIM_0002848150_24.txt').readline()
f = f.replace('BA', '*').replace('DA', '*').replace('A', ' ').replace('B', ' ').replace('D', ' ').split()
print(len(max(f, key=len)))
