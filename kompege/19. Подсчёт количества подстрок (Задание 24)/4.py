f = open('24-4.txt').readline()
print(f.count('BOSS') - f.count('JBOSS') - f.count('BOSSJ') + f.count('JBOSSJ'))
