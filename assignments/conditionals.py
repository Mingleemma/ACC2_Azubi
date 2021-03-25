response = "yes"
while response == "yes":
    userInput = input("What is your name? ")
    userInput = userInput.lower()
    if userInput == "kojo" or userInput == "adwoa":
       if userInput == "kojo":
           print("You are a boy born on Monday")
       elif userInput == "adwoa":
           print("You are a girl born on Monday")
    elif userInput == "kwabena" or userInput == "abena":
       if userInput == "kwabena":
           print("You are a boy born on Tuesday")
       elif userInput == "abena":
           print("You are a girl born on Tuesday")
    elif userInput == "kwaku" or userInput == "akua":
       if userInput == "kwaku":
           print("You are a boy born on Wednesday")
       elif userInput == "akua":
           print("You are a girl born on Wednesday")
    elif userInput == "yaw" or userInput == "yaa":
       if userInput == "yaw":
           print("You are a boy born on Thursday")
       elif userInput == "yaa":
           print("You are a girl born on Thursday")
    elif userInput == "kofi" or userInput == "afia":
       if userInput == "kofi":
           print("You are a boy born on Friday")
       elif userInput == "afia":
           print("You are a girl born on Friday")
    elif userInput == "kwame" or userInput == "ama":
       if userInput == "kwame":
           print("You are a boy born on Saturday")
       elif userInput == "ama":
           print("You are a girl born on Saturday")
    elif userInput == "kwasi" or userInput == "akosua":
       if userInput == "kwasi":
           print("You are a boy born on Sunday")
       elif userInput == "akosua":
           print("You are a girl born on Sunday")

    else:
         print("You were not born on any of the days")

    response = input("Do you want to check for another name? Answer yes/no. ")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to check for another name? Answer yes/no. ")
        response = response.lower()