# python 3.9
# programme cloning an ATM machine

# defining users in database with nested dictionary in dictionary
# username used as first key

userIDs = {
    'JustBarca45': {
        'pin': 1598,
        "balance": "{'GHS': 1,516,350.67, 'USD': 0}",
    },
    'ThePiresChip': {
        'pin': 8417,
        "balance": "{'GHS': 78,082.40, 'USD': 584.10}",
    },
    'Registability': {
        'pin': 2681,
        "balance": "{'GHS': 233,086.62, 'USD': 375,000.00",
    },
}

# user login
# Requesting username
for username in userIDs:
    username = input("Please enter your username:\n ")
    if username in userIDs:
        pinRequest = input("Please enter your pin:\n ")
    else:
        print("Incorrect username")