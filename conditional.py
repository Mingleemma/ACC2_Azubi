response = "yes"
while response == "yes":
    userInput = input("What is your name? ")
    userInput = userInput.lower()
    if userInput == "mada" or userInput == "jane":
       if userInput == "mada":
           print("You are a boy born on Monday")
       elif userInput == "jane":
           print("You are a girl born on Monday")

    else:
         print("You were not born on Monday")

    response = input("Do you want to check for another name? Answer yes/no. ")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to check for another name? Answer yes/no. ")
        response = response.lower()