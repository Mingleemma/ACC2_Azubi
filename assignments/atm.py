# Alternate ATM Program
# print("********** WELCOME TO ZBANK **********")
# pin = int(input("Enter your pin: \n"))
# if pin == 1122 or 0000:
#     userchoice = input({
#         "1": "Deposit",
#         "2": "Withdraw"})
#     if userchoice == "1":
#         userDeposit = input("Enter the deposit amount: \n")
#         print(userDeposit, "GHS has been deposited into your account")
#     if userchoice == "2":
#         userWithdraw = input("Enter the withdrawal amount: \n")
#         print(userWithdraw, "GHS has been withdrawm from your account")
# else:
#     print("Invalid pin! Try again!")

users = [{"username" : "Adwoa", "pin" : 1100, "balance" : 15000}, {"username" : "Kojo", "pin" : 2222, "balance" : 17000}]

def balance():
    print("New balance is GHS:".format(users["balance"]))

def withdrawal(new, amount):
    if int(amount) <= users["balance"][new]:
        users["balance"][new] = int(users["balance"][new] - amount, 2)
