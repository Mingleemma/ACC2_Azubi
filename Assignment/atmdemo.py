#Python code mimicking the process of an atm
#defining userdata
userdata = {
    'lnoel': {'username': 'lnoel', 'pin': '5678', 'balance': {'GHS':8500}},
    'freda': {'username': 'fredaa', 'pin': '9023', 'balance': {'GHS':19450}},
    'rubyl': {'username': 'rubyl', 'pin': '3322', 'balance': {'GHS':300}},
    'gerta': {'username': 'gerta', 'pin': '5723', 'balance': {'GHS':40000}},
}
#Welcome page
print("Welcome to Banksy!")
username = input("Please enter your username:\n")
username = username.lower()
#Username attempts limited to 2
username_attempts = 2
while username not in userdata:
    username = input("Incorrect username, please re-enter:\n")
if username_attempts == 0:
    isWorking = False
#defining password login details
password = input("Please enter your 4 digit pin:\n")
password_attempts = 2
while password not in userdata[username]['pin']:
    password = input("Incorrect pin, please re-enter:\n")
if password_attempts == 0:
    isWorking = False
#transaction values are assigned to make process simple
transaction = ["1","2","3","4","5","6"]
print("What would you like to do today?\n")
print("1. Balance enquiry")
print("2. Withdraw money")
print("3. Deposit")
print("4. Change pin")
print("5. Transfer money")
print("6. Exit")
trans = input("Transaction number:\n")
#defining actions to be carried per transaction value
#defining balance enquiry
if trans == "1":
    statement = input("Would you like a receipt?\n")
    if statement == "yes":
        print("Here is your statement,Thank you for using Banksy!")
    else:
        print("Thank you for using our services, come again!")
#defining withdraw money 
elif trans == "2":
    amount = input("Please enter the amount you want to withdraw:")
    if amount>0:
        print("Please wait as your money loads\n")
        print("Take your cash,Have a nice day!")
    else:
        print("Please enter a valid amount of money\n")
#defining deposit
elif trans == "3":
    deposit = input("Please enter withdrawal amount\n")
    if deposit>0:
        print("Deposit successful")
    else:
        print("Error, please enter valid amount and try again")
#defining change pin
elif trans == "4":
    changepin = input("Please enter your new pin\n")
    if changepin>=0:
        print("Pin succesfully changed")
    else:
        print("Please enter a valid pin\n ")
#defining transfer money
elif trans == "5":
    receipient = input("Please enter receipient username\n")
    receipient = receipient.lower()
    if receipient in userdata:
        transfermoney = input("Enter amount to transfer")
        if transfermoney>0:
            print("Transfer successful.")
        else:
            print("Please enter valid amount")
    else:
        print("Please enter valid username")
#defining transfer process
elif trans == "6":
    print("Are you sure you want to exit? 1-Yes 2-No")
    if quit == "1":
        print("Thank you have a nice day!")
    else:
        print("Choose another transaction")
