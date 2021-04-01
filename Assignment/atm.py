user = {
    'pin': '0000',
    'balance': {'GHS': 140, 'USD': 0},
}

def welcome():
    print(
        "\n\nWelcome\n"
        "Please\n"
    )
    
    pin = input("Enter your pin: ")
    check_pin(pin)


def check_pin(pin):
    if pin == user['pin']:
        operations()
    else:
        print('wrong pin entered')

def operations():
    loop_operations = True
    while loop_operations:
        print(
            "1. Withdraw Money\n"
            "2. Check Balance\n"
            "3. Exit\n"
        )

        option = input("Option: ")

        if option == "1":

            print(
                "1. Cedi Account\n"
                "2. Dollar Account\n"
                "3. Quit\n"
            )

            account_type = input("Option: ")

            if account_type == "1":

                withdrawal_amount = input("How much do you want to withdraw: ")
                if int(withdrawal_amount) <= user['balance']['GHS']:
                    user['balance']['GHS'] = user['balance']['GHS'] - \
                        int(withdrawal_amount)

                    print(
                        "Do you want a receipt printed for you?\n"
                        "1. Yes\n"
                        "2. No\n"
                    )

                    receipt = input("Option: ")

                    if receipt == "1":
                        print_receipt(withdrawal_amount)
                    elif receipt == "2":
                        print("Thank you for your transaction!\n")
                    else:
                        print("Invalid input entered!\n")

                else:
                    print("Insufficient funds!")

            elif account_type == "2":

                withdrawal_amount = input("How much do you want to withdraw: ")
                if int(withdrawal_amount) <= user['balance']['USD']:
                    user['balance']['USD'] = user['balance']['USD'] - \
                        int(withdrawal_amount)

                    print(
                        "Do you want a receipt printed for you?\n"
                        "1. Yes\n"
                        "2. No\n"
                    )

                    receipt = input("Option: ")

                    if receipt == "1":
                        print_receipt(withdrawal_amount)
                    elif receipt == "2":
                        print("Thank you for your transaction!\n")
                    else:
                        print("Invalid input entered!\n")

                else:
                    print("Insufficient funds!")

            elif account_type == "3":
                pass
            else:
                print("Invalid input entered!\n")

        elif option == "2":

            ghs_balance = f"GHS: {user['balance']['GHS']}\n"
            usd_balance = f"USD: {user['balance']['USD']}\n"

            print(
                "Current Balance\n"
                "Your current balance is: \n" +
                ghs_balance + usd_balance
            )

        elif option == "3":
            print("Thanks for passing by!")
            loop_operations = False

        else:
            print("Invalid input entered!\n")


def print_receipt(amount_withdrawn):
    """
    A function to print transaction receipt
    :param amount_withdrawn: amount withdrawn from account
    :return:
    """
    withdrawn = f"Amount withdrawn: {amount_withdrawn}\n"
    ghs_balance = f"GHS: {user['balance']['GHS']}\n"
    usd_balance = f"USD: {user['balance']['USD']}\n"

    print(
        "Current Balance\n" +
        withdrawn +
        "Your current balance is: \n" +
        ghs_balance + usd_balance
    )


if welcomename == '__main__':
    while 1:
        welcome()
