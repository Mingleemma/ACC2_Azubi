f1 = open('text.txt', 'r')
print(f1.read())
# print (f1)
f1.close()

f1 = open('text.txt', 'w')
f1.write('This is also for business')
f1.close()