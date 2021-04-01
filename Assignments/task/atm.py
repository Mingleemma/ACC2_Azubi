# ATM app

# declare account balance
balance = 45000

# request pin
print("    Welcome to MAWUBANK ATM    ")
PIN = int(input("Please enter your 4-digit PIN code:..."))

# List Menu
print("       MAWUBANK ATM")
print("""
1)        Balance
2)        Withdraw
3)        Deposit
4)        Quit
""")

# request user option
Option = int(input("Enter Option: "))

# option 1 logic
if Option == 1:
    print("Your balance is GHS " + str(balance))
    Option = int(input("Enter Option: "))

# option 2 logic
if Option == 2:
    print("Your balance is GHS  " + str(balance))
    Withdraw = float(input("Enter Withdraw amount GHS "))
    if Withdraw > 0:
      
        newbalance = (balance - Withdraw)
        print("Your new balance is GHS " + str(newbalance))
        Option = int(input("Enter Option: "))
    elif Withdraw > balance:
        print("Not sufficient funds")
        Option = int(input("Enter Option: "))
    else:
        print("No withdrawal was made")
        print("No was deposit made. Your balance is " + str(balance))
        Option = int(input("Enter Option: "))


#option 3 logic
if Option == 3:
    print("Balance is GHS " + str(balance))
    Deposit = float(input("Enter deposit amount GHS "))
    if Deposit > 0:
        newbalance = (balance + Deposit)
        print("Your deposit was successful. New balance is GHS " + str(newbalance))
        Option = int(input("Enter Option: "))
    else:
        print("No was deposit made. Your balance is " + str(balance))
        Option = int(input("Enter Option: "))

#option 4 logic
if Option == 4:
    print("Thank you for doing business with us. Have a sunny day :)")
    exit()
