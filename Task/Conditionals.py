response = "Yes"
while response == "Yes":
    userInput = input("What is your day born name? ")
    userInput = userInput.lower()
    if userInput == "adwoa" or userInput == "kojo":
        if userInput == "kojo":
             print("You are a boy born on Monday")
        elif userInput == "adwoa":
             print("You are a girl born on Monday")

    else:
        print("Your were not born on Monday")

    response = input("Do you want to check for another name? yes/no ")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to check for another name? yes/no ")
        response = response.lower()


