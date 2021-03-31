# Pass in the input
# Calc Fahrenheit = 9/5*DegC + 32

deg_celsius = int(input("Enter temperature in Celsius: "))


def Temp_Fahrenheit(deg_celsius):
    f = ((deg_celsius * 9 / 5) + 32)
    return round(f, 2)


print(f"Your Temperature in Fahrenheit is: {Temp_Fahrenheit(deg_celsius)}")
