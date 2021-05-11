#!/usr/bin/python


# creating a lists of users, their PINs
users = ['trial']
pins = ['0000']
GHS = [140]
USD = [0]

# while loop checks existence of the entered username and pin
count = 1
while True:
    user = input('\nENTER USER NAME: ')
    # case sensitivity
    user = user.lower()
    if user in users:
        # first item in list has index 0
        if user == users[0]:
            n = 0
    else:
        print('INVALID USERNAME')
        exit()

    # comparing pin
    pin = (input('\nPLEASE ENTER PIN: '))

    if user == 'user':
        if pin == pins[0]:
            break
    elif pin != pins[0] and count != 3:
        print('WRONG PIN. TRY AGAIN')
        count += 1
        continue

    if pin != pins[0] and count == 3:
        print('YOU HAVE ENTERED THE WRONG PASSWORD THREE TIMES. CONTACT A BANK ASSISTANT TO COLLECT YOUR CARD')
        exit()

    print('-------------------------------')
    print('*******************************')
    print('LOGIN SUCCESSFUL, CONTINUE')
    print(str.capitalize(users[0]), 'welcome to ATM')
    break

# Main menu
while True:
    # selecting currency and atm action to carry out

    print('**************************')
    print('----------ATM SYSTEM-----------')
    account = input('Select account to use: \nGHS__(1) \nUSD__(2) \n:')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) '
                     '\nDeposit__(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
# GHS
    if account == '1':

        valid_responses = ['s', 'w', 'd', 'p', 'q']
        # bank statement
        if response == 's':
            print('---------------------------------------------')
            print('*********************************************')
            print(str.capitalize(users[0]), 'YOU HAVE ', GHS[0], 'GHS IN YOUR ACCOUNT.')
            print('*********************************************')
            print('---------------------------------------------')

        # withdraw cash
        elif response == 'w':
            print('---------------------------------------------')
            print('*********************************************')
            cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
            print('*********************************************')
            print('---------------------------------------------')
            if cash_out % 10 != 0:
                print('------------------------------------------------------')
                print('******************************************************')
                print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10 GHS NOTES OR MUST BE DIVISIBLE BY 10')
                print('******************************************************')
                print('------------------------------------------------------')
            elif cash_out > GHS[0]:
                print('-----------------------------')
                print('*****************************')
                print('YOU HAVE INSUFFICIENT GHS BALANCE')
                print('*****************************')
                print('-----------------------------')

            else:
                GHS[0] = GHS[0] - cash_out
                print('-----------------------------------')
                print('***********************************')
                print('YOUR NEW GHS BALANCE IS: ', GHS[0], 'GHS')
                print('***********************************')
                print('-----------------------------------')

        # deposit cash
        elif response == 'd':
            print()
            print('---------------------------------------------')
            print('*********************************************')
            cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
            print('*********************************************')
            print('---------------------------------------------')
            print()
            if cash_in % 10 != 0:
                print('----------------------------------------------------')
                print('****************************************************')
                print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 GHS NOTES')
                print('****************************************************')
                print('----------------------------------------------------')
            else:
                GHS[0] = GHS[0] + cash_in
                print('----------------------------------------')
                print('****************************************')
                print('YOUR NEW GHS BALANCE IS: ', GHS[0], 'GHS')
                print('****************************************')
                print('----------------------------------------')

        # change pin
        elif response == 'p':

            print('-----------------------------')
            print('*****************************')

            new_pin = str(input('ENTER A NEW PIN: '))

            print('*****************************')
            print('-----------------------------')

            if new_pin != pins[0] and len(new_pin) == 4:

                print('------------------')
                print('******************')

                new_pins = str(input('CONFIRM NEW PIN: '))

                print('*******************')
                print('-------------------')

                if new_pins != new_pin:

                    print('------------')
                    print('************')
                    print('PIN MISMATCH')
                    print('************')
                    print('------------')

                else:
                    pins[0] = new_pin
                    print('NEW PIN SAVED')

            else:
                print('-------------------------------------')
                print('*************************************')
                print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
                print('*************************************')
                print('-------------------------------------')

        # quit
        elif response == 'q':
            exit()

        else:
            print('INVALID INPUT')

    # USD account
    if account == '2':

        if response == 's':
            print('---------------------------------------------')
            print('*********************************************')
            print(str.capitalize(users[0]), 'YOU HAVE ', USD[0], 'USD ON YOUR ACCOUNT.')
            print('*********************************************')
            print('---------------------------------------------')

        # withdraw cash
        elif response == 'w':
            print('---------------------------------------------')
            print('*********************************************')
            cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
            print('*********************************************')
            print('---------------------------------------------')
            if cash_out % 10 != 0:
                print('------------------------------------------------------')
                print('******************************************************')
                print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 USD NOTES OR MUST BE DIVISIBLE BY 10')
                print('******************************************************')
                print('------------------------------------------------------')
            elif cash_out > USD[0]:
                print('-----------------------------')
                print('*****************************')
                print('YOU HAVE INSUFFICIENT USD BALANCE')
                print('*****************************')
                print('-----------------------------')

            else:
                USD[0] = USD[0] - cash_out
                print('-----------------------------------')
                print('***********************************')
                print('YOUR NEW USD BALANCE IS: ', USD[0], 'USD')
                print('***********************************')
                print('-----------------------------------')

        # deposit cash
        elif response == 'd':
            print()
            print('---------------------------------------------')
            print('*********************************************')
            cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
            print('*********************************************')
            print('---------------------------------------------')
            print()
            if cash_in % 10 != 0:
                print('----------------------------------------------------')
                print('****************************************************')
                print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 USD NOTES')
                print('****************************************************')
                print('----------------------------------------------------')
            else:
                USD[0] = USD[0] + cash_in
                print('----------------------------------------')
                print('****************************************')
                print('YOUR NEW USD BALANCE IS: ', USD[0], 'USD')
                print('****************************************')
                print('----------------------------------------')

# change pin
        elif response == 'p':
            print('-----------------------------')
            print('*****************************')
            new_pin = str(input('ENTER A NEW PIN: '))
            print('*****************************')
            print('-----------------------------')
            if new_pin != pins[0] and len(new_pin) == 4:
                print('------------------')
                print('******************')
                new_pins = str(input('CONFIRM NEW PIN: '))
                print('*******************')
                print('-------------------')
                if new_pins != new_pin:
                    print('------------')
                    print('************')
                    print('PIN MISMATCH')
                    print('************')
                    print('------------')
                else:
                    pins[0] = new_pin
                    print('NEW PIN SAVED')

            else:
                print('-------------------------------------')
                print('*************************************')
                print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
                print('*************************************')
                print('-------------------------------------')

# exit system
        elif response == 'q':
            exit()

        else:
            print('INVALID INPUT')
