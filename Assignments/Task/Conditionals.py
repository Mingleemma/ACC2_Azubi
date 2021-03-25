response = "yes"
while response == "yes":
    userInput = input("What is your day born name? ")
    userInput = userInput.lower()
    if userInput == "kwadwo":
        print("You are a boy born on Monday")
    elif userInput == "adwoa":
        print("You are a girl born on Monday")
    elif userInput == "abena":
        print("You are a girl born on Tuesday")
    elif userInput == "kwabena":
        print("You are a boy born on Tuesday")
    elif userInput == "akua":
        print("You are a girl born on Wednesday")
    elif userInput == "kwaku":
        print("You are a boy born on Wednesday")
    elif userInput == "yaw":
        print("You are a boy born on Thursday")
    elif userInput == "yaa":
        print("You are a girl born on Thursday")
    elif userInput == "kofi":
        print("You are a boy born on Friday")
    elif userInput == "afia":
        print("You are a girl born on Friday")
    elif userInput == "kwame":
        print("You are a boy born on Saturday")
    elif userInput == "ama":
        print("You are a girl born on Saturday")
    elif userInput == "akosua":
        print("You are a girl born on Sunday")
    elif userInput == "kwasi":
        print("You are a boy born on Sunday")


        response = input("Do you want to check for another name? Answer yes/no. ")
        response = response.lower()
        while response != "yes" and response != "no":
            response = input("Do you want to check for another name? Answer yes/no. ")
            response = response.lower()