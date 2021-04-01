#!/usr/bin/python3

users = {
    "willie": {
        "pin": "1234",
        "balance": {
            "GHS": 10000,
            "USD": 100
        }
    },
    "brian": {
        "pin": "5678",
        "balance": {
            "GHS": 25000,
            "USD": 500
        }
    },
    "kasakula": {
        "pin": "3456",
        "balance": {
            "GHS": 47525,
            "USD": 322
        }
    },

}


def login():
    username = input("Enter your username: ")
    try:
        user = users[username]
        pin = input("Enter your pin: ")
        if user:
            if user['pin'] == pin:
                return username
            else:
                print("Wrong pin")
        else:
            print("User does not exist")
        return None
    except KeyError:
        print("User {} is not registered".format(username))


def check_balance(username):
    GHS = users[username]['balance']['GHS']
    USD = users[username]['balance']['USD']
    print("Your balance is: {} GHS and {} USD".format(GHS, USD))


def update_balance(username, currency, amount):
    balance = float(users[username]['balance'][currency])
    if (balance + amount) >= 0:
        users[username]['balance'][currency] += amount
        print("New balance is {} {}".format(users[username]['balance'][currency], currency))
    else:
        print("Insufficient Funds")


def withdraw(username):
    currency = input("Enter Currency. (GHS or USD): ").upper()
    amount = float(input("Enter amount to withdraw: "))
    update_balance(username, currency, (amount * -1))


def deposit(username):
    currency = input("Enter Currency. (GHS or USD): ").upper()
    amount = float(input("Enter amount to deposit: "))
    update_balance(username, currency, amount)


def logic(username):
    text = '''
            1. Check Balance
            2. Withdraw Money
            3. Deposit Money
            What do you want to do? (Enter 1,2,or 3): '''
    choice = int(input(text))
    if choice == 1:
        check_balance(username)
    elif choice == 2:
        withdraw(username)
    elif choice == 3:
        deposit(username)
    else:
        print("wrong choice")
        logic(username)


def main():
    username = None
    while username is None:
        username = login()

    end = False
    while not end:
        logic(username)
        end = input("Enter 1 to continue using the ATM or any other key to end: ") != "1"


main()
