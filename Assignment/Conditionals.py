# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:43:05 2021

@author: Colin
"""
response='yes'
while response=='yes':
    userInput=input('What is your name ')
    userInput=userInput.lower()
    if userInput=='adwoa' or userInput=='kojo':
        if userInput=='kojo':
            print('You are a boy born on Monday')
        elif userInput=='adwoa':
            print('You are a girl born on Monday')
    else:
        print('You were not born on Monday')
    response = input('Do you want to check for another name (yes/no)')
    reponse=response.lower()
    while response!='yes' and response!='no':
        response = input('Do you want to check for another name (yes/no)')
        response=response.lower()
        