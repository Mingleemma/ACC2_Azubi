userReply = input("Do you need to ship a package? (Type yes or no) ")
if userReply == "yes":
  print("We can help you ship that package!")
else:
  print("Please come back when you do need to  ship a package. Thank you.")

userReply = input("Would you like to buy stamps, an envelope, or make a copy? (Type stamps, envelope, or copy)")
if userReply == "stamps":
    print("We have plenty of stamp designs to  choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Type a number)")
    print("Here are {} copies".format(copies))
else:
    print("Thank you, please come again.")