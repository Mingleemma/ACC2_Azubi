# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:43:05 2021

@author: Colin
"""

letters=['a','b','c','d']
num=[1,2,3,4]
for x in letters:
    for y in num:
        print(str(x) +'is to' +str(y))
        
output=['Finance', 'Accounting', 'HR', 'Sales', 'Media', 'IT']
subgroup=['Accounting', 'Finance', 'Sales', 'Legal', 'Operations']

print('\n')

for i in output:
    for j in subgroup:
        if j==i:
            found = True
            print('This is an existing group: '+ j)
print('This is not an existing group: '+j)
