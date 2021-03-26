response = "yes"
while response == "yes":
    userInput = input("What is your day born name? ")
    userInput = userInput.lower()
    if userInput =="abena" or "kwabena":
        if userInput == "abena":
            print("You are a female born on a Tuesday." )
        if userInput == "kwabena":
            print("You are a male born on a Tuesday.")
    else:
        print("You weren't born on a Tuesday.")
    if userInput == "kwaku" or "akua":
        if userInput == "kwaku":
            print("You are a male born on a Wednesday.")
        if userInput == "akua":
            print("You are a female born on a Wednesday.")
    else:
        print("You weren't born on a Wednesday.")
    if userInput == "adwoa" or userInput == "kojo":
        if userInput == "kojo":
            print("You are a male born on a Monday.")
        elif userInput == "adwoa":
            print("You are a female born on a Monday.")
    else:
        print("You weren't born on a Monday.")
    response = input("Do you want to find out about other day born names? Answer yes/no. ")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to find out about other day born names? Answer yes/no. ")
        response = response.lower()