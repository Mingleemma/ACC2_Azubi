#!/usr/bin/env python
# Python dictionary key-value pair to hold user information and account balance in GHS and USD

user1 = {
    'username': 'user1',
    'pin': '2106',
    'balance': {'GHS': 140, 'USD': 40},  # nested dictionary (dictionary inside a dictionary)
}

user2 = {
    'username': 'user2',
    'pin': '2021',
    'balance': {'GHS': 850, 'USD': 200},  # nested dictionary (dictionary inside a dictionary)
}

user3 = {
    'username': 'user3',
    'pin': '1741',
    'balance': {'GHS': 540, 'USD': 300},  # nested dictionary (dictionary inside a dictionary)
}

all_users = [user1, user2, user3]


def welcome():
    """
    A function to welcome users when they start the application and checks if they have the correct pin
    :return: returns nothing
    """

    print(
        "\n\nWelcome\n"
        "Please enter your pin to begin\n"
    )

    pin = input("Enter your pin: ")

    # call check_pin function to check if the user entered the correct pin
    check_pin(pin)


def check_pin(pin):
    """
    A function to check validity of atm pin

    :param pin: ATM pin
    :return:
    """

    for user in all_users:
        if pin == user['pin']:
            # if the user's pin is correct then allow the user to perform atm operations by calling the operation()
            # function
            operations(user)

    print('wrong pin entered')


def operations(user):
    """
    A function to guide users to perform certain ATM operations

    :return:
    """

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
                    user['balance']['GHS'] = user['balance']['GHS'] - int(withdrawal_amount)

                    print(
                        "Do you want a receipt printed for you?\n"
                        "1. Yes\n"
                        "2. No\n"
                    )

                    receipt = input("Option: ")

                    if receipt == "1":
                        print_receipt(withdrawal_amount, user)
                    elif receipt == "2":
                        print("Thank you for your transaction!\n")
                    else:
                        print("Invalid input entered!\n")

                else:
                    print("Insufficient funds!")

            elif account_type == "2":

                withdrawal_amount = input("How much do you want to withdraw: ")
                if int(withdrawal_amount) <= user['balance']['USD']:
                    user['balance']['USD'] = user['balance']['USD'] - int(withdrawal_amount)

                    print(
                        "Do you want a receipt printed for you?\n"
                        "1. Yes\n"
                        "2. No\n"
                    )

                    receipt = input("Option: ")

                    if receipt == "1":
                        print_receipt(withdrawal_amount, user)
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


def print_receipt(amount_withdrawn, user):
    """
    A function to print transaction receipt

    :param user: user details
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


if __name__ == '__main__':

    # while 1 keeps the program running forever
    while 1:
        welcome()
