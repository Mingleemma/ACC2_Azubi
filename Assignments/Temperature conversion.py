#converting degree celsius to Fahrenheit

def celtoFah():
    y = (9/5 * x) + 32
    return y
x = int(input("Input Celsisus temperature "))

print(celtoFah())

#another way
degree_cel = int(input("Kindly input your temperature in degree Celsius to be converted "))

def change_Cel_to_Fah():
     y = (9/5 * degree_cel) + 32
     return round( y , 2)


print("The temperature in Fahrenheit is " + str(change_Cel_to_Fah()))






