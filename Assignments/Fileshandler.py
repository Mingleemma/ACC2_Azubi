f1 = open("dairy.txt", "r")
print(f1.read())
f1.close()

f2=open("dairy.txt", "a")
f2.write("This is also for business")
f2.close()
