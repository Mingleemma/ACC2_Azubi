#  imports 
import datetime

account = {'username':'Paula', 'pin': 1234 , 'balance':{'GHS': 140, 'USD':0}}





class Atm:
    def login(self):
        isLogIn = False
        
        while(isLogIn == False):
            userName = str(input("Please enter your username: "))
            pin = int(input("Please enter your pin: "))
        
            if userName == account['username'] and pin == account['pin']:
                isLogIn = True
                return True
            elif userName != account['username'] and pin == account['pin']:
                print("Wrong user name! Try again")
            elif userName == account['username'] and pin != account['pin']:
                print("Wrong pin! Try again")
            else:
                print("Wrong pin as well as username!")

    def balance(self): 
                  
        print("Your balance is "+str(account['balance']['GHS']))

        cont = input("""
        Continue using ATM?
        Yes
        No
        """)
        if(cont.lower() == "yes"):
            logic()
        else:
            exit()
        
        return True


    

    def do_deposit(self): 
        while(True):
            try:
                
                deposit = float(input("Enter your deposit\n"))
                if deposit <= 0:
                    print("\nThe deposit should be greater than 0 (Zero)") 
                    continue 
            except ValueError as e: 
                print("This should be a decimal or an integer . Re-enter the deposit again")
                continue
                    
            break    
               
        account['balance']['GHS'] = account['balance']['GHS']+deposit
        print("Your new balance is "+str(account['balance']['GHS']))

        cont = input("""
        Continue using ATM?
        Yes
        No
        """)
        if(cont.lower() == "yes"):
            logic()
        else:
            exit()
        
        return True

    def do_withdrawal(self):
        
        while(True):
            try:
                amount = float(input("Enter amount you want to withdraw.\n"))
                while amount <=  0:
                    print("\nAmount must be greater than Zero")
                    amount = float(input("Enter amount you want to withdraw.\n"))

                 
            except ValueError as e:
                print("Amount must be an integer or a decimal.Re-enter...")
                continue
            break    
        if amount < float(account['balance']['GHS']):
            account['balance']['GHS'] = account['balance']['GHS']-amount
            print("Transaction is sucessful")
            print(" A withdrawal of " + str(amount) + ' has been made.')
            cont = input("""
                Continue using ATM?
                Yes
                No
                """)
            if(cont.lower() == "yes"):
                logic()
            else:
                exit()
        else:
            print("Insufficient funds!")
            cont = input("""
                Continue using ATM?
                Yes
                No
                """)
            if(cont.lower() == "yes"):
                logic()
            else:
                exit()


    def do_transfer(self):
        rep_acc_number = input("Enter the receiver's account number below\n")
        
        while(True):

            try:
                amount = float(input("Enter the amount you want to send.\n"))
                if amount > 0:
                    break
                else:
                    continue    
            except ValueError as e:
                print("\nThe value must be a number, not an alphabet")
                continue

        if amount >= account['balance']['GHS']:
            print("Failed")
            print("Transafer amount greater than the balance in your account at the momment.")
            cont = input("""
                Continue using ATM?
                Yes
                No
                """)
            if(cont.lower() == "yes"):
                logic()
            else:
                exit()
        else:
            account['balance']['GHS'] -= amount
            print("Transfer sucessful.")
            print(" An amount of " + str(amount) + " has been sent to " + str(rep_acc_number))
            print("Current balance is: " + str(account['balance']['GHS'])+".")
            cont = input("""
                Continue using ATM?
                Yes
                No
                """)
            if(cont.lower() == "yes"):
                logic()
            else:
                exit()


def Driver_code():

    print("Welcome to Paula's ATM ")
    obj= Atm() # Creating the ATM class instance 

    if(obj.login()):
        logic()
            
            
def logic():
    obj= Atm() # Creating the ATM class instance 
    print("You can choose from the options below.")
    print("\n\n\n1. Deposit\n" + "2. Withdraw cash\n" + "3. Transfer cash to another wallet\n"\
        + "4. Check current balance\n" + "9. Exit program\n")

    choice = input("Enter prefered choice\n")
    try:
        if choice == '1':
            print("Deposit initiated...\n")
            obj.do_deposit()
            
        elif choice == '2':
            print("Withdrawal initiated...\n")
            obj.do_withdrawal()
                 
        elif choice == '3':
            print("Transfer action intiated...\n")
            obj.do_transfer()  
            
        elif choice == '4':
            print("checking balance done...\n")
            obj.balance()  
    
        else:
            exit()
    except ValueError as e:
        print("You made a wrong choice")


Driver_code() # This is the main code 