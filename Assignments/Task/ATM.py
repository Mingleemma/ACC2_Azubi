users = {
    "username": "trial",
    "pin": 0000,
    "balance": {
        "GHS": 140.00,
        "USD": 0.00
    }
}
valerr = "Please type a number \n"

print("Welcome to Cash Money ATM \n\n")
while True:
    username = input("Please type your username to log in: \n")
    if username == users["username"]:
        while True:
            password = input("Please type your pin: \n")
            try:

                if int(password) == users["pin"]:
                    print("You have successfully logged in")
                    while True:
                        action = input("1: Check Balance "
                                       "\n2: Withdraw Money \nEnter Option Here: \n3: Exit \n")
                        try:
                            if int(action) == 1:
                                print("Your balance is \nGHS: {}\nUSD: {}".format(users["balance"]["GHS"],
                                                                                  users["balance"]["USD"]))
                            elif int(action) == 2:
                                while True:
                                    currency = input("Which account do you want to withdraw from?\n1: GHS\n2: USD\n")
                                    try:
                                        if int(currency) == 1:
                                            amount = float(input("How much do you want to withdraw?\n"))
                                            try:
                                                if amount <= users["balance"]["GHS"]:
                                                    users["balance"]["GHS"] = round((users["balance"]
                                                                                     ["GHS"] - amount), 2)
                                                    print("Your balance is \nGHS: {}\nUSD: {}".format(users["balance"]
                                                                                                      ["GHS"],
                                                                                                      users["balance"][
                                                                                                          "USD"]))
                                                    break
                                                else:
                                                    print("Sorry, you do not have enough money in your account")
                                            except ValueError:
                                                print(valerr)
                                        elif int(currency) == 2:
                                            amount = float(input("How much do you want to withdraw?\n"))
                                            try:
                                                if amount <= users["balance"]["USD"]:
                                                    users["balance"]["GHS"] = round((users["balance"]
                                                                                     ["USD"] - amount), 2)
                                                    print("Your balance is \nGHS: {}\nUSD: {}".format(
                                                        users["balance"]["GHS"],
                                                        users["balance"]["USD"]))
                                                    break
                                                else:
                                                    print("Sorry, you do not have enough money in your account")
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
