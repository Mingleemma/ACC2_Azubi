import random
import string
import datetime
import json
import csv
from os import  path
import time
# sample data for users is loaded from external file
userJsonPath="users.json"
a_file = open(userJsonPath, "r")
userData = json.load(a_file)

# variable initialized
balance = 0

# this is where our login function is initialized
def login():
    # we declare variables to be used in our function
    loggedIn = False
    attempts = 3
    global loggedInUser
    while(loggedIn == False):

        # prompt user to enter username and password
        username = input("Welcome, please enter your username: ")
        pin = int(input("Please enter your PIN: "))

        # this if block simply checks if the number of attempts have ran out so that it exits
        if(attempts == 0):
            print("You are out of attempts! Logging you out...")
            return False

        # we loop through all values in the userData dictionary
        for user in userData:

            # we check if the entered username exists in the dictionary
            if(username in userData[user].values()):

                # if the username exists, we check if the pin corresponds to the entered username
                if(pin == int(userData[user]["pin"])):
                    print("Logged in")
                    loggedIn = True
                    # we keep logged in user data in loggedInUser variable
                    loggedInUser = userData[user]
                    return True
                else:
                    print("Wrong pin! "+ str(attempts) + " attempts left")
                    attempts = attempts - 1
                    break

        # this executes after looping through all values in the dictionary and find that username does not match
        else:
            print("Username not found! " + str(attempts) + " attempts left")
            attempts = attempts - 1

#end of login function

# main function for starting the menu
def startMenu():
    print("""
    ___Welcome """ + loggedInUser["username"] + """___
    Please choose your option:
    1) Withdraw money
    2) Check balace
    3) Change your pin
    4) View your past transactions
    5) Exit
    """)
    choice = int(input("Your option: "))
    if(choice == 1):
        withdraw()
    elif(choice == 2):
        checkBalance()
        afterTransaction("balance",None)
    elif(choice == 3):
        changePin()
        afterTransaction("Change pin",None)
    elif(choice == 4):
        viewStatements()
        performAnother()
    else:
        exit()
# end of main function

# start of withdraw function
def withdraw():
    print("""
    Please select the currency to withdraw
    1 - USD
    2 - GHS
    """)
    currency = int(input("Your selection: "))

    withdrawAmount = int(input("Please enter amount to withdraw "))

    if(currency == 1):
        #withdraw from USD

        # we are checking if the balance for the loggedInUser is enough for withdraw
        if(withdrawAmount <= loggedInUser["balance"]["USD"]):
            balance = loggedInUser["balance"]["USD"] - withdrawAmount
            for user in userData:
                if(loggedInUser["username"] == userData[user]["username"]):
                    userData[user]["balance"]["USD"] = balance
            a_file = open(userJsonPath, "w")
            json.dump(userData, a_file)
            a_file.close()
            print("Withdrawn successfully!!! Your balance is USD " + str(balance))
        else:
            print("Insufficient balance in USD!" )
            return False

    else:
        #withdraw from GHS

        # we are checking if the balance for the loggedInUser is enough for withdraw
        if(withdrawAmount <= loggedInUser["balance"]["GHS"]):
            balance = loggedInUser["balance"]["GHS"] - withdrawAmount
            for user in userData:
                if(loggedInUser["username"] == userData[user]["username"]):
                    userData[user]["balance"]["GHS"] = balance
            a_file = open(userJsonPath, "w")
            json.dump(userData, a_file)
            a_file.close()
            print("Withdrawn successfully!!! Your balance is GHS " + str(balance))
        else:
            print("Insufficient balance in GHS!" )
            return False
    
    afterTransaction("withdraw",withdrawAmount)
    return True
# end of withdraw


# start of check balance
def checkBalance():
    balanceUsd = loggedInUser["balance"]["USD"]
    balanceGhs = loggedInUser["balance"]["GHS"]
    print("Your balance is USD " + str(balanceUsd) + " and GHS " + str(balanceGhs) +" !")
    return True
# end of check balance


# start of change pin
def changePin():
    oldPin = input("Enter your old pin ")
    if(loggedInUser["pin"] == oldPin):
        newPin = input("Now enter your new pin ")
        confirmPin = input("Re-enter your new pin ")
        if(newPin == confirmPin):
            # this block of code loops through entire list of users so that if can update exactly where the pin for the logged user is
            for user in userData:
                if(loggedInUser["username"] == userData[user]["username"]):
                    userData[user]["pin"] = newPin
            a_file = open(userJsonPath, "w")
            json.dump(userData, a_file)
            a_file.close()
            # pin change ends here

            print("Password changed")
        else:
            print("Passwords do not match")
    else:
        print("Wrong pin")
    return True
# end of change pin

# start of view statements
def viewStatements():
    print("Transaction TransactionId Amount")
    with open('transactions.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['username'] == loggedInUser["username"]):
                print(row['transaction'], row['transactionId'], row['amount'])
    # console stops for 3 seconds so user can read past transactions
    time.sleep(3)
# end of view statements


# start of function to ask to perform another transaction
def performAnother():
    print("""
        Do you want to perform another transaction?
        Yes
        No
        """)
    another = input("Your value: ")
    if(another.lower() == "yes"):
        startMenu()
    else:
        exit()
# end of perform another function


# start of function to be called after every transaction
def afterTransaction(transValue, amount):
    todayDate = datetime.datetime.now()
    # this code simply creates a unique transactionId by appending the transvalue e.g. balance with a random string of 10 small letters as well as the current timestamp
    transactionId = transValue + ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + "-" + str(todayDate)
    printReceipt = input("Should a receipt be printed? Yes/No: ")
    if(printReceipt.lower() == "yes"):
        if(transValue.lower() == "withdraw"):
            print("""
            ____RECEIPT____
            TransID: """ + transactionId + """
            Dear customer, you have successfully withdrawn """ + str(amount) + """.
            """)
            time.sleep(3)
        elif(transValue.lower() == "balance"):
            print("""
            ____RECEIPT____
            TransID: """ + transactionId + """
            Dear customer, you have successfully checked your balance.
            """)
            time.sleep(3)
        else:
            print("""
            ____RECEIPT____
            TransID: """ + transactionId + """
            Dear customer, you have successfully changed your pin.
            """)
            time.sleep(3)
            
    #  this just checks if the transactions exist before diving in   
    file_exists = path.isfile('transactions.csv')
    with open('transactions.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'transaction', 'transactionId', 'date','amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header

        if(transValue.lower() != "withdraw"):
            writer.writerow({'username': loggedInUser["username"], 'transaction': transValue, 'transactionId':transactionId, 'date':str(todayDate),'amount':'no'})
        else:
            writer.writerow({'username': loggedInUser["username"], 'transaction': transValue, 'transactionId':transactionId, 'date':str(todayDate),'amount':amount})

        performAnother()
        
    return True
# end of after transaction function















