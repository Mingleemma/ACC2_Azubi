#Converting temperature in Degrees Celsius to Degrees Fahrenheit
celsius = float(input('Enter temperature in Celsius: '))

# calculate temperature in Fahrenheit
#f = c * 9/5 + 32
#1.8 = 9/5
fahrenheit = (celsius * 1.8) + 32
print('{}  Celsius is equal to {} degree Fahrenheit' .format (celsius, fahrenheit))