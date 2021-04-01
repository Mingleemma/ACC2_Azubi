import json

with open("accounts.json") as accountsfile:
    users = json.load(accountsfile)
    valerr = "Please type a number \n"
    sorry = "Sorry, you do not have enough money in this account\n\n"

    print("\n\nWelcome to Cash Money ATM \n")
    while True:
        username = input("Please type your username to log in: \n")
        for user in users:

            if username in user["username"]:
                while True:
                    pin = input("Please type your pin: \n")
                    try:

                        if int(pin) == user["pin"]:
                            print("You have successfully logged in")
                            while True:
                                action = input("1: Check Balance "
                                               "\n2: Withdraw Money \nEnter Option Here: \n3: Exit \n")
                                try:
                                    if int(action) == 1:
                                        print("Your balance is \nGHS: {}\nUSD: {} \n\n".format(user["balance"]["GHS"],
                                                                                               user["balance"]["USD"])
                                              )
                                    elif int(action) == 2:
                                        while True:
                                            currency = input(
                                                "Which account do you want to withdraw from?\n1: GHS\n2: USD\n")
                                            try:
                                                if int(currency) == 1:
                                                    amount = float(input("How much do you want to withdraw?\n"))
                                                    try:
                                                        if amount <= user["balance"]["GHS"]:
                                                            user["balance"]["GHS"] = round((user["balance"]
                                                                                            ["GHS"] - amount), 2)

                                                            print("Your new balance is \nGHS: {}\nUSD: {}\n\n".format(
                                                                user["balance"]["GHS"],
                                                                user["balance"]["USD"])
                                                            )
                                                            break
                                                        else:
                                                            print(sorry)
                                                    except ValueError:
                                                        print(valerr)
                                                elif int(currency) == 2:
                                                    amount = float(input("How much do you want to withdraw?\n"))
                                                    try:
                                                        if amount <= user["balance"]["USD"]:
                                                            user["balance"]["USD"] = round((user["balance"]
                                                                                            ["USD"] - amount), 2
                                                                                           )

                                                            print("Your new balance is \nGHS: {}\nUSD: {} \n\n".format(
                                                                user["balance"]["GHS"],
                                                                user["balance"]["USD"])
                                                            )
                                                            break
                                                        else:
                                                            print(sorry)
                                                    except ValueError:
                                                        print(valerr)
                                            except ValueError:
                                                print(valerr)
                                    elif int(action) == 3:
                                        break
                                except ValueError:
                                    print(valerr)
                            break
                    except ValueError:
                        print("The pin should be a 4 digit number")
                break
