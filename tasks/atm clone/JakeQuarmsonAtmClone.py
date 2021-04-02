# python 3.9
# cloning the operations of an ATM

# import system module to stop running programme
import sys

# Dictionary of registered users imported from bank database
userData = {
    'thebe': {'username': 'thebe', 'pin': '2268', 'balanceGHS': 14_863.54, 'balanceUSD': 150.00},
    'mayor': {'username': 'mayor', 'pin': '8438', 'balanceGHS': 7_186.96, 'balanceUSD': 12.75},
    'flysiifu': {'username': 'flysiifu', 'pin': '0336', 'balanceGHS': 3_043.12, 'balanceUSD': 36.84},
    }

# request for username
login = input("Please enter your username:\n ")
while login not in userData:
    login = input("The username you entered does not exist, please re-enter:\n ")

# request for pin
print()

pinCode = input("Please enter four-digit pin:\n ")
# error when pin entered does not match username
while pinCode not in userData[login]['pin']:
    print()
    pinCode = input("The pin you entered is incorrect. Please re-enter:\n ")

# function for user choice for another transaction
def pester():
    print()
    menu = "Would you like to perform another transaction?"
    menu += "\n 1 - Yes \t 2 - No\n"
    menu = input(menu)
    menu = str(menu)

    while menu != "1" or menu != "2":

        # Return to main menu if user inputs 1
        if menu == "1":
            mainmenu()

        # exit the programme if user enters 2
        elif menu == "2":
            print("Goodbye!")
            sys.exit()

        # pester user to make right choice
        else:
            menu = "Would you like to perform another transaction?"
            menu += "\n 1 - Yes \t 2 - No\n"
            menu = input(menu)
            menu = str(menu)

# function for ATM operations
def mainmenu():
    while True:
        # welcome screen
        print()
        options = "Welcome! What do you want to do today?"
        options += "\n1 - View Balance \t 2 - Withdraw Funds \t 3 - Request Statement \t 4 - Exit\n "

        # user input preferred action
        action = input(options)
        action = str(action)

        # Viewing user balance
        if action == "1":
            # balance variables retrieve balance from dictionary
            balanceGHS = userData[login]['balanceGHS']
            balanceUSD = userData[login]['balanceUSD']
            print()
            print("Your available balance is:")
            print(f"GHS{balanceGHS}")
            print(f"USD{balanceUSD}")
            pester()

        # requesting bank statement
        elif action == "3":
            print()
            statOpt = "What period should the statement cover?"
            statOpt += "\n1 - Last 7 days \t 2 - Last 30 days \t 3 - Last 3 months\n"
            statReq = input(statOpt)
            statReq = str(statReq)

            while statReq != "1" or statReq != "2" or statReq != "3":
                if statReq == "1" or statReq == "2" or statReq == "3":
                    print("You would receive your statement within three business days")
                    break
                # invalid input so question asked again
                else:
                    statOpt = "What period should the statement cover?"
                    statOpt += "\n1 - Last 7 days \t 2 - Last 30 days \t 3 - Last 3 months\n"
                    statReq = input(statOpt)
                    statReq = str(statReq)
            pester()

        # withdrawing funds
        elif action == "2":
            withOpt = "Which account do you wish to withdraw from?"
            withOpt += "\n1 - Cedi Account \t 2 - Dollar Account\n"
            withReq = input(withOpt)
            withReq = str(withReq)

            while withReq != "1" or withReq != "2":
                # Cedi account chosen
                if withReq == "1":
                    withAmt = input("What amount do you wish to withdraw?\n ")
                    withAmt = int(withAmt)

                    # temporary balance to check if minumum balance is met
                    tmpBal = int(userData[login]['balanceGHS']) - withAmt
                    if tmpBal >= 5:
                        askRec = "Do you want a receipt for this transaction?"
                        askRec += "\n1 - Yes \t 2 - No\n"
                        confRec = input(askRec)
                        if confRec == "1":
                            print("Please wait for your receipt.")
                            print("Please take your cash.")
                            # User balance updated
                            userData[login]['balanceGHS'] = tmpBal
                            break
                        else:
                            print("Please take your cash.")
                            userData[login]['balanceGHS'] = tmpBal
                            break
                    # Minimum balance check not met
                    else:
                        print("Your balance is insufficient.\n Please enter a different amount.")

                # Dollar account chosen
                elif withReq == "2":
                    withAmt = input("What amount do you wish to withdraw?\n ")
                    withAmt = int(withAmt)
                    tmpBal = int(userData[login]['balanceUSD']) - withAmt
                    if tmpBal >= 2:
                        askRec = "Do you want a receipt for this transaction?"
                        askRec += "\n1 - Yes \t 2 - No\n"
                        confRec = input(askRec)
                        if confRec == "1":
                            print("Please wait for your receipt.")
                            print("Please take your cash.")
                            # User balance updated
                            userData[login]['balanceUSD'] = tmpBal
                            break
                        else:
                            print("Please take your cash.")
                            userData[login]['balanceUSD'] = tmpBal
                            break
                    # Minimum balance check not met
                    else:
                        print("Your balance is insufficient.\n Please enter a different amount.")

                # Returns withdrawal menu if invalid option chosen
                else:
                    withOpt = "Which account do you wish to withdraw from?"
                    withOpt += "\n1 - Cedi Account \t 2 - Dollar Account\n"
                    withReq = input(withOpt)
                    withReq = str(withReq)
            pester()

        # Exits the programme
        elif action == "4":
            print("Goodbye!")
            sys.exit()

        # Returns user to main menu if invalid option chosen
        else:
            mainmenu()


# Running the programme
mainmenu()
