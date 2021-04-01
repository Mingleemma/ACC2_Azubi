f1 = open("text.txt","r")
print(f1.read())
f1.close()

f2 = open("text.txt","a")
f2.write("I really need to make it! ")
f2.close()