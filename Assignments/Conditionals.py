
userDictionary = {
    "ADWOA" : "You were born on Monday",
    "KOJO" : "You were born on Monday",
    "ABENA" : "You were born on Tuesday",
    "KWABENA" : "You were born on Tuesday",
    "KWAKU" : "You were born on Wednesday",
    "AKUA" : "You were born on Wednesday",
    "YAA" : "You were born on Thursday",
    "YAW" : "You were born on Thursday",
    "AFIA" : "You were born on Friday",
    "KOFI" : "You were born on Friday",
    "AMA" : "You were born on Saturday",
    "KWAME" : "You were born on Saturday",
    "AKOSUA" : "You were born on Sunday",
    "KWESI" : "You were born on Sunday"
}
#myFavoriteFruitDictionary["Adam"]

# print(userDictionary['Abena'])



response = "yes"
while response == "yes":
    userInput = input("What is your name? ")
    userInput = userInput.upper()
    print(userInput)
    a = userInput
    if userInput in userDictionary:
        print(userDictionary[userInput])
    else:
         print("Try again")

    response = input("Do you want to check for another name? Answer yes/no. ")
    response = response.lower()
    while response != "yes" and response != "no":
        response = input("Do you want to check for another name? Answer yes/no. ")
        response = response.lower()
