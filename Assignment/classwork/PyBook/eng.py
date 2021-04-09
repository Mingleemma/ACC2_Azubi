Acceptable_TEMP =102.5
temperature = float(input("Enter the substance Temperature: "))

while temperature >= Acceptable_TEMP:
    print("The temperature is too high. ")
    print("Turn the thermostat down and wait.....")
    print("5 min. Then take the temperature again")
    print("Enter it")
    temperature = float(input("Enter the new Temperature: "))
    
print("The temperature is acceptable. ")
print("Check it again in 15 min.")