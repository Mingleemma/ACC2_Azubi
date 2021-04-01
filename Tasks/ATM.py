#! /bin/bash
# Creating user
print("Welcome to AZUBIBANK ATM SYSTEM")
userName = input("Enter your username: ")
names = ["Kwame"]
balance = ["5000"]

if userName == "kayfa":
    options = int(input("Press 1 to withdraw or Press 2 to check balance: "))
    if options == 1:
        amount = int(input("enter amount to withdraw: "))
        if amount > int(balance[0]):
            print("Insufficient Balance")
            exit()
        available_balance = int(balance[0]) - amount
        receipt = input("Do want a receipt for your transactions? Y/N ")
        if receipt == "Y":
            print(f'Receipt printed')
            another = input("Do you want to perform another transaction? Y/N ")
            if another == "Y":
                amount = int(input("enter amount to withdraw: "))
                if amount > int(balance[0]):
                    print("Insufficient Balance")
                    exit()
                available_balance = int(balance[0]) - amount
            elif another == "N":
                print(f"Transaction complete!, GHS{amount} debited from your account"),
                print(f"available balance is GHS{available_balance}, Thank you for banking with us")
        else:
            print(f"Transaction complete!, GHS{amount} debited from your account")
            print(f"available balance is GHS{available_balance}, Thank you for banking with us")
    elif options == 2:
        print(f'{names[0]}, your account balance is {balance[0]}')
else:
    print("Invalid Username")
