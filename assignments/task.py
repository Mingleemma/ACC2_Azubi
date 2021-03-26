response = "yes"
while response == "yes":
    userInput = input("What is your day born name ?")
    userInput = userInput.lower()
    if userInput == "adjoa" or userInput == "kojo":
        if userInput == "kojo":
            print("You are a boy born on Monday")
        elif userInput == "adjoa":
            print("You are a girl born on Monday")
    else:
        print("You were not born on Monday")
    response = input("Do you want to check for another name?(Enter yes or no) ")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to check for another name ? (Enter yes or no" )
        response = response.lower()

