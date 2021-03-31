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