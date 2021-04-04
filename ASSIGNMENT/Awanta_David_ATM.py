# This is to allow date and time be printed on the receipt
# .strf allows me structure the date and time
import datetime

today = datetime.time()
full_date = today.strftime("%d/%m/%Y %H:%M:%S")

# A dictionary list storing the details of the users
user_1 = {"username": "DAVID", "pin": 2248, "Balance": {"GHS": 1000}}
user_2 = {"username": "JENNIFER", "pin": 5902, "Balance": {"GHS": 3500}}
user_3 = {"username": "WICK", "pin": 4921, "Balance": {"GHS": 500}}
count = 0

# This prints a start-up message
print("************************")
print("*    ACC2 AZUBI ATM    *")
print("************************")

# A loop to ensure user enters their correct name and inputs their pin
while True:
    user = input("\nEnter Your Username: ")
    user = user.upper()
    if user == user_1["username"] or user == user_2["username"] or user == user_3["username"]:
        print(user + " YOU MAY PROCEED...")
    else:
        print("INCORRECT USERNAME!!!")
    while user == user_1["username"] or user == user_2["username"] or user == user_3["username"]:
        pin = int(input("\nEnter Your ATM PIN: "))

# FOR THE FIRST USER
# The user's name and pin must correspond to move on to select their transaction to be performed
        if user == user_1["username"] and pin == 2248:
            print("WELCOME  " + user + "\nYOU ARE LOGGED IN, CONTINUE YOUR TRANSACTION...")
            while user == user_1["username"] and pin == 2248:
                print("\nCHOOSE YOUR TRANSACTION TYPE: ")
                print("1. WITHDRAWAL \n2. CHECK BALANCE")
# A function balance to calculate amount left after withdrawal

                def balance():
                    n = 1000 - int(amount)
                    return n

                selection = int(input("\nCHOICE: "))
                if selection == 1:
                    amount = int(input("\nENTER AMOUNT TO WITHDRAW: "))

                    original_balance = 1000
                    if amount <= original_balance:
                        print("\nAN AMOUNT OF GHS" + str(amount) + " HAS BEEN WITHDRAWN")
                        print("\nYOUR NEW BALANCE IS: ")
                        print(balance())
                    else:
                        print("\nINSUFFICIENT FUNDS!!!")
# If a withdrawal is made you choose to print a receipt or not
                    while amount <= original_balance:
                        response = input("\nDO YOU WANT A RECEIPT? (Y/N): ")
                        response = response.upper()
                        if response == "Y":
                            print()
                            print("****************************")
                            print("*         RECEIPT          *")
                            print("****************************")
                            print("\nTRANSACTION IS NOW COMPLETE")
                            print("NAME:")
                            print(user_1["username"])
                            print("AMOUNT WITHDRAWN:")
                            print(amount)
                            print("YOUR BALANCE IS:")
                            print(balance())
                            print("DATE & TIME:")
                            print(full_date)
                            print("\nTHANK YOU FOR BANKING WITH ACC2 AZUBI !!!")
                            break
                        elif response != "Y":
                            print("EXITING>>>")
                        break
# the break ends a specific sequence
# This gives the user an option to do another withdrawal or exit the system.
                    while selection == 1:
                        print("\nDO YOU WANT TO WITHDRAW AGAIN? OR QUIT")
                        answer = input("\nENTER (W) to continue withdrawal OR ENTER (Q) to quit: ")
                        answer = answer.upper()

# A function new_balance to subtract the new amount withdrawn from balance obtained after the first withdrawal

                        def new_balance():
                            y = (balance()) - int(new_amount)
                            return y
                        if answer == "W":
                            print("LOADING>>>")
                            print("\nCHOOSE YOUR TRANSACTION TYPE: ")
                            print("1. WITHDRAWAL ")

                            selection = int(input("\nCHOICE: "))
                            if selection == 1:
                                new_amount = int(input("\nENTER AMOUNT TO WITHDRAW: "))

                                original_balance_x = (balance())
                                if amount <= original_balance_x:
                                    print("\nAN AMOUNT OF GHS" + str(new_amount) + " HAS BEEN WITHDRAWN")
                                    print("\nYOUR NEW BALANCE IS: ")
                                    print(new_balance())
                                else:
                                    print("\nINSUFFICIENT FUNDS!!!")

                                while amount <= original_balance_x:
                                    response = input("\nDO YOU WANT A RECEIPT? (Y/N): ")
                                    response = response.upper()
                                    if response == "Y":
                                        print()
                                        print("****************************")
                                        print("*         RECEIPT          *")
                                        print("****************************")
                                        print("\nTRANSACTION IS NOW COMPLETE")
                                        print("NAME:")
                                        print(user_1["username"])
                                        print("AMOUNT WITHDRAWN:")
                                        print(new_amount)
                                        print("YOUR BALANCE IS:")
                                        print(new_balance())
                                        print("DATE & TIME:")
                                        print(full_date)
                                        print("\nTHANK YOU FOR BANKING WITH ACC2 AZUBI !!!")
                                        break
                                    elif response != "Y":
                                        print("EXITING>>>")
                                        break
                                    break
# After the second withdrawal the system closes
                            if answer == "W":
                                print("\nYOU HAVE EXCEEDED YOUR TOTAL NUMBER OF WITHDRAWALS FOR TODAY ")
                                break
                        if answer == "Q":
                            print("EXITING>>>")
                            break

                    break
# If the user does no withdrawal and just checks their balance
                if selection == 2:
                    print(user_1["Balance"])
                    break
                break
            break

# FOR THE SECOND USER
# Same line of codes used for the first user was repeated for the third user.
        if user == user_2["username"] and pin == 5902:
            print("WELCOME  " + user + "\nYOU ARE LOGGED IN, CONTINUE YOUR TRANSACTION...")
            while user == user_2["username"] and pin == 5902:
                print("\nCHOOSE YOUR TRANSACTION TYPE: ")
                print("1. WITHDRAWAL \n2. CHECK BALANCE")

                def balance_1():
                    n = 3500 - int(amount)
                    return n

                selection = int(input("\nCHOICE: "))
                if selection == 1:
                    amount = int(input("\nENTER AMOUNT TO WITHDRAW: "))

                    original_balance_1 = 3500
                    if amount <= original_balance_1:
                        print("\nAN AMOUNT OF GHS" + str(amount) + " HAS BEEN WITHDRAWN")
                        print("\nYOUR NEW BALANCE IS: ")
                        print(balance_1())

                    else:
                        print("\nINSUFFICIENT FUNDS!!!")

                    while amount <= original_balance_1:
                        response = input("\nDO YOU WANT A RECEIPT? (Y/N): ")
                        response = response.upper()
                        if response == "Y":
                            print()
                            print("****************************")
                            print("*         RECEIPT          *")
                            print("****************************")
                            print("\nTRANSACTION IS NOW COMPLETE")
                            print("NAME:")
                            print(user_2["username"])
                            print("AMOUNT WITHDRAWN:")
                            print(amount)
                            print("YOUR BALANCE IS:")
                            print(balance_1())
                            print("DATE & TIME:")
                            print(full_date)
                            print("\nTHANK YOU FOR BANKING WITH ACC2 AZUBI !!!")
                            break
                        elif response != "Y":
                            print("EXITING>>>")
                        break
                    while selection == 1:
                        print("\nDO YOU WANT TO WITHDRAW AGAIN? OR QUIT")
                        answer = input("\nENTER (W) to continue withdrawal OR ENTER (Q) to quit: ")
                        answer = answer.upper()

                        def new_balance1():
                            y = (balance_1()) - int(new_amount)
                            return y
                        if answer == "W":
                            print("LOADING>>>")
                            print("\nCHOOSE YOUR TRANSACTION TYPE: ")
                            print("1. WITHDRAWAL ")

                            selection = int(input("\nCHOICE: "))
                            if selection == 1:
                                new_amount = int(input("\nENTER AMOUNT TO WITHDRAW: "))

                                original_balance_x = (balance_1())
                                if amount <= original_balance_x:
                                    print("\nAN AMOUNT OF GHS" + str(new_amount) + " HAS BEEN WITHDRAWN")
                                    print("\nYOUR NEW BALANCE IS: ")
                                    print(new_balance1())
                                else:
                                    print("\nINSUFFICIENT FUNDS!!!")
                                while amount <= original_balance_x:
                                    response = input("\nDO YOU WANT A RECEIPT? (Y/N): ")
                                    response = response.upper()
                                    if response == "Y":
                                        print()
                                        print("****************************")
                                        print("*         RECEIPT          *")
                                        print("****************************")
                                        print("\nTRANSACTION IS NOW COMPLETE")
                                        print("NAME:")
                                        print(user_2["username"])
                                        print("AMOUNT WITHDRAWN:")
                                        print(new_amount)
                                        print("YOUR BALANCE IS:")
                                        print(new_balance1())
                                        print("DATE & TIME:")
                                        print(full_date)
                                        print("\nTHANK YOU FOR BANKING WITH ACC2 AZUBI !!!")
                                        break
                                    elif response != "Y":
                                        print("EXITING>>>")
                                        break
                                    break
                            if answer == "W":
                                print("YOU HAVE EXCEEDED YOUR TOTAL NUMBER OF WITHDRAWALS FOR TODAY ")
                                break
                        if answer == "Q":
                            print("EXITING>>>")
                            break

                    break
                if selection == 2:
                    print(user_2["Balance"])
                    break
                break
            break

# FOR THE THIRD USER
# Same line of codes used for the first user was repeated for the third user.
        if user == user_3["username"] and pin == 4921:
            print("WELCOME  " + user + "\nYOU ARE LOGGED IN, CONTINUE YOUR TRANSACTION...")
            while user == user_3["username"] and pin == 4921:
                print("\nCHOOSE YOUR TRANSACTION TYPE: ")
                print("1. WITHDRAWAL \n2. CHECK BALANCE")

                def balance_2():
                    n = 500 - int(amount)
                    return n

                selection = int(input("\nCHOICE: "))
                if selection == 1:
                    amount = int(input("\nENTER AMOUNT TO WITHDRAW: "))

                    original_balance_2 = 500
                    if amount <= original_balance_2:
                        print("\nAN AMOUNT OF GHS" + str(amount) + " HAS BEEN WITHDRAWN")
                        print("\nYOUR NEW BALANCE IS: ")
                        print(balance_2())
                    else:
                        print("\nINSUFFICIENT FUNDS!!!")

                    while amount <= original_balance_2:
                        response = input("\nDO YOU WANT A RECEIPT? (Y/N): ")
                        response = response.upper()
                        if response == "Y":
                            print()
                            print("****************************")
                            print("*         RECEIPT          *")
                            print("****************************")
                            print("\nTRANSACTION IS NOW COMPLETE")
                            print("NAME:")
                            print(user_3["username"])
                            print("AMOUNT WITHDRAWN:")
                            print(amount)
                            print("YOUR BALANCE IS:")
                            print(balance_2())
                            print("DATE & TIME:")
                            print(full_date)
                            print("\nTHANK YOU FOR BANKING WITH ACC2 AZUBI !!!")
                            break
                        elif response != "Y":
                            print("EXITING>>>")
                        break
                    while selection == 1:
                        print("\nDO YOU WANT TO WITHDRAW AGAIN? OR QUIT")
                        answer = input("\nENTER (W) to continue withdrawal OR ENTER (Q) to quit: ")
                        answer = answer.upper()

                        def new_balance2():
                            y = (balance_2()) - int(new_amount)
                            return y
                        if answer == "W":
                            print("LOADING>>>")
                            print("\nCHOOSE YOUR TRANSACTION TYPE: ")
                            print("1. WITHDRAWAL ")

                            selection = int(input("\nCHOICE: "))
                            if selection == 1:
                                new_amount = int(input("\nENTER AMOUNT TO WITHDRAW: "))

                                original_balance_x = (balance_2())
                                if amount <= original_balance_x:
                                    print("\nAN AMOUNT OF GHS" + str(new_amount) + " HAS BEEN WITHDRAWN")
                                    print("\nYOUR NEW BALANCE IS: ")
                                    print(new_balance2())
                                else:
                                    print("\nINSUFFICIENT FUNDS!!!")
                                while amount <= original_balance_x:
                                    response = input("\nDO YOU WANT A RECEIPT? (Y/N): ")
                                    response = response.upper()
                                    if response == "Y":
                                        print()
                                        print("****************************")
                                        print("*         RECEIPT          *")
                                        print("****************************")
                                        print("\nTRANSACTION IS NOW COMPLETE")
                                        print("NAME:")
                                        print(user_3["username"])
                                        print("AMOUNT WITHDRAWN:")
                                        print(new_amount)
                                        print("YOUR BALANCE IS:")
                                        print(new_balance2())
                                        print("DATE & TIME:")
                                        print(full_date)
                                        print("\nTHANK YOU FOR BANKING WITH ACC2 AZUBI !!!")
                                        break
                                    elif response != "Y":
                                        print("EXITING>>>")
                                        break
                                    break
                            if answer == "W":
                                print("YOU HAVE EXCEEDED YOUR TOTAL NUMBER OF WITHDRAWALS FOR TODAY ")
                                break
                        if answer == "Q":
                            print("EXITING>>>")
                            break
                    break
                if selection == 2:
                    print(user_3["Balance"])
                    break
                break
            break
# If the user enters a wrong pin, it loops and asks the user to enter a pin again
        else:
            count += 1
            print(user + " YOUR ATM PIN IS INCORRECT!!!")
# the count helps determine the number of times the user will enter a pin again
# when the count gets to three after failed pin entries, the card locks and exits
        if count == 3:
            print("\nTHREE UNSUCCESSFUL TRIES \nYOUR ATM CARD IS BLOCKED")
            print("VISIT THE NEAREST ACC2 AZUBI BANK TO UNLOCK YOUR CARD..")
            print()
            break
    break
