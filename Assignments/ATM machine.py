# Dictionary for ATM
from typing import Dict, Any, Union

# x = 'username'
# y = 'pin'
# z = 'balance'
#Database for ATM Machine
Database = {
    'trial': {'pin': 0000, 'balance':{'GHC': 140, 'USD':0 }},
    'abby1': {'pin': 1234, 'balance':{'GHC': 21140, 'USD':100 }},
    'bamby21': {'pin': 2120, 'balance': {'GHC': 12300, 'USD': 0}},
    'cint12': {'pin': 3349, 'balance': {'GHC': 2135, 'USD': 589}},
}



def Currency():
    Currency = str(input("Choose the currency, GHC or USD "))
    currency = Currency
    if currency == "GHC" or "USD":
        print(Currency)

    else:
        print("Kindly check and input the right currency.")


def Amount():
    float(input("How much do you want to withdraw? "))
    print(Amount)
    amount = Amount

def a():
    a = int(input("Kindly input the number that corresponds with the options above "))
    return a

def login():
    Question = input("Kindly enter your username. ")
    username = Question
    if username in Database:
        Pin = int(input("Kindly input your PIN "))
        if Pin == Database[username]["pin"]:
            print("correct pin!")
        else:
            print("Wrong pin. Kindly try again.")
    else:
        print("check your username and try again.")



def balance(username, currency):
    amount = Database[username]["balance"][currency]
    print("You have {} {}".format(currency, amount))


def withdrawal(username, currency, amount):
    balance = Database[username]["balance"][currency]
    if balance - amount >= 5:
        Database[username]["balance"][currency] -= amount
        print("You are withdrawal {} {}".format(currency, amount))
        balance(username, currency)
    else:
        userInput = input("You can not have a balance of less than GHC 5 or USD 5. Do you want to re-enter a different amount? "
              "YES/NO ")
        userInput = userInput.Upper
        print(userInput)
        if userInput == "YES":
            print(mainMenu)

mainMenu = '''
Welcome to Ecobank.
What would you like to do today?
    1. Withdraw
    2. Deposit
    3. Check balance'''



def deposit(username, currency, amount):
    Currency= input("Choose the currency, GHC or USD ")
    print(Currency)
    currency = Currency
    Amount = float(input("How do you want to withdraw? "))
    print(Amount)
    amount = Amount
    Database[username]["balance"][currency] += amount
    print("You are depositing {} {}".format(currency, amount))









response = "yes"
while response == "yes":
    print(mainMenu)
    ask = int(input("Kindly input the number that corresponds with the options above "))
    print(ask)
    a = ask
    if a == 1:
        login()
        Currency()
        Amount()
        withdrawal(username, currency, amount)
        balance(username, currency)

    elif a == 2:
        login()
        Currency()
        deposit(username, currency, amount)
        balance(username, currency)

    elif a == 3:
        login()
        balance(username, currency)



#        Question = input("Kindly enter your username. ")
#        question = Question
#        if question in Database:
#            Pin = int(input("Kindly input your PIN "))
#            if Pin == Database[question]["pin"]:
#                print(input("Select the currency: GHC or USD "))
#
#            else:
#                print("Kindly try again.")
#
#
#        else:
#            print ("check your username and try again.")
#
#     elif userInput == "no":
#         print("See customer care for other services.")
#     elif userInput != "yes" or userInput != "no":
#         print("Kindly read the prompt again.")
# #
#
#
#
#     print(Question)
#     if Question == "yes":
#         Question = Question.lower()
#         print(userName)
#     elif Question == "no":
#         Question = Question.lower()
#         print("See customer care for other services.")
#     else:
#         print("Try again")
#

# if response == "YES":
#  response = response.upper()

#     if userName() in Database():
#         print(pin())
#         if pin() in Database():
#             print ("Would you like to withdraw in GHS or USD? ")
#             if response == "GHS" or "USD":
#                 print("Kindly enter the amount. ")
#
#     else:
#         print((input("Would you like to withdraw money? yes/ no ")))

# print(input("Would you like to withdraw money? yes/ no "))
#     if userName() in Database():
#         print(pin())
#         if pin() in Database():
#             print ("Would you like to withdraw in GHS or USD? ")
#             if response == "GHS" or "USD":
#                 print("Kindly enter the amount. ")
# else:
#     print(userName() )

# response = "no":
#



