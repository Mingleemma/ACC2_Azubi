# import the json library so we can pull data fron the json file with the user and account details
import json


# function to update the json file with new account details after withdrawals
def update_account():
    with open("accounts.json", "w") as newacc:
        json.dump(users, newacc)


# print the balance of the current user
def print_balance():
    print("Your new balance is \nGHS: {}\nUSD: {}\n\n".format(
        user["balance"]["GHS"],
        user["balance"]["USD"])
    )


# check if the user has enough balance and make a withdrawal
def withdraw_money(cur, amo):
    try:
        if float(amo) <= user["balance"][cur]:
            user["balance"][cur] = round((user["balance"]
                                          [cur] - amount), 2)
            print_balance()
            update_account()
        else:
            print(sorry)
    except ValueError:
        print(valerr)


# start the program
if __name__ == '__main__':
    # open the json file
    with open("accounts.json", "r") as accountsfile:
        users = json.load(accountsfile)
        valerr = "Please type a number \n"
        sorry = "Sorry, you do not have enough money in this account\n\n"
        print("\nWelcome to MY ATM")
        # keep the program running until an arbitrary break is called
        while True:
            username = input("\n\nPlease type your username to log in: \n").lower()
            # loop through users to see if the name given by the user exists
            for user in users:
                if username in user["username"]:
                    pin = input("Please type your pin: \n")
                    try:
                        if int(pin) == user["pin"]:
                            print("You have successfully logged in")
                            while True:
                                action = input("1: Check Balance "
                                               "\n2: Withdraw Money \n3: Exit \nEnter Option Here: \n")
                                try:
                                    if int(action) == 1:
                                        print_balance()
                                    elif int(action) == 2:
                                        while True:
                                            currency = input(
                                                "Which account do you want to withdraw from?\n1: GHS\n2: USD\n")
                                            try:
                                                if int(currency) == 1:
                                                    denomination = "GHS"
                                                elif int(currency) == 2:
                                                    denomination = "USD"
                                                try:
                                                    amount = float(input("How much do you want to withdraw?\n"))
                                                except ValueError:
                                                    print("Please type a number")
                                                withdraw_money(denomination, amount)
                                                break
                                            except ValueError:
                                                print(valerr)
                                    elif int(action) == 3:
                                        break
                                except ValueError:
                                    print(valerr)
                            break
                        else:
                            print("Sorry, wrong password. Please retry. \n")
                    except ValueError:
                        print("The pin should be a 4 digit number")
