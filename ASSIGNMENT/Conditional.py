Response = "Yes"
while Response == "Yes":
    UserInput = input("What is your day born name? ")
    UserInput = UserInput.capitalize()
    if UserInput == "Kojo":
        print("You are a boy born on Monday")
    elif UserInput == "Adwoa":
        print("You are a girl born on Monday")
    elif UserInput == "Kwabena":
        print("You are a boy born on Tuesday")
    elif UserInput == "Abena":
        print("You are a girl born on Tuesday")
    elif UserInput == "Kweku":
        print("You are a boy born on Wednesday")
    elif UserInput == "Ekua":
        print("You are a girl born on Wednesday")
    elif UserInput == "Yaw":
        print("You are a boy born on Thursday")
    elif UserInput == "Yaa":
        print("You are a girl born on Thursday")
    elif UserInput == "Kofi":
        print("You are a boy born on Friday")
    elif UserInput == "Afia":
        print("You are a girl born on Friday")
    elif UserInput == "Kwame":
        print("You are a boy born on Saturday")
    elif UserInput == "Ama":
        print("You are a girl born on Saturday")
    elif UserInput == "Kwesi":
        print("You are a boy born on Sunday")
    elif UserInput == "Esi":
        print("You are a girl born on Sunday")

    else:
        print("Your name doesn't correspond to any day in the database")

    Response = input("Do you wish to enter a new name? (Yes / No) ")
    Response = Response.capitalize()
    while Response != "Yes" and Response != "No":
        print("This response isn't valid")
        Response = input("Do you wish to enter a new name? (Yes / No) ")
        Response = Response.capitalize()
