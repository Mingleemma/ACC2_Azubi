# ATM Machine
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Kissme2020@",
  database="instabank"
)

print("******* Welcome to InstaBank ATM *******")



users = [{"username" : "Adwoa", "pin" : 1100, "balance" : 15000}, {"username" : "Kojo", "pin" : 2222, "balance" : 17000}]

def balance(bal):
    print("New balance is GHS:" + str(bal))

def withdrawal(bal, amount):
    print("Your remaining balance is GHS:" + str(bal - amount))

def add_money(bal, amt):
    print("Your new balance is GHS:" + str(bal + amt))

Trials = 3

while Trials != 0:
    for user in users:
        username = input("Enter your username \n")
        if username != user["username"]:
            Trials -= 1
            print("Incorrect Username. You have", Trials, "trials remaining")
        else:
            pin = int(input("Enter Your 4 digit Pin : \n"))
            if pin != user["pin"]:
                Trials -= 1
                print("Incorrect Pin Code. You have", Trials, "trials remaining")
            else:
                while True:
                    userChoice = input("Select an Option:\n1: Deposit \n2: Withdraw \n3: Check Balance\n")
                    if userChoice == "1":
                        userDeposit = input("Enter the amount you want to deposit: \n")
                        add_money(user["balance"], int(userDeposit))
                        # print(userDeposit, "GHS Have Been Deposited Into Your Account")
                        userExit = input("Would you like to perform another transaction? y/n: ")
                        if userExit == "n":
                            print("Thank you for banking with InstaBank")
                            exit()  
                        else:
                            continue
                    elif userChoice == "2":
                        userWithdraw = input("Enter the amount you want to withdraw: \n")
                        # print("You have withdrawn GHS", userWithdraw)
                        withdrawal(user["balance"], int(userWithdraw))
                        userExit = input("Would you like to perform another transaction? y/n: ")
                        if userExit == "n":
                            print("Thank you for banking with InstaBank")
                            exit()  
                        else:
                            continue
                    elif userChoice == "3":
                        balance(user["balance"]) 
                        userExit = input("Would you like to perform another transaction? y/n: ")
                        if userExit == "n":
                            print("Thank you for banking with InstaBank")
                            exit()  
                        else:
                            continue
                    # else:
                    #     pass

            #  userExit = input("Would you like to perform another transaction? y/n: ")
            #  if userExit == "n":
            #       print("Thank you for banking with InstaBank")
            #       break  
            #   else:
            #       continue




            #if pin != userPin:
                #Trials -= 1
                #print("Incorrect Pin Code. You Have", Trials, "trials remaining ")
            #else:
                #userChoice = input("1: Deposit or 2: Withdraw or 3: Check Balance: ")
        #         if userChoice == "1":
        #             userDeposit = input("Enter the amount you want to deposit: \n")
        #             print(userDeposit, "GHS Have Been Deposited Into Your Account")
        #         elif userChoice == "2":
        #             userWithdraw = input("Enter the amount you want to withdraw: \n")
        #             print("You have withdrawn GHS", userWithdraw)
        #         elif userChoice == "3":
        #             pass 
        # userExit = input("Would you like to perform another transaction? y/n: ")
        # if userExit == "n":
        #     print("Thank you for banking with InstaBank")
        #     break  
        # else:
        #     continue    
        

