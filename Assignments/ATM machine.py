# Dictionary for ATM
from typing import Dict, Any, Union

# x = 'username'
# y = 'pin'
# z = 'balance'

Database = {
    'username': 'trial', 'pin' : 0000, 'balance':{'GHC': '140', 'USD':0 } ,
    'abby1': 'abby1', 'pin': 1234, 'balance': {'GHC': '21140', 'USD': 100},
    'username': 'bamby21', 'pin': 2120, 'balance': {'GHC': '12300', 'USD': 0},
    'username': 'cint12', 'pin': 3349, 'balance': {'GHC': '2135', 'USD': 589},
    'username': 'dandy4', 'pin': 7865, 'balance': {'GHC': '20', 'USD': 23400},
    'username': 'elit2', 'pin': 3820, 'balance': {'GHC': '22000', 'USD': 50},
    'username': 'fren1', 'pin': 9823, 'balance': {'GHC': '10', 'USD': 40},
    'username': 'gangy6', 'pin': 5297, 'balance': {'GHC': '5500', 'USD': 5},
    'username': 'hany8', 'pin': 8152, 'balance': {'GHC': '23470', 'USD': 11},
    'username': 'iter9', 'pin': 3545, 'balance': {'GHC': '2456', 'USD': 32},
}






response = "yes"
while response == "yes":
    print("Welcome to Ecobank")
    userInput = input("Would you like to withdraw money? yes/ no ")
    userInput = userInput.lower()
    if userInput == "yes":
       Question = input("Kindly enter your username. ")
       question = Question
       if question in Database:
           Pin = input("Kindly input your PIN ")
           print(input("Enter amount to withdraw "))
       else:
           print ("check your username and try again.")

    elif userInput == "no":
        print("See customer care for other services.")
    elif userInput != "yes" or userInput != "no":
        print("Kindly read the prompt again.")





# pin = int(input("Please enter your 4-digit pin "))
#
#
#
#
#
#
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