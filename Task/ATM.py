# Write
# a
# program
# that
# would
# mimic
# the
# operations
# of
# an
# ATM
# machine.
# 1.
# Your
# application
# should
# have
# information
# of
# multiple
# users
# stored in a
# dictionary as listed
# below.
# {'username': 'trial', 'pin': 0000, 'balance': {'GHS': 140, 'USD': 0}
# 2. Provide an option to login.
#3. The application should have two operations that run fully after a user is logged in.
#     a.Withdraw
# Money and update
# balance
# for user after the withdrawal.
# b.Check balance of the user
# c.Give the user the opportunity to withdraw money again or to quit
# d.Ask the user if they want a receipt or not for their transaction and generate a simple print statement as a receipt
#
# 4. Go ahead and add any additional features you would want to add as well, make the program intuitive also(The user should know exactly what to do to get some form of response)
#
# 5. Finally make the program self executing.(Research how to make the codeexecute / self running, more or less like theshebang used in designing bash scripts to make it execute)

myAtmDictionary = {"user1" : {"Name" : "Esther", "pin" : "1111", "Balance" : {"GHS" : "150", "USD" : "850"}},
                   "user2" : {"Name" : "Nana", "pin" : "2222", "Balance" : {"GHS" : "200", "USD" : "950"}},
                   "user3" : {"Name" : "Ohemaa", "pin" : "3333", "Balance" : {"GHS" : "250", "USD" : "850"}}}

# print(myAtmDictionary["username"])
# print(myAtmDictionary["pin"])
# print(myAtmDictionary["Balance"])

userReply = input("Welcome, please enter your pin.")
if userReply == "1111":
     userInput = input("Hello " + myAtmDictionary["user1"]["Name"] + ", please press 1 to check your balance or 2 to make a withdrawal.(Type 1 or 2)")
     if userInput == "1":
        print("Your balance is GHS " + myAtmDictionary["user1"]["Balance"]["GHS"] + " and USD " + myAtmDictionary["user1"]["Balance"]["USD"])
     elif userInput == "2":
          print("You can withdraw a maximum of GHS " + str(int(myAtmDictionary["user1"]["Balance"]["GHS"]) - 50) + " and USD " + str(int(myAtmDictionary["user1"]["Balance"]["USD"]) - 50))
          userWithdrawal = input("Do you want to proceed with the withdrawal? Please press 1 for GHS, 2 for USD or 3 to cancel." )
          if userWithdrawal == "1":
              userAmount = input("Please enter the amount (GHS): ")
              myAtmDictionary["user1"]["Balance"]["GHS"] = str(int(myAtmDictionary["user1"]["Balance"]["GHS"]) - int(userAmount))
              print("Your new balance is GHS " + myAtmDictionary["user1"]["Balance"]["GHS"])
          elif userWithdrawal == "2":
              userAmount = input("Please enter the amount (USD): ")
              myAtmDictionary["user1"]["Balance"]["USD"] = str(int(myAtmDictionary["user1"]["Balance"]["USD"]) - int(userAmount))
              print("Your new balance is USD " + myAtmDictionary["user1"]["Balance"]["USD"])
          elif userWithdrawal == "3":
              print("Thank you for banking with us.")








