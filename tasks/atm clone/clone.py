# python 3.9
# cloning the operations of an ATM

# Dictionary of registered users imported from bank database
userData = {
    'thebe': {'username': 'thebe', 'pin': '2268', 'balanceGHS': '14_863.54', 'balanceUSD': '0.00'},
    'mayor': {'username': 'mayor', 'pin': '8438', 'balanceGHS': '7_186.96', 'balanceUSD': '12.75'},
    'flysiifu': {'username': 'flysiifu', 'pin': '0336', 'balanceGHS': '3_043.12', 'balanceUSD': '36.84'},
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
        else:
            statOpt = "What period should the statement cover?"
            statOpt += "\n1 - Last 7 days \t 2 - Last 30 days \t 3 - Last 3 months\n"
            statReq = input(statOpt)
            statReq = str(statReq)


