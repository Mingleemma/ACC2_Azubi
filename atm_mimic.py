#! /usr/bin/python3

#imported the sys module to be able to use the exit function
import sys

#A dictionary containing account information of the users 
customers = {'MJ':{'username':'MJ', 'pin':'0000', 'balance':{'GHS':82366, 'USD':2220}},
            'Steph':{'username':'Steph', 'pin':'1234', 'balance':{'GHS':523000, 'USD':1340}},
            'NiiOdoi':{'username':'NiiOdoi', 'pin':'2025', 'balance':{'GHS':2733862, 'USD':123456}}
}

#This function asks the user if he/she would perform another transaction after completing an action.
def anotherOp():
    #declaring variable to be used in the function
    answer = input("""
Would you like to perform another transaction? (y/n): """).lower()
    if answer == 'y':
        active = True
    elif answer == 'n':
        active = False
        #exits the entire program running when there are no other transactions to be performed
        sys.exit("Thanks for banking with us!!")

#This function initializes the login feature. Where authorized users would have to login in with their username and pin 
#before accessing the services on the ATM
def log_in():
    loggedIn = False
    attempts = 2
    while(loggedIn == False):
        #request user to enter username and pin
        username = input("Enter your username: ")
        pin = int(input("Enter your 4-digit Pin: "))
        #checking if the user has ran out of attempts so he/she gets logged out
        if(attempts == 0):
            print("""
            You are out of attempts! 
            Logging you out...""")
            return False
        # looping through all values in the dictionary
        for user in customers:
            #checking if the entered username exists in the dictionary
            if(username in customers[user].values()):
                #checking if the pin entered corresponds with the entered username
                if(pin == int(customers[user]["pin"])):
                    print("Logged in")
                    loggedIn = True
                    return True                    
                else:
                    print(f"Wrong pin! {attempts} attempts left")
                    attempts = attempts - 1
                    break        
        else:
            print(f"Username does not exist! {attempts} attempts left")
            attempts = attempts - 1

#This function checks the balances of users in a selected currency
def check_balance(username):
    #assigning values in the user's dictionary to the GHS and USD variables
    GHS = customers[username]['balance']['GHS']
    USD = customers[username]['balance']['USD']
    #requests users to select a currency to transact in
    currency = input('Select your currency (GHS/USD): ')
    #displaying output dependent on currency input
    if currency == 'GHS':
        print(f'Your current balance is GHS{GHS}')
    elif currency == 'USD':
        print(f'Your current balance is USD{USD}') 
    else:
        print ('Kindly select a currency')
        print (currency)    

#this function updates the user's balance in the dictionary with deposits made
def deposit_balance_update(username, currency, deposit):
    #declaring variable to be used in the function
    balance = int(customers[username]['balance'][currency])
    #adding deposit to original balance and printing new balance in a statement 
    if (balance + deposit) >= 0:
        customers[username]['balance'][currency] += deposit
        print(f"Your new balance is {currency}{customers[username]['balance'][currency]}")
    
#this function updates the user's balance in the dictionary when withdrawals are made
def withdrawal_balance_update(username, currency, withdraw):
    balance = int(customers[username]['balance'][currency])
    #subtracting withdrawals from original balance and printing new balance in a statement 
    if (balance - withdraw) >= 0:
        customers[username]['balance'][currency] -= withdraw
        print(f"You have withdrawn {currency}{withdraw}")
        print(f"Your new balance is {currency}{customers[username]['balance'][currency]}")
    #printing the following statement when the withdrawal amount is greater than the user's balance  
    else:
        print("""
Insufficient funds. Cannot perform this transaction!!""")
        print(f'Your account balance available for withdrawal is {currency}{customers[username]["balance"][currency]}')

#this function runs the entire operations after the user logs in. i.e performs all the services the ATM offers
def ops(username):
    active = True
    #this loop keeps the program running as long as the condition is true
    while active:
        operations = """ 
        What Transaction Do You Want To Perform?
        1)    Deposit
        2)    Withdraw
        3)    Balance
        4)    Quit

        Select an option: """

        option = int(input(operations))
 #DEPOSIT OPTION -- Depositing into the account   
        if option == 1:
            currency = input('Select your currency (GHS/USD): ')
            if currency == 'GHS':
                #enter amount to deposit in GHS and print a statement
                deposit = int(input("Enter amount to deposit: GHS"))
                print("You have deposited GHS{} into your account".format(deposit))
            elif currency == 'USD':
                #enter amount to deposit in USD and print a statement
                deposit = int(input("Enter amount to deposit: USD"))
                print("You have deposited USD{} into your account".format(deposit)) 
            else:
                print (currency)
            #calling the deposit_balance_update and anotherOp functions
            deposit_balance_update(username, currency, deposit)    
            anotherOp()

 #WITHDRAWAL OPTION -- WIthdrawing from the account           
        elif option == 2:
            currency = input('Select your currency (GHS/USD): ')
            if currency == 'GHS':
                #enter amount to withdraw in GHS and print a statement
                withdraw = int(input("Enter amount to withdraw: GHS"))
            elif currency == 'USD':
                #enter amount to withdraw in USD and print a statement
                withdraw = int(input("Enter amount to withdraw: USD"))
            else:
                print (currency)
            #calling the withdrawal_balance_update and anotherOp functions   
            withdrawal_balance_update(username, currency, withdraw)
            anotherOp()

 #CHECK BALANCE OPTION
        elif option == 3:
            #calling the check_balance and anotherOp functions
            check_balance(username)
            anotherOp()

 #QUIT OPTION           
        elif option == 4:
            #exiting the entire program using the exit function
            sys.exit("""
            Thank you for banking with TronexBank
            Logging out......""")   

def program():
    #printing a welcome message
    print("Welcome to TronexBank!")
    input("""
Press ENTER to continue""")
    #authenticating users using the login function and running the ops function
    if log_in():
        username = input("Enter your username again: ")
        print (f'''Hi {username}, ''')
        ops(username)
    else:
        #exiting the ATM because the user could not successfully log in
        sys.exit("Exiting TronexBank ATM....")

program()

