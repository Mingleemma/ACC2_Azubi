response = "yes"
while response == "yes":
    userInput = input("what is your dayborn name?")
    userInput = userInput.lower()
    if userInput == "adwoa" or userInput == "kojo":
      if userInput == "kojo":
        print("You are a boy born on Monday")
    else:
        print("You were not born on Monday")
        response =input("Do you want to check for another name? Answer yes/no")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to check for another name? Answer yes/no")
response = response.lower()
