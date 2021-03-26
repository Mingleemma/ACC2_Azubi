response = "yes"
while response == "yes":
    userInput = input("what is your day born name?\n ")
    userInput = userInput.lower()
    if userInput == "kojo" or userInput == "adwoa":
        if userInput == "kojo":
            print("You are a boy born on monday")
        else:
            print("You are a girl born on monday")

    else:
        print("You are not born on monday")

    response = input("Do you want to check for another name? Answer yes/no.\n ")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to check for another name? Answer yes/no. ")
        response = response.lower()