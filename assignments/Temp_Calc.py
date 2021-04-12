# My Temperature Convertor
# Celcius = (F - 32) * (5/9)
# Fahrenhite = (9/5 * C) + 32
print("Welcome to the Temperature Convertor")
def temp_convert(c):
    f = (9/5 * c) + 32
    return f

celcius = float(input("Enter temperature in celcius: "))
print(temp_convert())