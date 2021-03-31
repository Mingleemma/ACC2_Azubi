import os
def new_user():
    confirm ="N"
    while confirm != "Y":
        username = str(input("Enter the name of the user to add: "))
        print("username '" + username + "'? (Y/N)")
        confirm = str(input("")).upper()
        os.system("sudo adduser " + username)

