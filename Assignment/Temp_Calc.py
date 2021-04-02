# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:19:29 2021

@author: Colin
"""

deg=int(input('Enter a temperature in degree celcius: '))

def temp_fahreinheit():
    F=(deg*5/2)+32
    return str(F) +' F'
temp_fahreinheit()