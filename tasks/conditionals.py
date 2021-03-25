response = "yes"
while response == "yes":
    userInput = input("What is your name? ")
    if userInput == "kojo" or userInput == "adwoa":
        userInput = userInput.lower()
        if userInput == "kojo":
            print("You are a boy born on monday")
        else:
            print("You are a girl born on monday")

    else:
        print("You are not born on monday")

        response = input("Do you want to check for another name? Answer yes/no. ")
        response = response.lower()
        while response != "yes" and response != "no":
            response = input("Do you want to check for another name? Answer yes/no. ")
            response = response.lower()