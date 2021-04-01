#!/usr/bin/python
import functions

# this is sample of how we can use the login function for the whole system
if functions.login():
    functions.startMenu()  
else:
    # we simply log out the user due to failure to log in
    exit()
