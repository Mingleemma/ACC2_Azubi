#FOR LOOPS
#userInput = input("What is your day born name? ")
#if userInput == "Adwoa" or userInput == "Kwadwo":
    #print ("You were born on Monday")
#else:
    #print("You weren't born on Monday")

#WHILE LOOPS
response = "yes"
while response == "yes":
    userInput = input("What is your day born name? ")
    if userInput == "Adwoa" or userInput == "Kwadwo":
        print ("You were born on Monday")
    else:
        print("You weren't born on Monday")
    response = input ("Do you want to enter another name? yes/no")

    while response != "yes" and response != "no":
        response = input("Do you want to enter another name? yes/no")