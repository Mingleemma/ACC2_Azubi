# python 3.9
# cloning the operations of an ATM

# Dictionary of registered users imported from bank database
userData = {
    'thebe': {'username': 'thebe', 'pin': '2268', 'balanceGHS': 14_863.54, 'balanceUSD': 0.00},
    'mayor': {'username': 'mayor', 'pin': '8438', 'balanceGHS': 7_186.96, 'balanceUSD': 12.75},
    'flysiifu': {'username': 'flysiifu', 'pin': '0336', 'balanceGHS': 3_043.12, 'balanceUSD': 36.84},
    }

# request for username
login = input("Please enter your username:\n ")
while login not in userData:
    login = input("The username you entered does not exist, please re-enter:\n ")

# request for pin
pinCode = input("Please enter four-digit pin:\n ")
# error when pin entered does not match username
while pinCode not in userData[login]['pin']:
    pinCode = input("The pin you entered is incorrect. Please re-enter:\n ")

# successful login and menu
options = "Welcome! What do you want to do today?"
options += "\n1 - View Balance \t 2 - Withdraw Funds \t 3 - Request Statement\n "

# user input preferred action
action = input(options)
action = str(action)


# Viewing user balance
if action == "1":
    balanceGHS = userData[login]['balanceGHS']
    balanceUSD = userData[login]['balanceUSD']
    print("Your available balance is:")
    print(f"GHS{balanceGHS}")
    print(f"USD{balanceUSD}")

# requesting bank statement
if action == "3":
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
# withdrawing funds
if action == "2":
    withOpt = "Which account do you wish to withdraw from?"
    withOpt += "\n1 - Cedi Account \t 2 - Dollar Account\n"
    withReq = input(withOpt)
    withReq = str(withReq)
    while withReq != "1" or withReq != "2":
        if withReq == "1":
            withAmt = input("What amount do you wish to withdraw?\n ")
            withAmt = int(withAmt)
            tmpBal = int(userData[login]['balanceGHS']) - withAmt
            if tmpBal >= 5:
                askRec = "Do you want a receipt for this transaction?"
                askRec += "\n1 - Yes \t 2 - No\n"
                confRec = input(askRec)
                if confRec == "1":
                    print("Please wait for your receipt.")
                    print("Please take your cash.")
                    userData[login]['balanceGHS'] = tmpBal
                    break
                else:
                    print("Please take your cash.")
                    userData[login]['balanceGHS'] = tmpBal

            else:
                print("Your balance is insufficient.\n Please enter a different amount.")

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
                    userData[login]['balanceUSD'] = tmpBal
                    break
                else:
                    print("Please take your cash.")
                    userData[login]['balanceUSD'] = tmpBal
            else:
                print("Your balance is insufficient.\n Please enter a different amount.")

        else:
            withOpt = "Which account do you wish to withdraw from?"
            withOpt += "\n1 - Cedi Account \t 2 - Dollar Account\n"
            withReq = input(withOpt)
            withReq = str(withReq)
