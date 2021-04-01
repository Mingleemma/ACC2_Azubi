This application seeks to replicate the operations of an ATM.


**Customer Information**
The userData dictionary contains details of registered users; usernames, pins and balances.


**Login**
The user is asked to input their username, their input is then checked against the userData
dictionary. The input is meant to be case-sensitive. If the input is not found in the dictionary,
the user is asked to input the username again.
If the input is contained in the dictionary, the user is asked to input their pin.

The pin is then matched against the pin in the dictionary of username that was input. 
User is logged in if the pin matches the username.

**Menu Function**
A function, mainmenu, is defined with all operations of the ATM. The function starts by asking the
user their preferred action among checking balance, withdrawing funds, requesting a statement and exiting.
A function, pester, is nested within this function to give the user the option of performing another transaction.

**Check Balance**
When the user enters one in the main menu, the user's balance is retrieved from the dictionary.

**Withdraw funds**
The user owns two accounts, cedi and dollar account. The user specifies the account to be drawn and
the amount to be withdrawn. For the cedi account, a minimum balance of GHS5 must be maintained whereas
the minimum balance on the dollar account is $2. 
After the user specifies the desired withdrawal amount, it is verified against the available balance if
the minimum balance would be maintained. If not, the user is asked to enter a different amount. If yes,
the user receives the cash and may opt for a receipt.
The users available balance is then updated.

**Request statement**
The user may request a statement for past 10 or 30 days or 3 months. The statement would be sent via email.