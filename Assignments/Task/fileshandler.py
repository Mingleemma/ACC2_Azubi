f1 = open('text.txt', 'r')
print(f1.read())
f1.close()

f1 = open('text.txt', 'w')
f1.write('This is also for business')
f1.close()