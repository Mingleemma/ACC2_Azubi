# Azubi ATM
# Dictionary containing users

atmUser = {'Trudy': {'pin': '1234', 'balance': {'GHC': 143384, 'USD': 233}},
           'Maureen': {'pin': '0000', 'balance': {'GHC': 213243, 'USD': 4346}},
           'Maud': {'pin': '7834', 'balance': {'GHC': 94949, 'USD': 7832}}
           }

print("\n *** Welcome to the ATM *** ")

# Global variables

atmBool = True
loginAttempts = 3

# Function for deposits

def deposit(name):
    cediAcct = atmUser[name]['balance']['GHC']  # balance in cedi account per user
    usdAcct = atmUser[name]['balance']['USD']   # balance in dollar account per user

    print('\nAccount to deposit into? \t1)GHC \t2)USD')
    
    userInput = int(input('\nEnter selection: '))

# Logic to check user's input

    if userInput == 1:
        amount = int(input('\nEnter amount to deposit: '))

        cediAcct += amount
        
        print(f'\nYou made a deposit of GHC {amount}. Your current balance is GHC {cediAcct}')
        print('\nTransaction successful')
    
    elif userInput == 2:
        amount = int(input('\nEnter amount to deposit: '))
 
        usdAcct += amount
        
        print(f'\nYou made a deposit of USD {amount}. Your current balance is USD {usdAcct}')
        print('\nTransaction successful')

    
    else:
        print('\nInvalid input.')


# Function for Withdrawal

def withdraw(name):
    cediAcct = atmUser[name]['balance']['GHC']  # repeated since the previous one was a local variable
    usdAcct = atmUser[name]['balance']['USD']

    print('\nAccount to withdraw from: \t1) GHC \t2) USD')
    
    userInput = int(input('Enter option: '))

    if userInput == 1:
        amount = int(input('\nEnter amount to withdraw: '))
      
        if amount >= cediAcct:
            print(f'\n{name}, insufficient funds in account.')
     
        else:
            cediAcct -= amount
            print(f'\nYou withdrew GHC {amount}. You have GHC {cediAcct} left.')
            print('\nTransaction successful')
    
    elif userInput == 2:
        amount = int(input('\nEnter amount to withdraw: '))
        
        if amount >= usdAcct:
            print(f'\n{name}, insufficient amount in account.')
        else:
            usdAcct -= amount
            print(f'\nYou withdrew USD {amount}. You have USD {usdAcct} left.')
            print('\nTransaction successful')
    
    else:
        print('\nInvalid input')

# Function to check for balance

def acctBalance(name):
    cediAcct = atmUser[name]['balance']['GHC']
    usdAcct = atmUser[name]['balance']['USD']

    print('\nAccount: \t1) GHC\t2) USD')
    userInput = int(input('\nEnter option: '))

    if userInput == 1:
        print(f'\nYour balance is GHC {cediAcct}')

    elif userInput == 2:
        print(f'\nYour balance is USD {usdAcct}')

    else:
        print('\nWrong input')


while atmBool and loginAttempts >= 1:
    name = input('\nEnter username: ')

# checks if entered name is in the atmUser dictionary  
 
    if name not in atmUser:
        print(f'\nHi {name}, no account found.')
        atmBool = False             # escapes loop
   
    else:
        print(f'\nWelcome {name}')

        userpin = input('Enter 4-digit PIN: ')   

# checks if entered pin by user is in the atmUser dictionary        
 
        if userpin != atmUser[name]['pin']:
            print('\nWrong pin')
            loginAttempts -= 1
            print(f'\n{loginAttempts} attempts left.')
            
        else:
            print('\nLogin successful\n')
            print('Menu:\n\t1) Check Balance\t2) Withdraw \t3) Deposit \t4) Exit')

            option = int(input('\nEnter option: '))
            
            if option == 1:
                acctBalance(name)       # calls function to check for balance
                atmBool = False
           
            elif option == 2:
                withdraw(name)          # calls function withdraw
                atmBool = False
           
            elif option == 3:
                deposit(name)           # calls the deposit function
                atmBool = False
            
            elif option == 4:
                atmBool = False 
            
            else:
                print('\nWrong input. Would you like to try again? Y/N')

                try2 = input('\nEnter selection: ')
                try2 = try2.upper()

                if try2 == 'N':
                    atmBool = False
