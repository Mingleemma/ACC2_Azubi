# f1 = open("diary.txt", "r")
# print(f1.read())
# f1.close()

f2 = open("diary.txt", "a")
f2.write("I learnt a lot.")
f2.close

f1 = open("diary.txt", "r")
print(f1.read())