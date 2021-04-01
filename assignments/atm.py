import getpass

users = {
	"Joshua": {
		"pin": '0000',
		"balance": [{'GHS': 140, 'USD': 10}]
	},
	"Aaron": {
		"pin": '1234',
		"balance": [{'GHS': 500, 'USD': 0}]
	},
	"Ivan": {
		"pin": '3698',
		"balance": [{'GHS': 0, 'USD': 30}]
	},
	"Ruby": {
		"pin": '2154',
		"balance": [{'GHS': 456,  'USD': 800}]
	},
	"Roland": {
		"pin": '0000',
		"balance": [{'GHS': 0,  'USD': 0}]
	},
}

account_type = [{1: 'GHS', 2: 'USD'}]

print('''       _             
      | |            
  __ _| |_ _ __ ___  
 / _` | __| '_ ` _ \ 
| (_| | |_| | | | | |
 \__,_|\__|_| |_| |_|''')

print('Welcome To The ATM')

isWorking = True
pin_attempts = 3

def withdraw(acc_type, currency):
	with_attempt = 3
	acc_typ = users[name]['balance'][0][currency]
	while with_attempt:
		if acc_type <=0 and acc_type >=3:
			print('Wrong input selected')
			with_attempt-=1
			print(f'You have {with_attempt} attempts remaining')
		else:
			amount = int(input('How much do you want to withdraw? '))
			if amount >=acc_typ:
				with_attempt-=1
				print('You have insufficient funds')
				print(f'You have {with_attempt} attempts remaining')
				print()
			else:
				receipt = input('Do you want a receipt of your transaction? y/n ').lower()
				if receipt == 'y' or receipt == 'y':
					print('Getting money ready .......')
					print('Withdrawal successful!!')
					acc_typ = acc_typ - amount
					print(f'You have {acc_typ} {currency} remaining')
					print()
				else:
					print('Transaction successful!')
					print()
				again=input("Do you want to withdraw again? y/n: ").lower()
				if again == 'n' or again == 'no':
					with_attempt = 0
					print("Goodbye")

def remaining_amount(name):
	acc_gh = users[name]['balance'][0]['GHS']
	acc_us = users[name]['balance'][0]['USD']
	print(f'Welcome {name}')
	print(f'You have {acc_gh} GHS in your cedi account and {acc_us} USD in your dollar account')
	print()

name = input("Please enter your name: ")
while isWorking:
	if name not in users:
		print(f'Hi {name}. You do not have an account. Kindly consider creating an account. Thanks')
		isWorking = False
	else:
		pin_number = getpass.getpass(prompt='Enter PIN number: ')
		if pin_number == users[name]['pin']:
			print(f'Welcome {name}. What do you want to do?')
			options = input('To withdraw money, press 1. To check balance, press 2: ')
			print()
			with_option = True
			while with_option:
				if options == '1':
					print('Which account you want to withdraw from?')
					account = int(input('Press 1 for cedi account or 2 for dollar account: '))
					if account >=3:
						print('Wrong option selected. Please select the correct one')
						with_option = False
						isWorking=False
					else:
						currency = account_type[0][1] if account == 1 else account_type[0][2]
						withdraw(account, currency)
						isWorking = False
						with_option = False
				elif options == '2':
					remaining_amount(name)
					with_option = False
					isWorking = False
				else:
					print('Wrong option selected!')	
					with_option = False
					isWorking = False
		else:
			pin_attempts-=1
			print('You entered the wrong pin number')
			print(f'You have {pin_attempts} attempts remaining')
			if pin_attempts == 0:
				isWorking = False

		
